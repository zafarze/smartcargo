# -*- coding: utf-8 -*-
# admin_utils.py
# 🛡️ SmartCargo Admin Utilities
# Handles notifications for administrators safely

import asyncio
from telegram.constants import ParseMode
from telegram.error import Forbidden, BadRequest
from config import logger, ADMIN_USER_IDS

async def notify_admins(bot, message: str, parse_mode=ParseMode.HTML):
    """
    Асинхронно отправляет сообщение всем админам из списка ADMIN_USER_IDS.
    По умолчанию использует HTML разметку.
    """
    if not ADMIN_USER_IDS:
        logger.warning("⚠️ Список админов пуст! Некому отправлять уведомление.")
        return

    tasks = []
    for admin_id in ADMIN_USER_IDS:
        # Создаем задачу для каждого админа
        tasks.append(send_admin_message(bot, admin_id, message, parse_mode))
    
    # Запускаем все задачи параллельно (это намного быстрее, чем цикл)
    # 
    await asyncio.gather(*tasks)

async def send_admin_message(bot, admin_id: int, message: str, parse_mode=None):
    """
    Отправляет одно сообщение конкретному админу с обработкой исключений.
    """
    try:
        await bot.send_message(
            chat_id=admin_id,
            text=message,
            parse_mode=parse_mode
        )
        # Используем debug, чтобы не спамить в логах при успешной рассылке
        logger.debug(f"✅ Уведомление отправлено админу {admin_id}")

    except Forbidden:
        logger.warning(f"⚠️ Админ {admin_id} заблокировал бота (Forbidden).")
    
    except BadRequest as e:
        if "chat not found" in str(e).lower():
            logger.error(f"⚠️ Чат с админом {admin_id} не найден (возможно, он не нажал /start).")
        else:
            logger.error(f"⚠️ Ошибка отправки админу {admin_id}: {e}")
            
    except Exception as e:
        logger.error(f"❌ Непредвиденная ошибка при отправке админу {admin_id}: {e}")