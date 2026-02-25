# -*- coding: utf-8 -*-
# jobs.py
# 🔄 SmartCargo Background Jobs
# Handles scheduled tasks: Notifications & Data Sync

import asyncio
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from telegram.error import Forbidden  # <--- ВАЖНО: Добавлен импорт ошибки

# Импорты конфигурации
from config import logger, XLSX_FILENAME, BASE_DIR
from admin_utils import notify_admins

# Импортируем логику из других модулей
from handlers import get_text, process_excel_to_db

from db_utils import (
    get_dushanbe_arrivals_to_notify,
    set_dushanbe_notification_sent
)

# === 1. ЗАДАЧА: ОПОВЕЩЕНИЕ О ПРИБЫТИИ В ДУШАНБЕ ===

async def notify_dushanbe_arrival_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Периодическая задача:
    1. Проверяет БД на наличие заказов со статусом 'Душанбе'.
    2. Отправляет уведомление.
    FIX: Если юзер заблокировал бота, помечаем как отправленное, чтобы не зацикливаться.
    """
    logger.info("⏱️ Job: Проверка поступлений в Душанбе...")
    
    try:
        # Получаем список заказов для уведомления
        orders_to_notify = await get_dushanbe_arrivals_to_notify()

        if not orders_to_notify:
            logger.info("Job: Нет новых поступлений для уведомления.")
            return

        logger.info(f"Job: Найдено {len(orders_to_notify)} заказов для уведомления.")
        
        # Создаем задачи для параллельной отправки
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
        
        await asyncio.gather(*notification_tasks)

    except Exception as e:
        logger.error(f"❌ CRITICAL Notify Job Error: {e}", exc_info=True)
        # Можно временно отключить уведомление админам, если ошибок слишком много
        # await notify_admins(context.bot, f"❌ Ошибка в задаче уведомлений:\n{e}")

async def send_notification_safe(context: ContextTypes.DEFAULT_TYPE, user_id: int, track_code: str, lang: str):
    """
    Отправка одного уведомления.
    """
    try:
        template = get_text('dushanbe_arrival_notification', lang)
        message_text = template.format(code=track_code)
        
        await context.bot.send_message(
            chat_id=user_id,
            text=message_text,
            parse_mode=ParseMode.HTML
        )
        
        # Успех -> отмечаем в базе
        await set_dushanbe_notification_sent(track_code)
        logger.info(f"✅ Уведомление отправлено пользователю {user_id} (Трек: {track_code})")
        
    except Forbidden:
        # --- ГЛАВНОЕ ИСПРАВЛЕНИЕ ЗДЕСЬ ---
        # Если бот заблокирован (Forbidden), мы всё равно помечаем уведомление как отправленное!
        # Иначе бот будет пытаться отправить его каждые 5 минут вечно.
        logger.warning(f"🚫 Пользователь {user_id} заблокировал бота. Помечаем заказ {track_code} как обработанный, чтобы не спамить ошибками.")
        await set_dushanbe_notification_sent(track_code)
        
    except Exception as e:
        # Другие ошибки (например, сети) можно оставить для повторной попытки
        # Но если ошибка "Chat not found", это тоже тупик, лучше пометить.
        error_str = str(e).lower()
        if "chat not found" in error_str:
             logger.warning(f"🚫 Чат с {user_id} не найден. Помечаем заказ {track_code} как обработанный.")
             await set_dushanbe_notification_sent(track_code)
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
        # Вызываем единую логику импорта
        stats = await process_excel_to_db(str(file_path))
        
        logger.info(f"Job: Обновление завершено. Статистика: {stats}")
        
        if stats.get('error'):
             await notify_admins(
                context.bot,
                f"⚠️ <b>Авто-обновление (Job):</b> Ошибка!\n"
                f"<code>{stats['error']}</code>"
            )
            
    except Exception as e:
        logger.error(f"❌ CRITICAL Migration Job Error: {e}", exc_info=True)
        await notify_admins(context.bot, f"❌ Критическая ошибка авто-обновления:\n{e}")