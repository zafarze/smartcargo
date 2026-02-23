# -*- coding: utf-8 -*-
# texts.py
# 🗣️ SmartCargo Texts (RU, EN, TG)
# Logic & Structure Preserved

from config import XLSX_FILENAME, PROJECT_NAME, CHANNEL_USERNAME

# Тексты на разных языках
TEXTS = {
    "ru": {
        "welcome": "Привет {name}, Рад что Вы с нами в SmartCargo. Пожалуйста, выберите язык.",
        "welcome_back": "С возвращением в SmartCargo, {name}!",
        "language_selected": "🇷🇺 Язык установлен: Русский",
        "invalid_input": "Пожалуйста, используйте кнопки меню или введите трек-код.",
        "select_action": "Выберите действие:",
        "track_code_prompt": "Введите ваш трек-код:",
        
        # --- СТАТУСЫ ---
        "track_code_found_yiwu": (
            "Ассалому алейкум!\n"
            "✅ Ваш груз с трек-кодом <b>{code}</b> принят на складе SmartCargo в г. Иу.\n"
            "🗓️ <b>Дата приёма:</b> {date}\n"
            "⏳ Срок доставки: 15-25 дней. Постараемся доставить Ваш груз раньше срока.\n\n"
            "✨ SmartCargo! Надежное, быстрое карго по доступной цене."
        ),

        "track_code_found_dushanbe": (
            "Ассалому алейкум!\n"
            "🚚 Ваш груз с трек-кодом <b>{code}</b> прибыл на склад SmartCargo в г. Душанбе!\n"
            "🗓️ <b>Дата прибытия:</b> {date}\n\n"
            "📞 Пожалуйста, свяжитесь с нами для получения груза.\n\n"
            "✨ SmartCargo! Надежное, быстрое карго по доступной цене."
        ),
        "track_code_not_found": "❌ Ваш груз пока не поступил на склад SmartCargo в г. Иу.",
        "track_code_found_other": (
            "ℹ️ Статус вашего заказа <b>{code}</b>:\n"
            "<b>{status}</b>"
        ),
        
        # --- СИСТЕМНЫЕ СООБЩЕНИЯ ---
        "track_codes_not_loaded": "⚠️ Проблема с загрузкой трек-кодов. Обратитесь к администратору.",
        "file_received": "Файл получен. Обрабатываю...",
        "file_wrong_name": f"⚠️ Пожалуйста, отправьте файл с точным именем: {XLSX_FILENAME}",
        "file_upload_forbidden": "⛔ У вас нет прав на загрузку файла.",
        "file_upload_success": f"✅ Файл {XLSX_FILENAME} успешно обновлен!\nЗагружено трек-кодов: {{count}}.",
        "file_download_error": "❌ Не удалось скачать или обработать файл.",
        "job_reload_success": "Автоматическое обновление трек-кодов из файла {filename} прошло успешно. Загружено кодов: {count}.",
        "job_reload_fail": "⚠️ Ошибка при автоматическом обновлении трек-кодов из файла {filename}. Проверьте логи бота или сам файл.",
        "admin_notify_initial_load_fail": f"⚠️ КРИТИЧЕСКАЯ ОШИБКА: Не удалось загрузить трек-кодов из {XLSX_FILENAME} при запуске бота!",
        "admin_notify_photo_not_found": "⚠️ Ошибка: Не найден файл фото '{photo_path}' при попытке отправки.",
        
        "dushanbe_arrival_notification": (
            "🚚 Уважаемый клиент!\n"
            "Ваш груз с трек-кодом '{code}' прибыл на склад SmartCargo в г. Душанбе!\n"
            "📞 Пожалуйста, свяжитесь с нами для получения груза."
        ),

        # --- ИНФОРМАЦИЯ ---
        "contacts": (
            "📞 <b>SmartCargo Контакты</b>\n"
            "🇹🇯 Душанбе: +992 20 761 6767\n"
            "🇨🇳 Китай: +86 172 8051 0553\n\n"
            "Режим работы: с 9:00 до 18:00\n"
            "Перерыв: с 12:45 до 14:00\n\n"
            f"✈️ Канал: {CHANNEL_USERNAME}\n"
            "📷 Инстаграм: <a href='https://www.instagram.com/_smart_cargo'>_smart_cargo</a>"
        ),
        "prices_text": (
            "📊 <b>Тариф SmartCargo:</b>\n\n"
            "🔹 <b>от 1 до 20 кг</b> = 2.8$\n"
            "🔹 <b>от 20 до 50 кг</b> = 2.5$\n"
            "🔹 <b>свыше 50 кг</b> = По договоренности\n\n"
            "📦 Объёмный груз (куб) - 250$\n"
            "⏳ Срок доставки 15-25 дней\n\n"
            "Крупногабаритные грузы рассчитываются как куб!!!"
        ),
        "forbidden_text": (
            "<b>Запрещённые товары:</b>\n"
            "1. Лекарства (порошок, таблетки, жидкие препараты)\n"
            "2. Все виды жидкостей (парфюм, ароматизаторы и т.д.)\n"
            "3. Все виды холодного оружия (ножи, электрошокеры, дубинки и т.д.)\n"
            "4. Электронные сигареты, кальяны и т.д. — не принимаются."
        ),
        "address_text": "Выберите адрес:",
        "button_china": "🏭 Адрес в Китае",
        "button_tajikistan": "🇹🇯 Адрес в Таджикистане",
        "address_caption_china": (
            "🏭 <b>Адрес SmartCargo в Китае:</b>\n\n"
            "收货人: (Ваше Имя) (номер телефона)\n"
            "手机号: 172 8051 0553\n"
            "Адрес склада: 浙江省金华市义乌市福田街道口岸路陶界岭小区105栋一楼店面56-21店面"
        ),
        "address_caption_tajikistan": (
            "📍 <b>Наш адрес в Душанбе:</b>\n"
            "ул. Саъди Шерози 22/1\n\n"
            "🗺 <a href='https://maps.google.com/?q=38.557575,68.764847'>Открыть на карте (Google Maps)</a>\n\n"
            "📞 Телефон: +992 20 761 6767"
        ),
        "image_received": "Изображение получено. Пока я не обрабатываю изображения, но могу помочь с чем-то другим! 😊",
        "error": "Произошла ошибка. Попробуйте снова или начните с /start.",
        
        "photo_address_error": "Не удалось отправить фото адреса. Вот адрес:\n{address}",
        "photo_contact_error": "Не удалось отправить фото контактов. Вот контакты:\n{contacts}",
        "photo_price_error": "Не удалось отправить фото тарифов. Вот тарифы:\n{price_list}",
        
        "stats_forbidden": "⛔ Эта команда доступна только администраторам.",
        "stats_message": "📊 Статистика SmartCargo:\nВсего уникальных пользователей: {count}",
        
        "admin_broadcast_prompt": "Введите сообщение для рассылки всем пользователям. Для отмены введите /cancel.",
        "admin_broadcast_confirm_prompt": "Вы уверены, что хотите отправить это сообщение? (Да, отправить / Нет, отменить)\n\n{message}",
        "admin_broadcast_cancelled": "Рассылка отменена.",
        "admin_broadcast_report": "✅ Рассылка завершена.\nУспешно отправлено: {success}\nНе удалось: {failed}",
        
        "help_message": (
            "👋 Здравствуйте! Я бот SmartCargo.\n\n"
            "Используйте кнопки ниже для навигации:\n"
            "🔍 <b>Отследить трек-код:</b> Проверить статус вашего груза.\n"
            "📞 <b>Контакты:</b> Посмотреть наши контакты и режим работы.\n"
            "📊 <b>Тарифы:</b> Узнать актуальные цены на доставку.\n"
            "❌ <b>Запрещённые грузы:</b> Список товаров, которые мы не перевозим.\n"
            "📍 <b>Адрес доставки:</b> Наши адреса в Китае и Таджикистане.\n"
            "🌐 <b>Сменить язык:</b> Выбрать другой язык интерфейса.\n\n"
            "Для начала работы или сброса диалога используйте команду /start."
        ),
        
        # --- БЛОК ДЛЯ ПОДПИСКИ ---
        "subscribe_prompt": f"Чтобы продолжить, пожалуйста, подпишитесь на наш канал: {CHANNEL_USERNAME}",
        "subscribe_button_channel": "SmartCargo Channel",
        "subscribe_button_check": "Я подписался ✅",
        "checking_button": "Проверка...",
        "subscribe_fail": "Вы не подписаны. Пожалуйста, подпишитесь и нажмите 'Проверить'.",
        "subscription_success": "Спасибо за подписку! ✅",
        
        # --- БЛОК ДЛЯ РЕГИСТРАЦИИ ---
        "registration_start": "Спасибо за подписку! ✅\n\nДавайте начнем регистрацию.",
        "registration_prompt_name": "Пожалуйста, отправьте ваше ФИО (например: Иванов Иван Иванович):",
        "registration_invalid_name": "❌ Неверный формат ФИО. Пожалуйста, введите хотя бы два слова (Имя и Фамилию).",
        "registration_prompt_phone": "Отлично, {full_name}.\nТеперь, пожалуйста, поделитесь вашим номером телефона, нажав на кнопку ниже, или введите его вручную в формате <code>+992XXXXXXXXX</code>:",
        "registration_invalid_phone": "❌ Неверный формат телефона. Номер должен быть в формате <code>+992XXXXXXXXX</code>.",
        "registration_prompt_address": "Спасибо.\nНаконец, введите ваш адрес доставки (например: г. Душанбе, ул. Рудаки 15, кв 5).\n\nЭтот адрес будет использоваться для оформления доставки.",
        "registration_complete": "🎉 Регистрация завершена! Добро пожаловать в SmartCargo, {full_name}!",
        "registration_error": "⚠️ Произошла ошибка во время регистрации. Попробуйте /start снова.",
        "registration_required": "Похоже, вы не зарегистрированы. Давайте начнем с /start.",
        "send_contact_button": "📱 Поделиться номером",
        "cancel_button": "Отмена",
        "admin_notify_new_user": (
            "👤 <b>Новый пользователь SmartCargo!</b>\n\n"
            "<b>ФИО:</b> {full_name}\n"
            "<b>Телефон:</b> {phone}\n"
            "<b>Адрес:</b> {address}\n"
            "<b>ID:</b> <code>{user_id}</code>\n"
            "<b>Username:</b> {username}"
        ),
    
        # --- БЛОК ЛИЧНОГО КАБИНЕТА ---
        "lk_welcome": "Вы в Личном кабинете, {name}. Выберите действие:",
        "lk_welcome_back": "Вы в Личном кабинете. Выберите действие:",
        
        "lk_menu_buttons": [
            ["📋 Мои заказы", "🏠 Мой профиль"],
            ["🚚 Заказать доставку"],
            ["⬅️ Назад"]
        ],
        
        'lk_admin_menu_buttons': [
            ["🚚 Оформление на доставку", "📦 Полученные товары"],
            ["📊 Статистика", "📣 Рассылка"],
            ["💾 Скачать Excel", "🏠 Мой профиль"],
            ["⬅️ Назад"]
        ],
        
        # Профиль
        "profile_info": (
            "<b>Ваш профиль:</b>\n\n"
            "<b>ФИО:</b> {full_name}\n"
            "<b>Телефон:</b> {phone_number}\n"
            "<b>Адрес:</b> {address}"
        ),
        "profile_address_not_set": "Не указан",
        "profile_button_edit_phone": "✏️ Изменить телефон",
        "profile_button_edit_address": "✏️ Изменить адрес",
        
        # Редактирование
        "lk_edit_address_prompt": "Ваш текущий адрес: <i>{address}</i>\n\nПожалуйста, введите ваш новый адрес:",
        "lk_edit_address_success": "✅ Ваш адрес успешно обновлен!",
        "lk_edit_phone_prompt": "Ваш текущий телефон: <i>{phone}</i>\n\nПожалуйста, введите ваш новый телефон (в формате <code>+992XXXXXXXXX</code>):",
        "lk_edit_phone_success": "✅ Ваш телефон успешно обновлен!",
        "lk_edit_error": "⚠️ Произошла ошибка. Попробуйте позже.",

        # Заказы
        "lk_orders_title": "<b>Ваши привязанные заказы</b>",
        "lk_no_orders": "У вас пока нет привязанных заказов. \n\nКак только вы проверите свой трек-код через '🔍 Отследить трек-код', он появится здесь.",
        "lk_order_item": "📦 <b>{code}</b> - {status} (от {date})\n",
        
        "status_yiwu": "В Иу",
        "status_dushanbe": "В Душанбе",
        "status_deliveryrequested": "Ожидает доставки",
        "status_delivered": "Доставлен",
        
        # Доставка (для клиента)
        "lk_delivery_select_order": "🚚 <b>Заказ доставки</b>\n\nВыберите заказ, который прибыл в Душанбе, для оформления доставки:",
        "lk_delivery_select_all_orders": (
            "🚚 <b>Заказ доставки</b>\n\n"
            "Найдены следующие заказы, готовые к доставке:\n"
            "{codes}\n\n"
            "Хотите заказать доставку для <b>всех</b> этих заказов?"
        ),
        "lk_delivery_button_all": "✅ Да, заказать доставку (Всего: {count} шт.)",
        "order_delivery_prompt_all": "Выбраны <b>все</b> заказы, готовые к доставке.\nКуда доставить?",
        "lk_delivery_no_orders": "У вас нет заказов, готовых к доставке (со статусом 'Душанбе').",
        "order_delivery_prompt": "Выбран заказ <b>{track_code}</b>.\nКуда доставить?",
        "order_delivery_button_use_saved": "📍 Использовать мой адрес: {address}",
        "order_delivery_button_new": "✏️ Ввести новый адрес",
        "order_delivery_prompt_new": "Пожалуйста, введите адрес доставки для этого заказа:",
        "order_delivery_request_sent": "✅ Ваша заявка принята. Ваш товар будет доставлен в течение 48-часов. Ожидайте звонка курьера.",
        "admin_notify_delivery_request": (
            "✅ Новая заявка на доставку!\n\n"
            "Клиент: {full_name} ({username})\n"
            "Телефон:{phone_number}\n"
            "Трек-код(ы):{track_codes}\n"
            "Адрес: {address}"
        ),
        
        # Привязка
        "order_link_success": "✅ Заказ успешно привязан к вашему профилю!",
        "order_link_fail": "⚠️ Не удалось привязать заказ. Возможно, он уже привязан к другому пользователю.",

        # --- АДМИН БЛОК ---
        "admin_delivery_requests_title": "<b>🚚 Новые заявки на доставку:</b>",
        "admin_delivery_requests_empty": "Новых заявок на доставку нет.",
        "admin_delivery_requests_item": (
            "\n<b>Клиент:</b> {full_name} (<code>{user_id}</code>)\n"
            "<b>Телефон:</b> <code>{phone_number}</code>\n"
            "<b>Адрес:</b> {address}\n"
            "<b>Заказы:</b> {track_codes}\n"
        ),
        "admin_delivery_button_confirm": "✅ Выдано (Клиент: {user_id})",
        "admin_delivery_confirm_success": "✅ Заявка для {full_name} (коды: {track_codes}) отмечена как 'Доставлено'.",
        "admin_delivery_confirm_fail": "❌ Не удалось обработать заявку.",
        
        "admin_delivered_list_title": "<b>📦 Недавно выданные товары:</b>",
        "admin_delivered_list_empty": "Пока нет недавно выданных товаров.",
        "admin_delivered_item": "✅ <b>{code}</b> - {full_name} (от {date})\n",
        
        "user_notify_delivered_title": "🎉 Заказ получен!",
        "user_notify_delivered_body": (
            "Ваши заказы были отмечены как <b>полученные</b>:\n"
            "{track_codes}\n\n"
            "Спасибо, что выбрали нас!"
        ),
        
        'main_buttons': [
            ["🔍 Отследить трек-код", "👤 Личный кабинет"],
            ["📞 Контакты", "📊 Тарифы"],
            ["❌ Запрещённые грузы", "📍 Адрес склада"],
            ["🌐 Сменить язык"]
        ],
    },
    
    # =================================================================
    # --- АНГЛИЙСКИЙ ЯЗЫК (EN) ---
    # =================================================================
    
    "en": {
        "welcome": "Hi {name}, glad to have you with us at SmartCargo. Please select a language.",
        "welcome_back": "Welcome back to SmartCargo, {name}!",
        "language_selected": "🇬🇧 Language set: English",
        "invalid_input": "Please use the menu buttons or enter a track code.",
        "select_action": "Select an action:",
        "track_code_prompt": "Enter your track code:",
        
        "track_code_found_yiwu": (
            "Assalomu alaykum!\n"
            "✅ Your cargo with track code <b>{code}</b> has been received at the SmartCargo warehouse in Yiwu city.\n"
            "🗓️ <b>Date of acceptance:</b> {date}\n"
            "⏳ Delivery time: 15-25 days. We will try to deliver your cargo ahead of schedule.\n\n"
            "✨ SmartCargo! Reliable, fast cargo at an affordable price."
        ),

        "track_code_found_dushanbe": (
            "Assalomu alaykum!\n"
            "🚚 Your cargo with track code <b>{code}</b> has arrived at the SmartCargo warehouse in Dushanbe!\n"
            "🗓️ <b>Date of arrival:</b> {date}\n\n"
            "📞 Please contact us to pick up your cargo.\n\n"
            "✨ SmartCargo! Reliable, fast cargo at an affordable price."
        ),
        "track_code_not_found": "❌ Your cargo has not yet arrived at the SmartCargo warehouse in Yiwu.",
        "track_code_found_other": (
            "ℹ️ Status of your order <b>{code}</b>:\n"
            "<b>{status}</b>"
        ),

        "track_codes_not_loaded": "⚠️ Problem loading track codes. Contact administrator.",
        "file_received": "File received. Processing...",
        "file_wrong_name": f"⚠️ Please send a file with the exact name: {XLSX_FILENAME}",
        "file_upload_forbidden": "⛔ You do not have permission to upload files.",
        "file_upload_success": f"✅ File {XLSX_FILENAME} updated successfully!\nLoaded track codes: {{count}}.",
        "file_download_error": "❌ Failed to download or process the file.",
        "job_reload_success": "Automatic reload of track codes from {filename} successful. Loaded codes: {count}.",
        "job_reload_fail": "⚠️ Error during automatic reload of track codes from {filename}. Check bot logs or the file itself.",
        "admin_notify_initial_load_fail": f"⚠️ CRITICAL ERROR: Failed to load track codes from {XLSX_FILENAME} on bot startup!",
        "admin_notify_photo_not_found": "⚠️ Error: Photo file '{photo_path}' not found when attempting to send.",
        
        "dushanbe_arrival_notification": (
            "🚚 Dear Customer!\n"
            "Your cargo with track code '{code}' has arrived at the SmartCargo warehouse in Dushanbe!\n"
            "📞 Please contact us to pick up your cargo."
        ),
        "contacts": (
            "📞 <b>SmartCargo Contacts</b>\n"
            "🇹🇯 Dushanbe: +992 20 761 6767\n"
            "🇨🇳 China: +86 172 8051 0553\n\n"
            "Working hours: 9:00 to 18:00\n"
            "Break: 12:45 to 14:00\n\n"
            f"✈️ Channel: {CHANNEL_USERNAME}\n"
            "📷 Instagram: <a href='https://instagram.com/_smart_cargo'>_smart_cargo</a>"
        ),
        "prices_text": (
            "📊 <b>SmartCargo Tariff:</b>\n\n"
            "🔹 <b>1 to 20 kg</b> = 2.8$\n"
            "🔹 <b>20 to 50 kg</b> = 2.5$\n"
            "🔹 <b>50+ kg</b> = Negotiable\n\n"
            "📦 Cubic meter - 250$\n"
            "⏳ Delivery time 15-25 days\n\n"
            "Oversized cargo is calculated as cube!!!"
        ),
        "forbidden_text": (
            "<b>Prohibited Items:</b>\n"
            "1. Medicines (powder, tablets, liquid drugs)\n"
            "2. All types of liquids (perfume, air fresheners, etc.)\n"
            "3. All types of cold weapons (knives, stun guns, batons, etc.)\n"
            "4. Electronic cigarettes, hookahs, etc. — not accepted."
        ),
        "address_text": "Select address:",
        "button_china": "🏭 Address in China",
        "button_tajikistan": "🇹🇯 Address in Tajikistan",
        "address_caption_china": (
            "🏭 <b>Address in China:</b>\n\n"
            "收货人: (Your Name) (phone number)\n"
            "手机号: 172 8051 0553\n"
            "Address: 浙江省金华市义乌市福田街道口岸路陶界岭小区105栋一楼店面56-21店面"
        ),
        "address_caption_tajikistan": (
            "📍 <b>Our address in Dushanbe:</b>\n"
            "Sa'di Sherozi 22/1\n\n"
            "🗺 <a href='https://maps.google.com/?q=38.557575,68.764847'>Open in Google Maps</a>\n\n"
            "📞 Phone: +992 20 761 6767"
        ),
        "image_received": "Image received. I can't process images yet, but I can help with something else! 😊",
        "error": "An error occurred. Please try again or start with /start.",
        
        "photo_address_error": "Could not send the address photo. Here is the address:\n{address}",
        "photo_contact_error": "Could not send the contacts photo. Here are the contacts:\n{contacts}",
        "photo_price_error": "Could not send the price list photo. Here is the price list:\n{price_list}",
        
        "stats_forbidden": "⛔ This command is only available to administrators.",
        "stats_message": "📊 Bot Statistics:\nTotal unique users: {count}",
        
        "admin_broadcast_prompt": "Enter message for broadcast. To cancel, type /cancel.",
        "admin_broadcast_confirm_prompt": "Are you sure you want to send this message? (Yes, send / No, cancel)\n\n{message}",
        "admin_broadcast_cancelled": "Broadcast cancelled.",
        "admin_broadcast_report": "✅ Broadcast finished.\nSent successfully: {success}\nFailed: {failed}",
        
        "help_message": (
            "👋 Hello! I am SmartCargo Bot.\n\n"
            "Use the buttons below to navigate:\n"
            "🔍 <b>Track code:</b> Check the status of your cargo.\n"
            "📞 <b>Contacts:</b> View our contact details and working hours.\n"
            "📊 <b>Price list:</b> Find out the current shipping rates.\n"
            "❌ <b>Banned cargo:</b> List of items prohibited for shipping.\n"
            "📍 <b>Delivery address:</b> Our addresses in China and Tajikistan.\n"
            "🌐 <b>Change language:</b> Select a different interface language.\n\n"
            "Use the /start command to begin or reset the conversation."
        ),
        
        # --- SUBSCRIPTION BLOCK ---
        "subscribe_prompt": f"To continue, please subscribe to our channel: {CHANNEL_USERNAME}",
        "subscribe_button_channel": "SmartCargo Channel",
        "subscribe_button_check": "I subscribed ✅",
        "checking_button": "Checking...",
        "subscribe_fail": "You are not subscribed. Please subscribe and press 'Check'.",
        "subscription_success": "Thank you for subscribing! ✅",
        
        # --- REGISTRATION BLOCK ---
        "registration_start": "Thank you for subscribing! ✅\n\nLet's start registration.",
        "registration_prompt_name": "Please send your Full Name (e.g., John Smith):",
        "registration_invalid_name": "❌ Invalid name format. Please enter at least two words (First and Last Name).",
        "registration_prompt_phone": "Great, {full_name}.\nNow, please share your phone number by pressing the button below, or enter it manually in format <code>+992XXXXXXXXX</code>:",
        "registration_invalid_phone": "❌ Invalid phone format. The number must be in <code>+992XXXXXXXXX</code> format.",
        "registration_prompt_address": "Thank you.\nFinally, please enter your delivery address (e.g., Dushanbe, Rudaki 15, apt 5).\n\nThis address will be used for delivery requests.",
        "registration_complete": "🎉 Registration complete! Welcome, {full_name}!",
        "registration_error": "⚠️ An error occurred during registration. Please try /start again.",
        "registration_required": "It seems you are not registered. Let's start with /start.",
        "send_contact_button": "📱 Share Phone Number",
        "cancel_button": "Cancel",
        "admin_notify_new_user": (
            "👤 <b>New user!</b>\n\n"
            "Full Name: {full_name}\n"
            "Phone: <b>{phone}</b>\n"
            "Address: <b>{address}</b>\n"
            "ID: <b>{user_id}</b>\n"
            "Username: <b>{username}</b>"
        ),
        # --- END OF BLOCK ---

        # --- PERSONAL CABINET BLOCK ---
        "lk_welcome": "You are in your Personal Cabinet, {name}. Choose an action:",
        "lk_welcome_back": "You are in your Personal Cabinet. Choose an action:",

        "lk_menu_buttons": [
            ["📋 My Orders", "🏠 My Profile"],
            ["🚚 Request Delivery"],
            ["⬅️ Back"]
        ],
        
        'lk_admin_menu_buttons': [
            ["🚚 Delivery Requests", "📦 Received Goods"],
            ["📊 Statistics", "📣 Broadcast"],
            ["💾 Download Excel", "🏠 My Profile"],
            ["⬅️ Back"]
        ],
            
        # Profile
        "profile_info": (
            "<b>Your Profile:</b>\n\n"
            "<b>Full Name:</b> {full_name}\n"
            "<b>Phone:</b> {phone_number}\n"
            "<b>Address:</b> {address}"
        ),
        "profile_address_not_set": "Not set",
        "profile_button_edit_phone": "✏️ Edit Phone",
        "profile_button_edit_address": "✏️ Edit Address",
        
        # Editing
        "lk_edit_address_prompt": "Your current address: <i>{address}</i>\n\nPlease enter your new address:",
        "lk_edit_address_success": "✅ Your address has been updated!",
        "lk_edit_phone_prompt": "Your current phone: <i>{phone}</i>\n\nPlease enter your new phone (in format <code>+992XXXXXXXXX</code>):",
        "lk_edit_phone_success": "✅ Your phone has been updated!",
        "lk_edit_error": "⚠️ An error occurred. Please try again later.",

        # Orders
        "lk_orders_title": "<b>Your Linked Orders</b>",
        "lk_no_orders": "You have no linked orders yet.\n\nOnce you check your track code via '🔍 Track code', it will appear here.",
        "lk_order_item": "📦 <b>{code}</b> - {status} (from {date})\n",
        
        "status_yiwu": "In Yiwu",
        "status_dushanbe": "In Dushanbe",
        "status_deliveryrequested": "Pending Delivery",
        "status_delivered": "Delivered",
        
        # Delivery (for client)
        "lk_delivery_select_order": "🚚 <b>Request Delivery</b>\n\nPlease select an order that has arrived in Dushanbe:",
        "lk_delivery_no_orders": "You have no orders ready for delivery (with 'Dushanbe' status).",
        "order_delivery_prompt": "Selected order <b>{track_code}</b>.\nWhere to deliver?",
        "order_delivery_button_use_saved": "📍 Use my address: {address}",
        "order_delivery_button_new": "✏️ Enter new address",
        "order_delivery_prompt_new": "Please enter the delivery address for this order:",
        "order_delivery_request_sent": "✅ Your request is accepted. Your item will be delivered within 48 hours. Expect a call from the courier.",
        "admin_notify_delivery_request": (
            "✅ New delivery request!*\n\n"
            "Customer: {full_name} ({username})\n"
            "Phone: {phone_number}\n"
            "Track code: <b>{track_code}</b>\n"
            "Address: {address}"
        ),
        
        # Linking
        "order_link_success": "✅ Order successfully linked to your profile!",
        "order_link_fail": "⚠️ Failed to link order. It might already be linked to another user.",
        
        # --- ADMIN BLOCK ---
        "admin_delivery_requests_title": "<b>🚚 New Delivery Requests:</b>",
        "admin_delivery_requests_empty": "No new delivery requests.",
        "admin_delivery_requests_item": (
            "\n<b>Client:</b> {full_name} (<code>{user_id}</code>)\n"
            "<b>Phone:</b> <code>{phone_number}</code>\n"
            "<b>Address:</b> {address}\n"
            "<b>Orders:</b> {track_codes}\n"
        ),
        "admin_delivery_button_confirm": "✅ Delivered (Client: {user_id})",
        "admin_delivery_confirm_success": "✅ Request for {full_name} (codes: {track_codes}) marked as 'Delivered'.",
        "admin_delivery_confirm_fail": "❌ Failed to process request.",
        
        "admin_delivered_list_title": "<b>📦 Recently Delivered Goods:</b>",
        "admin_delivered_list_empty": "No recently delivered goods.",
        "admin_delivered_item": "✅ <b>{code}</b> - {full_name} (on {date})\n",
        
        "user_notify_delivered_title": "🎉 Order Received!",
        "user_notify_delivered_body": (
            "Your orders have been marked as <b>received</b>:\n"
            "{track_codes}\n\n"
            "Thank you for choosing us!"
        ),

        'main_buttons': [
            ["🔍 Track Code", "👤 Personal Cabinet"],
            ["📞 Contacts", "📊 Rates"],
            ["❌ Forbidden Goods", "📍 Warehouse Address"],
            ["🌐 Change Language"]
        ],
    },
    
    # =================================================================
    # --- ТАДЖИКСКИЙ ЯЗЫК (TG) ---
    # =================================================================
    
    "tg": {
        "welcome": "Салом {name}, хуш омадед ба SmartCargo. Лутфан забонро интихоб кунед.",
        "welcome_back": "Хуш омадед ба SmartCargo, {name}!",
        "language_selected": "🇹🇯 Забон интихоб шуд: Тоҷикӣ",
        "invalid_input": "Лутфан тугмаҳои менюро истифода баред ё рақами пайгирӣ ворид кунед.",
        "select_action": "Амалро интихоб кунед:",
        "track_code_prompt": "Рақами пайгириро ворид кунед:",
        
        "track_code_found_yiwu": (
            "Ассалому алайкум!\n"
            "✅ Бори шумо бо трек-коди <b>{code}</b> дар анбори SmartCargo дар ш. Иву қабул карда шуд.\n"
            "🗓️ <b>Санаи қабул:</b> {date}\n"
            "⏳ Мӯҳлати тахминии расонидан: 15-25 рӯз. Мо кӯшиш мекунем, ки бори Шуморо пеш аз мӯҳлат расонем.\n\n"
            "✨ SmartCargo! Каргои боэтимод, зуд ва бо нархи дастрас."
        ),

        "track_code_found_dushanbe": (
            "Ассалому алайкум!\n"
            "🚚 Бори шумо бо трек-коди <b>{code}</b> ба анбори SmartCargo дар ш. Душанбе расид!\n"
            "🗓️ <b>Санаи расидан:</b> {date}\n\n"
            "📞 Лутфан барои гирифтани бор бо мо тамос гиред.\n\n"
            "✨ SmartCargo! Каргои боэтимод, зуд ва бо нархи дастрас."
        ),
        "track_code_not_found": "❌ Бори Шумо то ҳол дар анбори SmartCargo дар ш. Иву наомадааст.",
        "track_code_found_other": (
            "ℹ️ Ҳолати фармоиши шумо <b>{code}</b>:\n"
            "<b>{status}</b>"
        ),

        "track_codes_not_loaded": "⚠️ Мушкилот дар боркунии рақамҳои пайгирӣ. Ба администратор муроҷиат кунед.",
        "file_received": "Файл қабул шуд. Коркард рафта истодааст...",
        "file_wrong_name": f"⚠️ Лутфан, файлро бо номи аниқ ирсол кунед: {XLSX_FILENAME}",
        "file_upload_forbidden": "⛔ Шумо барои бор кардани файл ҳуқуқ надоред.",
        "file_upload_success": f"✅ Файли {XLSX_FILENAME} бомуваффақият нав карда шуд!\nМиқдори кодҳои боршуда: {{count}}.",
        "file_download_error": "❌ Файлро боргирӣ ё коркард кардан ғайриимкон аст.",
        "job_reload_success": "Навсозии автоматии рақамҳои пайгирӣ аз файли {filename} бомуваффақият гузашт. Миқдори кодҳои боршуда: {count}.",
        "job_reload_fail": "⚠️ Хатогӣ ҳангоми навсозии автоматии рақамҳои пайгирӣ аз файли {filename}. Лутфан, логҳои бот ё худи файлро санҷед.",
        "admin_notify_initial_load_fail": f"⚠️ ХАТОГИИ ҶИДДӢ: Ҳангоми оғози кор бот натавонист рамзҳои пайгириро аз {XLSX_FILENAME} бор кунад!",
        "admin_notify_photo_not_found": "⚠️ Хатогӣ: Файли акси '{photo_path}' ҳангоми кӯшиши фиристодан ёфт нашуд.",
        
        "dushanbe_arrival_notification": (
            "🚚 Мизоҷи муҳтарам!\n"
            "Бори шумо бо трек-коди '{code}' ба анбори SmartCargo дар ш. Душанбе расид!\n"
            "📞 Лутфан барои гирифтани бор бо мо тамос гиред."
        ),
        "contacts": (
            "📞 <b>SmartCargo Тамос</b>\n"
            "🇹🇯 Душанбе: +992 20 761 6767\n"
            "🇨🇳 Хитой: +86 172 8051 0553\n\n"
            "Реҷаи кори: аз 9:00 то 18:00\n"
            "Танаффус: аз 12:45 до 14:00\n\n"
            f"✈️ Канал: {CHANNEL_USERNAME}\n"
            "📷 Инстаграм: <a href='https://www.instagram.com/_smart_cargo'>_smart_cargo</a>"
        ),
        "prices_text": (
            "📊 <b>Тарифи SmartCargo:</b>\n\n"
            "🔹 <b>аз 1 то 20 кг</b> = 2.8$\n"
            "🔹 <b>аз 20 то 50 кг</b> = 2.5$\n"
            "🔹 <b>аз 50 кг боло</b> = Бо маслиҳат\n\n"
            "📦 Ҳаҷм (куб) - 250$\n"
            "⏳ Мӯҳлати расонидан 15-25 рӯз\n\n"
            "Борҳои калонҳаҷм чун куб ҳисоб карда мешаванд!!!"
        ),
        "forbidden_text": (
            "<b>Молҳои манъшуда:</b>\n"
            "1. Доруворӣ (хок, таблетка, доруҳои моеъ)\n"
            "2. Ҳама намудҳои моеъҳо (атриёт, ароматизаторҳо ва ғ.)\n"
            "3. Ҳама намудҳои аслиҳаи сард (корд, электрошокерҳо, чӯбдастҳо ва ғ.)\n"
            "4. Сигаретаҳои электронӣ, кальянҳо ва ғ. қабул намешаванд."
        ),
        "address_text": "Суроғаро интихоб кунед:",
        "button_china": "🏭 Суроға дар Хитой",
        "button_tajikistan": "🇹🇯 Суроға дар Тоҷикистон",
        "address_caption_china": (
            "🏭 <b>Суроға дар Хитой:</b>\n\n"
            "收货人: (Номи Шумо) (рақами телефон)\n"
            "手机号: 172 8051 0553\n"
            "Адрес склада: 浙江省金华市义乌市福田街道口岸路陶界岭小区105栋一楼店面56-21店面"
        ),
        "address_caption_tajikistan": (
            "📍 <b>Суроғаи мо дар Душанбе:</b>\n"
            "кӯч. Саъди Шерози 22/1\n\n"
            "🗺 <a href='https://maps.google.com/?q=38.557575,68.764847'>Дар харита кушоед (Google Maps)</a>\n\n"
            "📞 Телефон: +992 20 761 6767"
        ),
        "image_received": "Тасвир қабул шуд. Ман ҳоло тасвирҳоро коркард намекунам, аммо метавонам бо чизи дигар кӯмак кунам! 😊",
        "error": "Хатогӣ рух дод. Лутфан боз кӯшиш кунед ё аз /start оғоз кунед.",
        
        "photo_address_error": "Сурати суроғаро фиристодан мумкин нест. Ин аст суроға:\n{address}",
        "photo_contact_error": "Сурати тамосҳоро фиристодан мумкин нест. Ин аст тамосҳо:\n{contacts}",
        "photo_price_error": "Сурати нархномаро фиристодан мумкин нест. Ин аст нархнома:\n{price_list}",
        
        "stats_forbidden": "⛔ Ин фармон танҳо барои администраторҳо дастрас аст.",
        "stats_message": "📊 Омори бот:\nШумораи умумии истифодабарандагони нодир: {count}",
        
        "admin_broadcast_prompt": "Паёмро барои фиристодан ворид кунед. Барои бекор кардан /cancel-ро ворид кунед.",
        "admin_broadcast_confirm_prompt": "Оё шумо мутмаин ҳастед, ки ин паёмро ирсол мекунед? (Ҳа, фиристед / Не, бекор кунед)\n\n{message}",
        "admin_broadcast_cancelled": "Ирсол бекор карда шуд.",
        "admin_broadcast_report": "✅ Ирсол анҷом ёфт.\nБомуваффақият фиристода шуд: {success}\nФиристода нашуд: {failed}",
        
        "help_message": (
            "👋 Ассалому алайкум! Ман боти SmartCargo.\n\n"
            "Барои паймоиш тугмаҳои зеринро истифода баред:\n"
            "🔍 <b>Трек-код:</b> Санҷиши ҳолати бори шумо.\n"
            "📞 <b>Тамос:</b> Дидани маълумоти тамос ва реҷаи кории мо.\n"
            "📊 <b>Нархнома:</b> Омӯхтани нархҳои ҷории интиқол.\n"
            "❌ <b>Молҳои манъшуда:</b> Рӯйхати молҳое, ки барои интиқол манъ аст.\n"
            "📍 <b>Тарзи пур кардани адрес:</b> Суроғаҳои мо дар Чин ва Тоҷикистон.\n"
            "🌐 <b>Ивази забон:</b> Интихоби забони дигари интерфейс.\n\n"
            "Барои оғози кор ё аз нав оғоз кардани сӯҳбат фармони /start -ро истифода баред."
        ),
        
        # --- БЛОК ДЛЯ ПОДПИСКИ ---
        "subscribe_prompt": f"Барои идома, лутфан ба канали мо обуна шавед: {CHANNEL_USERNAME}",
        "subscribe_button_channel": "SmartCargo Channel",
        "subscribe_button_check": "Ман обуна шудам ✅",
        "checking_button": "Санҷида мешавад...",
        "subscribe_fail": "Шумо обуна нашудаед. Лутфан обуна шавед ва 'Санҷиш'-ро пахш кунед.",
        "subscription_success": "Ташаккур барои обуна! ✅",
        
        # --- БЛОК ДЛЯ РЕГИСТРАЦИИ ---
        "registration_start": "Ташаккур барои обуна! ✅\n\nБиёед бақайдгириро оғоз кунем.",
        "registration_prompt_name": "Лутфан, Ном ва Насаби худро ворид кунед (Масалан: Каримов Карим):",
        "registration_invalid_name": "❌ Формати ННН нодуруст аст. Лутфан, ҳадди аққал ду калима (Ном ва Насаб) ворид кунед.",
        "registration_prompt_phone": "Хуб, {full_name}.\nАкнун, лутфан рақами телефони худро бо пахши тугмаи поён равон кунед, ё онро дастӣ дар формати <code>+992XXXXXXXXX</code> ворид кунед:",
        "registration_invalid_phone": "❌ Формати телефон нодуруст аст. Рақам бояд дар формати <code>+992XXXXXXXXX</code> бошад.",
        "registration_prompt_address": "Ташаккур.\nДар охир, суроғаи худро барои дастрасӣ ворид кунед (Масалан: ш. Душанбе, кӯч. Рӯдакӣ 15, х 5).\n\nИн суроға барои дархостҳои дастрасӣ истифода мешавад.",
        "registration_complete": "🎉 Бақайдгирӣ анҷом ёфт! Хуш омадед ба SmartCargo, {full_name}!",
        "registration_error": "⚠️ Ҳангоми бақайдгирӣ хатогӣ рух дод. Лутфан /start -ро аз нав оғоз кунед.",
        "registration_required": "Чунин ба назар мерасад, ки шумо ба қайд гирифта нашудаед. Биёед бо /start оғоз кунем.",
        "send_contact_button": "📱 Равон кардани рақам",
        "cancel_button": "Бекор кардан",
        "admin_notify_new_user": (
            "👤 <b>Истифодабарандаи нав!</b>\n\n"
            "ННН: <b>{full_name}</b>\n"
            "Телефон: <b>{phone}</b>\n"
            "Суроға: <b>{address}</b>\n"
            "ID: <b>{user_id}</b>\n"
            "Username: <b>{username}</b>"
        ),
        # --- КОНЕЦ БЛОКА ---

        # --- БЛОКИ КАБИНЕТИ ШАХСӢ ---
        "lk_welcome": "Шумо дар Кабинети шахсӣ, {name}. Амалро интихоб кунед:",
        "lk_welcome_back": "Шумо дар Кабинети шахсӣ. Амалро интихоб кунед:",

        "lk_menu_buttons": [
            ["📋 Фармоишҳои ман", "🏠 Профили ман"],
            ["🚚 Дархости дастрасӣ"],
            ["⬅️ Ба менюи асосӣ"]
        ],
        
        'lk_admin_menu_buttons': [
            ["🚚 Дархостҳои нав", "📦 Молҳои гирифташуда"],
            ["📊 Омор", "📣 Паёмнамо"],
            ["💾 Боргирии Excel", "🏠 Профили ман"],
            ["⬅️ Ба менюи асосӣ"]
        ],
            
        # Профил
        "profile_info": (
            "<b>Профили шумо:</b>\n\n"
            "<b>ННН:</b> {full_name}\n"
            "<b>Телефон:</b> {phone_number}\n"
            "<b>Суроға:</b> {address}"
        ),
        "profile_address_not_set": "Нишон дода нашудааст",
        "profile_button_edit_phone": "✏️ Ивази телефон",
        "profile_button_edit_address": "✏️ Ивази суроға",
        
        # Таҳрир (Редактирование)
        "lk_edit_address_prompt": "Суроғаи ҷории шумо: <i>{address}</i>\n\nЛутфан, суроғаи нави худро ворид кунед:",
        "lk_edit_address_success": "✅ Суроғаи шумо бомуваффақият нав карда шуд!",
        "lk_edit_phone_prompt": "Телефони ҷории шумо: <i>{phone}</i>\n\nЛутфан, телефони нави худро ворид кунед (дар формати <code>+992XXXXXXXXX</code>):",
        "lk_edit_phone_success": "✅ Телефони шумо бомуваффақият нав карда шуд!",
        "lk_edit_error": "⚠️ Хатогӣ рух дод. Лутфан баъдтар кӯшиш кунед.",

        # Фармоишҳо
        "lk_orders_title": "<b>Фармоишҳои шумо</b>",
        "lk_no_orders": "Шумо ҳоло фармоишҳои ба худ алоқаманд надоред.\n\nПас аз санҷиши трек-код тавассути '🔍 Трек-код', он дар ин ҷо пайдо мешавад.",
        "lk_order_item": "📦 <b>{code}</b> - {status} (аз {date})\n",
        
        "status_yiwu": "Дар Иу",
        "status_dushanbe": "Дар Душанбе",
        "status_deliveryrequested": "Интизори расонидан",
        "status_delivered": "Расонида шуд",
        
        # Дастрасӣ (Доставка для клиента)
        "lk_delivery_select_order": "🚚 <b>Дархости дастрасӣ</b>\n\nФармоишеро, ки ба Душанбе расидааст, интихоб кунед:",
        "lk_delivery_no_orders": "Шумо фармоишҳои ба Душанбе расида (бо статуси 'Душанбе') надоред.",
        "order_delivery_prompt": "Фармоиши <b>{track_code}</b> интихоб шуд.\nБа куҷо дастрас кунем?",
        "order_delivery_button_use_saved": "📍 Суроғаи ман: {address}",
        "order_delivery_button_new": "✏️ Ворид кардани суроғаи нав",
        "order_delivery_prompt_new": "Лутфан, суроғаи дастрасиро барои ин фармоиш ворид кунед:",
        "order_delivery_request_sent": "✅ Дархости шумо қабул шуд. Моли шумо дар давоми 48 соат расонида мешавад. Занги моро интизор шавед.",
        "admin_notify_delivery_request": (
            "✅ Дархости нави дастрасӣ!\n\n"
            "Мизоҷ: {full_name} ({username})\n"
            "Телефон: {phone_number}\n"
            "Трек-код: {track_code}\n"
            "Суроға: {address}"
        ),
        
        # Пайвасткунӣ
        "order_link_success": "✅ Фармоиш ба профили шумо бомуваффақият пайваст карда шуд!",
        "order_link_fail": "⚠️ Фармоишро пайваст кардан мумкин нест. Эҳтимол, он аллакай ба корбари дигар пайваст аст.",

        # --- АДМИН БЛОК ---
        "admin_delivery_requests_title": "<b>🚚 Дархостҳои нав барои дастрасӣ:</b>",
        "admin_delivery_requests_empty": "Дархостҳои нав вуҷуд надоранд.",
        "admin_delivery_requests_item": (
            "\n<b>Мизоҷ:</b> {full_name} (<code>{user_id}</code>)\n"
            "<b>Телефон:</b> <code>{phone_number}</code>\n"
            "<b>Суроға:</b> {address}\n"
            "<b>Фармоишҳо:</b> {track_codes}\n"
        ),
        "admin_delivery_button_confirm": "✅ Супорида шуд (Мизоҷ: {user_id})",
        "admin_delivery_confirm_success": "✅ Дархост барои {full_name} (кодҳо: {track_codes}) ҳамчун 'Расонидашуда' қайд карда шуд.",
        "admin_delivery_confirm_fail": "❌ Коркарди дархост номуваффақ шуд.",

        "admin_delivered_list_title": "<b>📦 Молҳои ба наздикӣ супоридашуда:</b>",
        "admin_delivered_list_empty": "Молҳои ба наздикӣ супоридашуда вуҷуд надоранд.",
        "admin_delivered_item": "✅ <b>{code}</b> - {full_name} (санаи {date})\n",
        
        "user_notify_delivered_title": "🎉 Фармоиш гирифта шуд!",
        "user_notify_delivered_body": (
            "Фармоишҳои шумо ҳамчун <b>гирифташуда</b> қайд карда шуданд:\n"
            "{track_codes}\n\n"
            "Ташаккур, ки моро интихоб кардед!"
        ),
        
        'main_buttons': [
            ["🔍 Пайгирии трек-код", "👤 Утоқи шахсӣ"],
            ["📞 Тамосҳо", "📊 Тарофаҳо"],
            ["❌ Молҳои манъшуда", "📍 Суроғаи анбор"],
            ["🌐 Ивази забон"]
        ],
    },
}

def get_text(key, lang='ru'):
    """
    Возвращает текст по ключу для выбранного языка.
    Если на выбранном языке ключа нет, пытается вернуть на русском.
    """
    
    # 1. Пытаемся получить словарь для выбранного языка
    # Если языка нет в словаре (например 'de'), берем 'ru' по умолчанию
    selected_texts = TEXTS.get(lang, TEXTS['ru'])

    # 2. Пытаемся получить значение по ключу
    text = selected_texts.get(key)

    # 3. Если текст найден - возвращаем
    if text:
        return text

    # 4. Fallback: Если текста нет в выбранном языке (например в 'en' забыли ключ),
    # пытаемся найти его в 'ru'
    if lang != 'ru':
        text_ru = TEXTS['ru'].get(key)
        if text_ru:
            return text_ru

    # 5. Если ключа нет даже в русском - возвращаем заглушку, чтобы бот не падал
    return f"!!NO_TEXT_FOR_{key}!!"