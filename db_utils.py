# -*- coding: utf-8 -*-
# db_utils.py
# 🗄️ SmartCargo Database Layer
# Supports Senior Handlers

import psycopg2
from psycopg2 import pool, extras
import asyncio
from datetime import datetime
from urllib.parse import urlparse
import logging

from config import DATABASE_URL

logger = logging.getLogger(__name__)
db_pool = None

# --- 1. Управление Подключением ---

def init_db_pool():
    global db_pool
    try:
        result = urlparse(DATABASE_URL)
        username = result.username
        password = result.password
        database = result.path[1:]
        hostname = result.hostname
        port = result.port
        
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 20,
            user=username,
            password=password,
            host=hostname,
            port=port,
            database=database
        )
        if db_pool:
            logger.info("✅ PostgreSQL Connection Pool created successfully")
            create_tables()
    except Exception as e:
        logger.critical(f"❌ Error creating connection pool: {e}")
        raise e

def close_db_pool():
    global db_pool
    if db_pool:
        db_pool.closeall()
        logger.info("🔌 Database pool closed.")

def get_db():
    global db_pool
    if not db_pool: return None
    try:
        return db_pool.getconn()
    except Exception as e:
        logger.error(f"Error getting connection: {e}")
        return None

def release_db(conn):
    global db_pool
    if db_pool and conn:
        db_pool.putconn(conn)

# --- 2. Таблицы ---

