from datetime import datetime
from datetime import time
from datetime import timedelta
from aiogram import types
from aiogram.dispatcher import FSMContext

import keyboards
from loader import ts
from loader import bot
from loader import dp
from loader import BASE_URL
from data import *
from states import *
from keyboards import *
from services import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import requests
import requests
from keyboards import *


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
                           reply_markup=GeneralKeyboards.single_btn_registration)
    await UserState.start_register.set()

async def fio (message:types.Message):

    global dataAboutUser
    if message.text == "Зарегистрироваться":
        await AgreementUser.get_user_info.set()
        await bot.send_message(message.from_user.id, f'{txt_reg.t_agreement_1}',
                               reply_markup=GeneralKeyboards.group_agreement)
        await bot.send_message(message.from_user.id, f'{txt_reg.t_agreement_2}',
                               reply_markup=keyboards.inlineKeyboards.UserAgreement)
        await UserState.get_dateAboutUser_fio.set()
        await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.fio}',reply_markup=ReplyKeyboardRemove())
    else:
        await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'ПОЛЬЗУЙСЯ КНОПКОЙ',
                               reply_markup=GeneralKeyboards.single_btn_command_start)
        await UserState.start_register.set()

async def ask_phone(message: types.Message):
    global dataAboutUser
    dataAboutUser[message.from_user.id]["name"] = message.text
    await UserState.get_dateAboutUser_number.set()
    await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.numb}')

async def ask_mail(message:types.Message):
    global dataAboutUser
    dataAboutUser[message.from_user.id]["phone"] = message.text
    await UserState.go_menu.set()
    await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.mail}')


async def go_to_menu(message:types.Message):
    global dataAboutUser
    dataAboutUser[message.from_user.id]["mail"] = message.text
    await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'Все прошло успешно')
    print(dataAboutUser)
    print(dataAboutUser[message.from_user.id]["name"])


    #Запрос на POST этих данных
    userData = requests.post(f'{BASE_URL}/registrations',json={'tg_id':dataAboutUser[message.from_user.id]["user_tg_id"],
                                                               'name':dataAboutUser[message.from_user.id]["name"],
                                                              'phone':dataAboutUser[message.from_user.id]["phone"],
                                                              'email':dataAboutUser[message.from_user.id]["mail"]})



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
    dp.register_message_handler(fio, state=UserState.start_register)
    dp.register_message_handler(ask_phone, state=UserState.get_dateAboutUser_fio)
    dp.register_message_handler(ask_mail, state=UserState.get_dateAboutUser_number)
    dp.register_message_handler(go_to_menu, state=UserState.go_menu)
