# -*- coding: utf-8 -*-
# jobs.py
# 🔄 SmartCargo Background Jobs
# Handles scheduled tasks: Notifications & Data Sync

import asyncio
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

# Импорты конфигурации
from config import logger, XLSX_FILENAME, BASE_DIR
from admin_utils import notify_admins

# Импортируем логику из других модулей, чтобы не дублировать код
# (Убедитесь, что handlers.py не импортирует jobs.py, иначе будет ошибка цикла)
from handlers import get_text, process_excel_to_db

from db_utils import (
    get_dushanbe_arrivals_to_notify,
    set_dushanbe_notification_sent
)

# === 1. ЗАДАЧА: ОПОВЕЩЕНИЕ О ПРИБЫТИИ В ДУШАНБЕ ===

async def notify_dushanbe_arrival_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Периодическая задача:
    1. Проверяет БД на наличие заказов со статусом 'Душанбе', по которым еще не было уведомления.
    2. Отправляет уведомление пользователю на его языке.
    3. Отмечает в БД, что уведомление отправлено.
    """
    logger.info("⏱️ Job: Проверка поступлений в Душанбе...")
    
    try:
        # Получаем список заказов, владельцев которых надо уведомить
        # Функция должна возвращать список словарей: {'user_id': int, 'track_code': str, 'language_code': str}
        orders_to_notify = await get_dushanbe_arrivals_to_notify()

        if not orders_to_notify:
            logger.debug("Job: Нет новых поступлений для уведомления.")
            return

        logger.info(f"Job: Найдено {len(orders_to_notify)} заказов для уведомления.")
        
        # Создаем задачи для параллельной отправки (чтобы не ждать каждого по очереди)
        notification_tasks = []
        for order in orders_to_notify:
            notification_tasks.append(
                send_notification_safe(
                    context, 
                    order['user_id'], 
                    order['track_code'], 
                    order['language_code']
                )
            )
        
        # Запускаем все уведомления разом
        
        await asyncio.gather(*notification_tasks)

    except Exception as e:
        logger.error(f"❌ CRITICAL Notify Job Error: {e}", exc_info=True)
        # Уведомляем админа о поломке джобы, чтобы не пропустить сбой
        await notify_admins(context.bot, f"❌ Ошибка в задаче уведомлений (Notify Job):\n{e}")

async def send_notification_safe(context: ContextTypes.DEFAULT_TYPE, user_id: int, track_code: str, lang: str):
    """
    Вспомогательная функция отправки одного уведомления с подавлением ошибок (чтобы один сбой не ломал все).
    """
    try:
        # 1. Формируем текст
        # Берем шаблон из texts.py и подставляем код
        template = get_text('dushanbe_arrival_notification', lang)
        message_text = template.format(code=track_code)
        
        # 2. Отправляем
        await context.bot.send_message(
            chat_id=user_id,
            text=message_text,
            parse_mode=ParseMode.HTML
        )
        
        # 3. Отмечаем успех в БД (чтобы не спамить пользователю каждые 5 минут)
        await set_dushanbe_notification_sent(track_code)
        logger.info(f"✅ Уведомление отправлено пользователю {user_id} (Трек: {track_code})")
        
    except Exception as e:
        # Если бот заблокирован пользователем - это не ошибка системы, просто игнорим
        error_str = str(e).lower()
        if "bot was blocked" in error_str or "user is deactivated" in error_str:
            logger.warning(f"⚠️ Не удалось уведомить {user_id}: Пользователь заблокировал бота.")
            # Можно пометить в БД как 'sent' или 'failed', чтобы не пытаться снова, 
            # но пока оставим как есть, вдруг разблокирует.
        else:
            logger.error(f"⚠️ Ошибка отправки уведомления {user_id}: {e}")


# === 2. ЗАДАЧА: АВТО-ИМПОРТ EXCEL (Синхронизация) ===

async def reload_codes_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Периодическая задача:
    Пытается найти файл SmartCargo.xlsx на сервере и обновить базу данных.
    """
    logger.info(f"⏱️ Job: Авто-обновление базы из {XLSX_FILENAME}...")
    
    file_path = BASE_DIR / XLSX_FILENAME
    
    # Проверка существования файла перед запуском тяжелой логики
    if not file_path.exists():
        logger.warning(f"Job: Файл {XLSX_FILENAME} не найден. Пропускаю обновление.")
        return

    try:
        # Вызываем единую логику импорта (ту же, что и при ручной загрузке админом)
        # process_excel_to_db берет на себя чтение, парсинг и обновление БД
        stats = await process_excel_to_db(str(file_path))
        
        logger.info(f"Job: Обновление завершено. Статистика: {stats}")
        
        # Уведомляем админов только если есть критическая ошибка или проблемы
        if stats.get('error'):
             await notify_admins(
                context.bot,
                f"⚠️ <b>Авто-обновление (Job):</b> Ошибка!\n"
                f"<code>{stats['error']}</code>"
            )
        # Если много ошибок в строках, тоже можно маякнуть (раскомментируй при желании)
        # elif stats.get('failed', 0) > 10:
        #     await notify_admins(...)
            
    except Exception as e:
        logger.error(f"❌ CRITICAL Migration Job Error: {e}", exc_info=True)
        await notify_admins(context.bot, f"❌ Критическая ошибка авто-обновления:\n{e}")