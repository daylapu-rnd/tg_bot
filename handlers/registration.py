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
import requests


async def startCommand(message: types.Message):
    """
    startCommand function
    """
    global dataAboutUser

    if not Authentication(message.from_user.id):
        await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.mistake}',
                               reply_markup=GeneralKeyboards.single_btn_command_start)
        return


    await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.welcome}',
                           reply_markup=GeneralKeyboards.single_btn_command_start)



# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _

async def user_agreement(message: types.Message):
    global dataAboutUser
    if message.text == "Согласиться":
        try:
            dateRequest: dict
            dateRequest = requests.post(
                f"{BASE_URL}/consent/save_response", json={"user_tg_id": dataAboutUser[message.from_user.id]["user_tg_id"],
                                                           "response": 1}).json()
        except Exception as e:
            log_error(e)
            await bot.send_sticker(message.from_user.id, sticker=open("data/png/file_131068229.png", 'rb'))
            await bot.send_message(message.from_user.id, txt_reg.mistake)
        if dateRequest["action"] == "success":
            await UserState.get_dateAboutUser_name.set()
            ts(1)
            await bot.send_message(message.from_user.id, txt_reg.t_reg_name_1)
            ts(1)
            await bot.send_message(message.from_user.id, txt_reg.t_reg_name_2)
    else:
        await bot.send_message(message.from_user.id, txt_reg.t_foolproof_buttons)
        await UserState.start_register.set()


def startReg(dp=dp):
    dp.register_message_handler(user_agreement, state=AgreementUser.get_user_info)
    dp.register_message_handler(startCommand, commands=["start"], state="*")
