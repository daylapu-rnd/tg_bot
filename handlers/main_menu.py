from datetime import datetime
from datetime import time
from datetime import timedelta
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import ts
from loader import bot
from loader import dp
from loader import BASE_URL
from data import *
from states import *
from keyboards import *
from services import *
from handlers import profile_menu
from handlers import orders


async def menu_command(message: types.Message):
    """menu comand function"""
    await bot.send_message(message.from_user.id, txt_main_menu.section_main_menu,
                           reply_markup=GeneralKeyboards.group_kb_main_menu)
    await MainMenuState.start_menu.set()


async def main_menu_handler(message: types.Message, state:FSMContext):
    if message.text == "Профиль":
        await bot.send_message(message.from_user.id, "Раздел: Профиль",
                               reply_markup=GeneralKeyboards.group_kb_profile_menu)
        await ProfileMenuState.first_profile_function.set()
        await profile_menu.MyProfileCommandRegisteredFunction(message,state)
    elif message.text == "Мои заказы":
        await bot.send_message(message.from_user.id, txt_main_menu.section_my_orders,
                               reply_markup=GeneralKeyboards.group_kb_orders)
        await MainMenuState.my_orders.set()
        await orders.MyOrdersStart(message,state)
    elif message.text == "Поддержка":
        await bot.send_message(message.from_user.id, txt_main_menu.support, reply_markup=supportkb)
    elif message.text == "О сервисе":
        await bot.send_message(message.from_user.id, txt_main_menu.about)
    elif message.text == "Вернуться в меню":
        pass
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.fool_use_buttons,reply_markup=GeneralKeyboards.group_kb_main_menu)


# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _
def main_menu_reg(dp=dp):
    # - - - Message handlers - - -
    dp.register_message_handler(menu_command, commands='menu', state="*")
    dp.register_message_handler(main_menu_handler, state=MainMenuState.start_menu)


    # - - - Callback handlers - - -