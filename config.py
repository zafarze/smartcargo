# -*- coding: utf-8 -*-
# config.py
# 🚀 SmartCargo Configuration
# Senior Code Edition: Fixed States & Paths

import logging
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# --- 1. Настройка логирования ---
logger = logging.getLogger(__name__)

# --- 2. Определение путей ---
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / '.env'

# --- 3. Загрузка переменных окружения (.env) ---
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    logger.info(f"✅ Файл .env найден: {env_path}")
else:
    logger.warning("⚠️ Файл .env не найден (возможно, переменные заданы в системе)")

BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DATABASE_URL = os.environ.get("DATABASE_URL")

# Критическая проверка
if not BOT_TOKEN:
    logger.critical("❌ FATAL: TELEGRAM_TOKEN не найден! Проверьте .env")
    sys.exit(1)

if not DATABASE_URL:
    logger.critical("❌ FATAL: DATABASE_URL не найден! Проверьте .env")
    sys.exit(1)

# --- 4. Настройки SmartCargo ---
PROJECT_NAME = "SmartCargo"
XLSX_FILENAME = "SmartCargo.xlsx"
CHANNEL_USERNAME = "+mzHC2tsmw65mOGY1"
SUPPORT_USERNAME = "@smartcargo_support" 

# --- 5. ID Администраторов ---
ADMIN_USER_IDS = [
    515809298,   # Zafar
    6778668416,  # Али
]

# --- 6. Настройки Фоновых Задач (JOBS) --- 
JOBS = {
    'reload_codes': {
        'enabled': True,
        'interval': 300,  # Каждые 5 минут
        'first': 10
    },
    'notify_dushanbe': {
        'enabled': True,
        'interval': 300,  # Каждые 5 минут
        'first': 15
    }
}

# --- 7. Пути к Медиа ---
IMG_DIR = BASE_DIR / "img"

PHOTO_CONTACT_PATH = IMG_DIR / "contacts.jpg"
PHOTO_PRICE_PATH = IMG_DIR / "price.jpg"
PHOTO_ADDRESS_TAJIK_PATH = IMG_DIR / "address_tajik.jpg"

PHOTO_FORBIDDEN_PATH = IMG_DIR / "forbidden.jpg"

# Китай
PHOTO_ADDRESS_CHINA_PATH = IMG_DIR / "address_china.jpg"
PHOTO_ADDRESS_CHINA_2_PATH = IMG_DIR / "address_china-2.jpg" # <--- ДОБАВИЛИ ЭТУ СТРОКУ

VIDEO_ADDRESS_TAJIK_PATH = IMG_DIR / "address_tajik.mov"

# --- 8. Состояния Разговора ---
(
    START_ROUTES,               # 0
    AWAITING_SUBSCRIPTION,      # 1
    MAIN_MENU,                  # 2
    LK_MENU,                    # 3
    ADMIN_MENU,                 # 4
    AWAITING_FULL_NAME,         # 5
    AWAITING_PHONE,             # 6
    AWAITING_ADDRESS,           # 7
    AWAITING_LANG_CHOICE,       # 8
    AWAITING_TRACK_CODE,        # 9
    LK_WAITING_FOR_TRACK,       # 10
    
    # Новые состояния для доставки и админки:
    LK_AWAIT_DELIVERY_ADDRESS,  # 11
    LK_AWAIT_PROFILE_ADDRESS,   # 12
    LK_AWAIT_PHONE,             # 13
    AWAITING_BROADCAST_MESSAGE, # 14
    CONFIRM_BROADCAST,          # 15
    ADMIN_AWAIT_SEARCH_CODE,    # 16
    ADMIN_AWAIT_ORDER_CODE,     # 17
    ADMIN_AWAIT_ORDER_STATUS,   # 18
    ADMIN_AWAIT_ORDER_DATE_YIWU,# 19
    ADMIN_AWAIT_ORDER_DATE_DUSH # 20
) = range(21)

logger.info(f"✅ Конфигурация {PROJECT_NAME} успешно инициализирована.")