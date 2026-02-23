# -*- coding: utf-8 -*-
# bot.py
# 🚀 SmartCargo Main Entry Point
# Senior Code Edition: Clean, Robust & Async

import logging
import asyncio
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
    Defaults
)
from telegram.constants import ParseMode

# --- Настройка логов ---
from logging_config import setup_logging

# --- 1. Загрузка переменных окружения ---
env_path = Path(__file__).resolve().parent / '.env'

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print(f"✅ Файл .env найден: {env_path}")
else:
    print("⚠️ Файл .env НЕ НАЙДЕН! (Бот попробует использовать системные переменные)")

# --- 2. Импорты модулей ---
import config
from config import BOT_TOKEN, logger, JOBS, ADMIN_USER_IDS

# ВАЖНО: Мы убрали address_callback из импортов, так как он больше не нужен снаружи
from handlers import (
    get_main_conv_handler,
    get_broadcast_conv_handler,
    get_admin_conv_handler,
    document_handler,
    admin_mark_delivered,
    link_order_callback,
    error_handler
)

from jobs import (
    reload_codes_job,
    notify_dushanbe_arrival_job
)
from db_utils import init_db_pool, close_db_pool, get_db, release_db, get_all_users_count, execute_query

# --- 3. Функции Жизненного Цикла ---

async def post_init(app: Application) -> None:
    """Выполняется один раз после успешного запуска бота."""
    logger.info("🚀 SmartCargo Bot успешно инициализирован!")
    
    # Проверка наличия фото
    from config import (
        PHOTO_CONTACT_PATH, PHOTO_PRICE_PATH, 
        PHOTO_ADDRESS_TAJIK_PATH, PHOTO_ADDRESS_CHINA_PATH
    )
    
    files_to_check = {
        "Контакты": PHOTO_CONTACT_PATH,
        "Тарифы": PHOTO_PRICE_PATH,
        "Адрес ТЖ": PHOTO_ADDRESS_TAJIK_PATH,
        "Адрес CN": PHOTO_ADDRESS_CHINA_PATH
    }
    
    for name, path in files_to_check.items():
        if path.exists():
            logger.info(f"📁 Медиа '{name}' найден: {path.name}")
        else:
            logger.warning(f"⚠️ Медиа '{name}' НЕ НАЙДЕН: {path}")

async def post_shutdown(app: Application) -> None:
    """Выполняется при остановке бота."""
    logger.info("🛑 Бот останавливается...")
    await asyncio.to_thread(close_db_pool)

# --- 4. Служебные команды ---

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает состояние системы (только для админов)."""
    user_id = update.effective_user.id
    if user_id not in ADMIN_USER_IDS:
        return

    try:
        users_count = await asyncio.to_thread(get_all_users_count)
        status_text = (
            "📊 <b>SmartCargo System Status</b>\n\n"
            f"✅ <b>Core:</b> Online\n"
            f"👥 <b>Users:</b> {users_count}\n"
            f"🤖 <b>Version:</b> 3.0 (Senior Delivery Update)"
        )
        await update.message.reply_text(status_text, parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(f"Status command error: {e}")

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 <b>SmartCargo Bot</b> на связи!\nСистемы работают нормально.",
        parse_mode=ParseMode.HTML
    )

# --- 5. Main ---

def main() -> None:
    # 5.1 Настройка логов
    setup_logging()
    
    # 5.2 Проверка токена
    if not BOT_TOKEN:
        logger.critical("❌ FATAL: Токен бота не найден в .env!")
        return

    # 5.3 Инициализация БД
    try:
        init_db_pool()
    except Exception as e:
        logger.critical(f"❌ FATAL: Ошибка инициализации БД: {e}")
        return

    # 5.4 Настройка Persistence
    persistence = PicklePersistence(filepath="bot_persistence.pickle")

    # 5.5 Сборка приложения
    defaults = Defaults(parse_mode=ParseMode.HTML)
    
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .persistence(persistence)
        .defaults(defaults)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .connect_timeout(60.0)
        .read_timeout(60.0)
        .write_timeout(60.0)
        .build()
    )

    # 5.6 Настройка JobQueue
    job_queue = application.job_queue

    if JOBS.get('reload_codes', {}).get('enabled'):
        job_queue.run_repeating(
            reload_codes_job,
            interval=JOBS['reload_codes']['interval'],
            first=JOBS['reload_codes']['first']
        )

    if JOBS.get('notify_dushanbe', {}).get('enabled'):
        job_queue.run_repeating(
            notify_dushanbe_arrival_job,
            interval=JOBS['notify_dushanbe']['interval'],
            first=JOBS['notify_dushanbe']['first']
        )

    # 5.7 Регистрация Хендлеров
    
    # Группа 0: Основные диалоги
    application.add_handler(MessageHandler(filters.Document.ALL, document_handler), group=0)
    application.add_handler(get_broadcast_conv_handler(), group=0)
    application.add_handler(get_admin_conv_handler(), group=0)
    application.add_handler(get_main_conv_handler(), group=0)
    
    # Группа 1: Команды и кнопки
    application.add_handler(CommandHandler("delivered", admin_mark_delivered), group=1)
    application.add_handler(CommandHandler("status", status_command), group=1)
    application.add_handler(CommandHandler("test", test_command), group=1)
    
    # Кнопка "Привязать заказ" (единственный колбэк, который остался вне диалогов)
    application.add_handler(CallbackQueryHandler(link_order_callback, pattern='^link_'), group=1)
    
    # ВАЖНО: Мы убрали 'addr_' handler, потому что он теперь внутри get_main_conv_handler

    # Обработчик ошибок
    application.add_error_handler(error_handler)

    # 5.8 Запуск
    logger.info("🚀 Бот запускается...")
    
    try:
        application.run_polling(drop_pending_updates=True)
    except Exception as e:
        logger.critical(f"❌ Ошибка Polling: {e}")

if __name__ == "__main__":
    main()