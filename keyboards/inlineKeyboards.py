from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

supportkb = InlineKeyboardMarkup(row_width=1)
url_tg = InlineKeyboardButton('@baze1evs', url='https://t.me/Baze1evs')
supportkb.add(url_tg)

active_orders = InlineKeyboardMarkup(row_width=2)
cancel_order = InlineKeyboardButton('Отменить заказ ❌', callback_data='cancel')
update_order = InlineKeyboardButton('Обновить заказ 📝', callback_data='update')
active_orders.add(cancel_order,update_order)

past_orders = InlineKeyboardMarkup(row_width=1)
get_report = InlineKeyboardButton('Получить отчёт 🔍', callback_data='report')
past_orders.add(get_report)