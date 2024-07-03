from datetime import datetime
from datetime import time
from datetime import timedelta
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

import services.orders
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
from handlers import main_menu
import requests


async def MyOrdersStart(message: types.Message, state: FSMContext):
    global dataAboutUser
    try:
        clientData = requests.post(
            f"{BASE_URL}/client/profile", json={"tg_id": f'{dataAboutUser[message.from_user.id]["user_tg_id"]}'}).json()["data"]["client_id"]
        ordersData = requests.post(
            f"{BASE_URL}/client/get_orders", json={"client_id": f'{clientData}'}).json()
    except Exception as e:
        log_error(e)

    if ordersData["action"] == "success":
        if message.text == "Прошлые заказы":
            for i in ordersData["data"]:
                if i["status"] == "complete":
                    await bot.send_message(message.from_user.id, services.orders.pretty_print_dict(i), reply_markup=past_orders)
        elif message.text == "Активные заказы":
            for i in ordersData["data"]:
                if i["status"] == "active":
                    await bot.send_message(message.from_user.id, services.orders.pretty_print_dict(i), reply_markup=active_orders)
        elif message.text == "Вернуться в меню":
            await bot.send_message(message.from_user.id, "Раздел: главное меню",reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()
        elif message.text == "Мои заказы":
            pass
        else:
            await bot.send_message(message.from_user.id, txt_mistakes.fool_use_buttons)
    else:
        await bot.send_message(message.from_user.id, txt_reg.mistake)
        ts(1)
        await bot.send_message(message.from_user.id, txt_reg.maintenance,
                               reply_markup=GeneralKeyboards.single_btn_command_start)





def orders_reg(dp=dp):
    # - - - Message handlers - - -
    dp.register_message_handler(MyOrdersStart, state=MainMenuState.my_orders)
