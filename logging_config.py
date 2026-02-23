# -*- coding: utf-8 -*-
# logging_config.py
# 📝 SmartCargo Logging System

import logging
import sys
import os
from logging.handlers import RotatingFileHandler

def setup_logging():
    """Настраивает систему логирования для всего приложения."""
    
    # Определяем базовую директорию (где лежит этот файл)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

    # Создаем папку 'logs', если ее нет
    if not os.path.exists(LOG_DIR):
        try:
            os.makedirs(LOG_DIR)
        except OSError as e:
            print(f"Warning: Could not create log directory {LOG_DIR}. {e}", file=sys.stderr)

    # Пути к файлам логов
    log_file = os.path.join(LOG_DIR, 'bot.log')
    error_log_file = os.path.join(LOG_DIR, 'error.log')

    # --- Настройка корневого логгера ---
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    
    # Очистка старых хендлеров (чтобы не дублировались при перезапуске)
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # --- Форматтер ---
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # --- 1. Консоль (StreamHandler) ---
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # --- 2. Основной файл (RotatingFileHandler) ---
    try:
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, # 5 MB
            backupCount=5, 
            encoding='utf-8'  # Важно для Таджикского языка
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    except Exception as e:
        print(f"Error setting up log file: {e}", file=sys.stderr)

    # --- 3. Файл ошибок (FileHandler) ---
    try:
        error_handler = logging.FileHandler(error_log_file, mode='a', encoding='utf-8')
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)
        root_logger.addHandler(error_handler)
    except Exception as e:
        print(f"Error setting up error log file: {e}", file=sys.stderr)

    # --- Фильтры (Убираем шум) ---
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("telegram.ext").setLevel(logging.WARNING)
    logging.getLogger("apscheduler").setLevel(logging.WARNING)

    # Финальный лог
    logging.getLogger(__name__).info("✅ SmartCargo Logging System Initialized")