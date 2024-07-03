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
from utils.profile_menu import *
from utils.registration import is_valid_email, is_valid_phone_number, format_phone_number, is_valid_name
from utils.my_orders_menu import *
from utils.general import get_client_id
import requests


async def my_orders_menu_handler(message: types.Message):
    if message.text == "Прошлые заказы":
        client_id = get_client_id(message.from_user.id)
        orders_data = requests.post(f"{BASE_URL}/client/orders/get_orders", json={
            "client_id": f'{client_id}'}).json()
        data_list = create_list_of_orders(orders_data['data'], 0, 0)
        await MainMenuState.start_menu.set()
        if len(data_list) > 0:
            await bot.send_message(message.from_user.id, f"Прошлые заказы:\n{generate_new_str_for_order(data_list)}",
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
        else:
            await bot.send_message(message.from_user.id, "Вы еще не совершали заказов(((",
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)

    elif message.text == "Веруться в меню":
        await bot.send_message(message.from_user.id, txt_main_menu.section_main_menu,
                               reply_markup=GeneralKeyboards.group_kb_main_menu)
        await MainMenuState.start_menu.set()


# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _
def my_orders_menu_reg(dp=dp):
    # - - - Message handlers - - -
    dp.register_message_handler(my_orders_menu_handler, state=MyOrdersMenuState.start_orders_menu)

    # - - - Callback handlers - - -