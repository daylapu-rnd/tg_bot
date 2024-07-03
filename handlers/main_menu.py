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


async def menu_command(message: types.Message):
    """menu comand function"""
    await bot.send_message(message.from_user.id, txt_main_menu.section_main_menu,
                           reply_markup=GeneralKeyboards.group_kb_main_menu)
    await MainMenuState.start_menu.set()


async def main_menu_handler(message: types.Message):
    if message.text == "Профиль":
        await bot.send_message(message.from_user.id, "Раздел: Профиль",
                               reply_markup=GeneralKeyboards.group_kb_profile_menu)
        await ProfileMenuState.start_profile_menu.set()
    elif message.text == "Веруться в меню":
        await bot.send_message(message.from_user.id, txt_main_menu.section_main_menu,
                               reply_markup=GeneralKeyboards.group_kb_main_menu)
        await MainMenuState.start_menu.set()


# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _
def main_menu_reg(dp=dp):
    # - - - Message handlers - - -
    dp.register_message_handler(menu_command, commands=["menu"], state="*")
    dp.register_message_handler(main_menu_handler, state=MainMenuState.start_menu)


    # - - - Callback handlers - - -