def create_tables():
    conn = get_db()
    if not conn: return
    queries = [
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username VARCHAR(255),
            full_name VARCHAR(255),
            phone_number VARCHAR(50),
            address TEXT,
            language_code VARCHAR(10) DEFAULT 'ru',
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS orders (
            track_code VARCHAR(255) PRIMARY KEY,
            user_id BIGINT,
            status_yiwu VARCHAR(255),
            date_yiwu VARCHAR(50),
            status_dushanbe VARCHAR(255),
            date_dushanbe VARCHAR(50),
            status_delivered VARCHAR(255),
            date_delivered VARCHAR(50),
            notification_sent BOOLEAN DEFAULT FALSE,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """,
        "CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);"
    ]
    try:
        with conn.cursor() as cur:
            for q in queries: cur.execute(q)
            conn.commit()
    finally:
        release_db(conn)

# --- 3. Синхронные функции (ядро) ---

def _upsert_user_sync(user_id, full_name, phone, address, username, lang='ru'):
    conn = get_db()
    if not conn: return False
    try:
        with conn.cursor() as cur:
            query = """
                INSERT INTO users (user_id, username, full_name, phone_number, address, language_code)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET
                    username = EXCLUDED.username,
                    full_name = EXCLUDED.full_name,
                    phone_number = EXCLUDED.phone_number,
                    address = EXCLUDED.address,
                    language_code = EXCLUDED.language_code;
            """
            cur.execute(query, (user_id, username, full_name, phone, address, lang))
            conn.commit()
            return True
    except Exception:
        conn.rollback()
        return False
    finally:
        release_db(conn)

def _get_user_sync(user_id):
    conn = get_db()
    if not conn: return None
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            return cur.fetchone()
    finally:
        release_db(conn)

def _update_field_sync(user_id, field, value):
    conn = get_db()
    if not conn: return False
    try:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE users SET {field} = %s WHERE user_id = %s", (value, user_id))
            conn.commit()
            return True
    except:
        conn.rollback()
        return False
    finally:
        release_db(conn)

def _get_all_user_ids_sync():
    conn = get_db()
    if not conn: return []
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id FROM users")
            return [row[0] for row in cur.fetchall()]
    finally:
        release_db(conn)
        
def _get_all_users_count_sync():
    conn = get_db()
    if not conn: return 0
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM users")
            return cur.fetchone()[0]
    except Exception as e:
        logger.error(f"Error counting users: {e}")
        return 0
    finally:
        release_db(conn)

def _get_user_orders_sync(user_id):
    conn = get_db()
    if not conn: return []
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM orders WHERE user_id = %s ORDER BY updated_at DESC LIMIT 50", (user_id,))
            return cur.fetchall()
    finally:
        release_db(conn)

def _request_delivery_multiple_sync(track_codes, address):
    conn = get_db()
    if not conn: return False
    try:
        with conn.cursor() as cur:
            # Обновляем статус заказа на "Запрошена"
            # Примечание: Адрес юзера обновляется отдельно, тут мы просто метим заказы
            for code in track_codes:
                cur.execute("""
                    UPDATE orders 
                    SET status_delivered = 'Запрошена', date_delivered = NULL 
                    WHERE track_code = %s
                """, (code,))
            conn.commit()
            return True
    except:
        conn.rollback()
        return False
    finally:
        release_db(conn)

def _get_delivery_requests_sync():
    conn = get_db()
    if not conn: return []
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Получаем заказы со статусом 'Запрошена' и данные пользователей
            query = """
                SELECT o.track_code, o.user_id, u.full_name, u.phone_number, u.address
                FROM orders o
                JOIN users u ON o.user_id = u.user_id
                WHERE o.status_delivered = 'Запрошена'
                ORDER BY o.updated_at ASC
            """
            cur.execute(query)
            return cur.fetchall()
    finally:
        release_db(conn)

def _confirm_delivery_sync(track_codes):
    conn = get_db()
    if not conn: return []
    confirmed = []
    try:
        with conn.cursor() as cur:
            now_str = datetime.now().strftime("%d.%m.%Y")
            for code in track_codes:
                cur.execute("""
                    UPDATE orders 
                    SET status_delivered = 'Доставлен', date_delivered = %s 
                    WHERE track_code = %s
                """, (now_str, code))
                confirmed.append(code)
            conn.commit()
            return confirmed
    except:
        conn.rollback()
        return []
    finally:
        release_db(conn)

def _get_delivered_paginated_sync(limit, offset):
    conn = get_db()
    if not conn: return []
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            query = """
                SELECT o.*, u.full_name 
                FROM orders o
                LEFT JOIN users u ON o.user_id = u.user_id
                WHERE o.status_delivered = 'Доставлен'
                ORDER BY o.updated_at DESC
                LIMIT %s OFFSET %s
            """
            cur.execute(query, (limit, offset))
            return cur.fetchall()
    finally:
        release_db(conn)

def _get_delivered_count_sync():
    conn = get_db()
    if not conn: return 0
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM orders WHERE status_delivered = 'Доставлен'")
            return cur.fetchone()[0]
    finally:
        release_db(conn)

def _admin_upsert_order_sync(track_code, status, date_yiwu, date_dushanbe, owner_id):
    conn = get_db()
    if not conn: return False
    try:
        with conn.cursor() as cur:
            # Определяем поля статусов
            s_yiwu, s_dush, s_del = None, None, None
            
            if status.lower() in ['yiwu', 'иу']: s_yiwu = 'Иу'
            elif status.lower() in ['dushanbe', 'душанбе']: s_dush = 'Душанбе'
            elif status.lower() in ['delivered', 'доставлен']: s_del = 'Доставлен'
            else: s_yiwu = status # Фолбек

            query = """
                INSERT INTO orders (track_code, user_id, status_yiwu, date_yiwu, status_dushanbe, date_dushanbe, status_delivered)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (track_code) DO UPDATE SET
                    status_yiwu = COALESCE(EXCLUDED.status_yiwu, orders.status_yiwu),
                    date_yiwu = COALESCE(EXCLUDED.date_yiwu, orders.date_yiwu),
                    status_dushanbe = COALESCE(EXCLUDED.status_dushanbe, orders.status_dushanbe),
                    date_dushanbe = COALESCE(EXCLUDED.date_dushanbe, orders.date_dushanbe),
                    status_delivered = COALESCE(EXCLUDED.status_delivered, orders.status_delivered),
                    updated_at = CURRENT_TIMESTAMP;
            """
            cur.execute(query, (track_code, owner_id, s_yiwu, date_yiwu, s_dush, date_dushanbe, s_del))
            conn.commit()
            return True
    except:
        conn.rollback()
        return False
    finally:
        release_db(conn)

def _upsert_order_from_excel_sync(track_code, status_yiwu, date_yiwu, status_dushanbe, date_dushanbe, status_delivered, date_delivered):
    conn = get_db()
    if not conn: return None
    try:
        with conn.cursor() as cur:
            # Проверяем, был ли заказ привязан
            cur.execute("SELECT user_id FROM orders WHERE track_code = %s", (track_code,))
            res = cur.fetchone()
            was_unlinked = True if res and res[0] else False # Если уже был user_id, значит был привязан

            query = """
                INSERT INTO orders (track_code, status_yiwu, date_yiwu, status_dushanbe, date_dushanbe, status_delivered, date_delivered)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (track_code) DO UPDATE SET
                    status_yiwu = EXCLUDED.status_yiwu,
                    date_yiwu = EXCLUDED.date_yiwu,
                    status_dushanbe = EXCLUDED.status_dushanbe,
                    date_dushanbe = EXCLUDED.date_dushanbe,
                    status_delivered = EXCLUDED.status_delivered,
                    date_delivered = EXCLUDED.date_delivered,
                    updated_at = CURRENT_TIMESTAMP
            """
            cur.execute(query, (track_code, status_yiwu, date_yiwu, status_dushanbe, date_dushanbe, status_delivered, date_delivered))
            
            # Проверяем привязку после вставки (если она произошла автоматически где-то еще, но у нас логика привязки отдельная)
            conn.commit()
            return {'was_unlinked': False} 
    except Exception as e:
        conn.rollback()
        return None
    finally:
        release_db(conn)

def _link_order_to_user_sync(track_code, user_id):
    conn = get_db()
    if not conn: return False
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE orders SET user_id = %s WHERE track_code = %s", (user_id, track_code))
            conn.commit()
            return cur.rowcount > 0
    except:
        conn.rollback()
        return False
    finally:
        release_db(conn)

def _get_dushanbe_notifications_sync():
    conn = get_db()
    if not conn: return []
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Ищем заказы:
            # 1. Статус содержит "Душанбе"
            # 2. Есть привязанный юзер (user_id IS NOT NULL)
            # 3. Уведомление еще не отправлено (notification_sent IS FALSE)
            query = """
                SELECT o.track_code, o.user_id, u.language_code 
                FROM orders o
                JOIN users u ON o.user_id = u.user_id
                WHERE (o.status_dushanbe ILIKE '%душанбе%' OR o.status_dushanbe ILIKE '%dushanbe%')
                AND o.notification_sent IS FALSE
            """
            cur.execute(query)
            return cur.fetchall()
    finally:
        release_db(conn)

def _set_notification_sent_sync(track_code):
    conn = get_db()
    if not conn: return
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE orders SET notification_sent = TRUE WHERE track_code = %s", (track_code,))
            conn.commit()
    finally:
        release_db(conn)

# --- 4. ASYNC WRAPPERS (Экспорт для handlers.py) ---

async def get_user(user_id):
    return await asyncio.to_thread(_get_user_sync, user_id)

async def register_user(user_id, full_name, phone_number, address, username, language_code):
    return await asyncio.to_thread(_upsert_user_sync, user_id, full_name, phone_number, address, username, language_code)

async def upsert_user(**kwargs): # Алиас для совместимости
    return await asyncio.to_thread(_upsert_user_sync, kwargs.get('user_id'), kwargs.get('full_name'), kwargs.get('phone'), kwargs.get('address'), kwargs.get('username'), kwargs.get('lang'))

async def update_user_lang(user_id, lang):
    return await asyncio.to_thread(_update_field_sync, user_id, 'language_code', lang)

async def update_user_address(user_id, address):
    return await asyncio.to_thread(_update_field_sync, user_id, 'address', address)

async def update_user_phone(user_id, phone):
    return await asyncio.to_thread(_update_field_sync, user_id, 'phone_number', phone)

async def get_all_user_ids():
    return await asyncio.to_thread(_get_all_user_ids_sync)

async def get_all_users_count():
    return await asyncio.to_thread(_get_all_users_count_sync)

async def get_user_orders(user_id):
    return await asyncio.to_thread(_get_user_orders_sync, user_id)

async def link_order_to_user(track_code, user_id):
    return await asyncio.to_thread(_link_order_to_user_sync, str(track_code), user_id)

async def request_delivery_multiple(track_codes, address):
    # Обновляем адрес юзера и ставим статус
    return await asyncio.to_thread(_request_delivery_multiple_sync, track_codes, address)

async def get_delivery_requests():
    return await asyncio.to_thread(_get_delivery_requests_sync)

async def confirm_delivery(track_codes):
    return await asyncio.to_thread(_confirm_delivery_sync, track_codes)

async def get_delivered_orders_paginated(page, limit):
    offset = (page - 1) * limit
    return await asyncio.to_thread(_get_delivered_paginated_sync, limit, offset)

async def get_delivered_orders_count():
    return await asyncio.to_thread(_get_delivered_count_sync)

async def mark_order_delivered_by_code(track_code):
    return await asyncio.to_thread(_confirm_delivery_sync, [track_code])

async def admin_upsert_order(track_code, status, date_yiwu, date_dushanbe, owner_id=None):
    return await asyncio.to_thread(_admin_upsert_order_sync, track_code, status, date_yiwu, date_dushanbe, owner_id)

async def get_order_by_track_code(track_code):
    conn = await asyncio.to_thread(get_db)
    if not conn: return None
    try:
        def _q():
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("SELECT * FROM orders WHERE track_code = %s", (str(track_code),))
                return cur.fetchone()
        return await asyncio.to_thread(_q)
    finally:
        await asyncio.to_thread(release_db, conn)

async def upsert_order_from_excel(track_code, status_yiwu, date_yiwu, status_dushanbe, date_dushanbe, status_delivered, date_delivered):
    return await asyncio.to_thread(
        _upsert_order_from_excel_sync,
        str(track_code), status_yiwu, date_yiwu, status_dushanbe, date_dushanbe, status_delivered, date_delivered
    )

# Совместимость с jobs.py
async def get_dushanbe_arrivals_to_notify():
    return await asyncio.to_thread(_get_dushanbe_notifications_sync)

async def set_dushanbe_notification_sent(track_code):
    return await asyncio.to_thread(_set_notification_sent_sync, str(track_code))

# Заглушки
async def get_order(track_code): return await get_order_by_track_code(track_code)
async def request_delivery(track_code, address): return await request_delivery_multiple([track_code], address)
async def get_delivered_orders(): return [] 
async def update_user_profile(**kwargs): pass
async def execute_query(query): pass