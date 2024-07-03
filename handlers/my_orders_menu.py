from datetime import datetime
from datetime import time
from datetime import timedelta
from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from loader import ts
from loader import bot
from loader import dp
from loader import BASE_URL
from data import *
from states import *
from keyboards import *
from services import *
from utils import my_orders_menu
from utils.profile_menu import *
from utils.my_orders_menu import *
from utils.general import get_client_id
import requests


async def my_orders_menu_handler(message: types.Message):
    global data_list
    client_id = get_client_id(message.from_user.id)
    if message.text == "Прошлые заказы":
        orders_data = requests.post(f"{BASE_URL}/client/orders/get_orders", json={
            "client_id": f'{client_id}'}).json()
        data_list = {f'{client_id}': create_list_of_orders(orders_data['data'], 0, 0)}
        await MainMenuState.start_menu.set()
        if len(data_list[client_id]) > 0:
            await bot.send_message(message.from_user.id, f"Прошлые заказы:\n{generate_new_str_for_order(data_list[client_id])}",
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
        else:
            await bot.send_message(message.from_user.id, txt_my_orders_menu.fool_doesnt_order,
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()

    elif message.text == "Отменить заказ":
        orders_data = requests.post(f"{BASE_URL}/client/orders/get_orders", json={
            "client_id": f'{client_id}'}).json()
        data_list = {f'{client_id}': create_list_of_orders(orders_data['data'], 0, 1)}
        await MyOrdersMenuState.cancel_order.set()
        if len(data_list[client_id]) > 0:
            await bot.send_message(message.from_user.id, f"Активные заказы:\n{generate_new_str_for_order(data_list[client_id])}")
            await bot.send_message(message.from_user.id, txt_my_orders_menu.ask_cancel_order_number, reply_markup=ReplyKeyboardRemove())
        else:
            await bot.send_message(message.from_user.id, txt_my_orders_menu.fool_doesnt_order,
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()

    elif message.text == "Веруться в меню":
        await bot.send_message(message.from_user.id, txt_main_menu.section_main_menu,
                               reply_markup=GeneralKeyboards.group_kb_main_menu)
        await MainMenuState.start_menu.set()


async def cancel_order(message: types.Message):
    global data_list, global_order_to_cancel
    global_order_to_cancel = {}
    data_list_local = data_list[get_client_id(message.from_user.id)]
    if is_integer_string(message.text):
        number = int(message.text)
        if number > 0 and number <= len(data_list_local):
            order_to_cancel = [data_list_local[number-1]]
            global_order_to_cancel[get_client_id(message.from_user.id)] = order_to_cancel[0]
            txt_order = f'{number}.{generate_new_str_for_order(order_to_cancel)[3:]}'
            await bot.send_message(message.from_user.id, f'{txt_my_orders_menu.cancel_order_confirmation[0]}\n{txt_order}')
            await bot.send_message(message.from_user.id, f'{txt_my_orders_menu.cancel_order_confirmation[1]}',
                                   reply_markup=GeneralKeyboards.group_kb_yes_or_no)
            await MyOrdersMenuState.cancel_order_confirm.set()
        else:
            await bot.send_message(message.from_user.id, txt_mistakes.order_number_mistake,
                                   reply_markup=ReplyKeyboardRemove())
            await MyOrdersMenuState.cancel_order.set()
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.order_number_mistake,
                               reply_markup=ReplyKeyboardRemove())
        await MyOrdersMenuState.cancel_order.set()


async def confirmation_cancel_order(message: types.Message):
    global global_order_to_cancel
    old_info = global_order_to_cancel[get_client_id(message.from_user.id)]
    if message.text == "Да":
        requests.post(f'{BASE_URL}/client/orders/update_order_info',
                      json={"order_id": old_info["order_id"], "service_type": old_info["service_type"],
                            "start_date": old_info["start_date"], "start_time": old_info["start_time"],
                            "end_date": old_info["end_date"], "end_time": old_info["end_time"],
                            "service_details": old_info["service_details"], "options": old_info["options"],
                            "region": old_info["region"], "city": old_info["city"],
                            "district": old_info["district"], "street": old_info["street"],
                            "house": old_info["street"], "building": old_info["building"],
                            "apartment": old_info["apartment"], "status": "cancelled"}).json()
        await bot.send_message(message.from_user.id, txt_my_orders_menu.cancel_order_success,
                               reply_markup=GeneralKeyboards.group_kb_my_orders_menu)
        await MyOrdersMenuState.start_orders_menu.set()
    elif message.text == "Нет":
        await bot.send_message(message.from_user.id, txt_my_orders_menu.cancel_order_cancel,
                               reply_markup=GeneralKeyboards.group_kb_my_orders_menu)
        await MyOrdersMenuState.start_orders_menu.set()


# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _
def my_orders_menu_reg(dp=dp):
    # - - - Message handlers - - -
    dp.register_message_handler(my_orders_menu_handler, state=MyOrdersMenuState.start_orders_menu)
    dp.register_message_handler(cancel_order, state=MyOrdersMenuState.cancel_order)
    dp.register_message_handler(confirmation_cancel_order, state=MyOrdersMenuState.cancel_order_confirm)


    # - - - Callback handlers - - -