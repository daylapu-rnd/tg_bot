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

import re
from handlers import main_menu


async def startCommand(message: types.Message):
    """
    startCommand function
    """
    global dataAboutUser

    if not Authentication(message.from_user.id):
        await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.mistake}',
                               reply_markup=GeneralKeyboards.single_btn_command_start)
        return
    
    
    if not Authorisation(dataAboutUser[message.from_user.id]["user_tg_id"]):
        await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.welcome}',
                            reply_markup=GeneralKeyboards.single_btn_registration)
        await UserState.start_register.set()
    else:
        await MainMenuState.start_menu.set()
        await main_menu.menu_command(message)


async def fio(message: types.Message):
    global dataAboutUser
    if message.text == "Зарегистрироваться":
        await AgreementUser.get_user_info.set()
        await bot.send_message(message.from_user.id, f'{txt_reg.t_agreement_1}',
                               reply_markup=GeneralKeyboards.group_agreement)
        await bot.send_message(message.from_user.id, f'{txt_reg.t_agreement_2}',
                               reply_markup=keyboards.inlineKeyboards.UserAgreement)
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.fool_use_buttons,
                               reply_markup=GeneralKeyboards.single_btn_command_start)

async def ask_phone(message: types.Message):
    global dataAboutUser
    if re.fullmatch(r'[А-Яа-яЁё\s]+', message.text):
        dataAboutUser[message.from_user.id]["name"] = message.text
        await UserState.get_dateAboutUser_number.set()
        await bot.send_message(message.from_user.id, f'{txt_reg.numb}')
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.name_mistake)
        await UserState.get_dateAboutUser_fio.set() 

async def ask_mail(message: types.Message):
    global dataAboutUser
    if message.text.startswith('+7') or message.text.startswith('8'):
        dataAboutUser[message.from_user.id]["phone"] = message.text
        await UserState.get_dateAboutUser_mail.set()
        await bot.send_message(message.from_user.id, f'{txt_reg.mail}')
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.phone_mistake)
        await UserState.get_dateAboutUser_number.set() 

async def go_to_menu(message: types.Message):
    global dataAboutUser
    if "@" in message.text:
        dataAboutUser[message.from_user.id]["mail"] = message.text
        await bot.send_message(message.from_user.id, f'Все прошло успешно')
        #Запрос на POST этих данных
        if not requestToRegistration({
            'tg_id':dataAboutUser[message.from_user.id]["user_tg_id"],
            'name':dataAboutUser[message.from_user.id]["name"],
            'phone':dataAboutUser[message.from_user.id]["phone"],
            'email':dataAboutUser[message.from_user.id]["mail"]}):

            await bot.send_message(message.from_user.id, f'{txt_reg.mail}')
            return
        #   func to go to the menu
        await MainMenuState.start_menu.set()
        await main_menu.menu_command(message)
        
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.email_mistake)
        await UserState.get_dateAboutUser_mail.set()
        

    
# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _

async def user_agreement(message: types.Message):
    global dataAboutUser
    if message.text == "Согласиться":
        try:
            dateRequest = requests.post(
                f"{BASE_URL}/consent/save_response", json={"user_tg_id": dataAboutUser[message.from_user.id]["user_tg_id"],
                                                           "response": 1}).json()
        except Exception as e:
            log_error(e)
            await bot.send_message(message.from_user.id, txt_reg.mistake)
        if dateRequest["action"] == "success":
            await UserState.get_dateAboutUser_fio.set()
            ts(1)
            await bot.send_message(message.from_user.id, txt_reg.t_reg_name_1)
            ts(1)
            await bot.send_message(message.from_user.id, txt_reg.fio)
    else:
        await bot.send_message(message.from_user.id, txt_reg.t_foolproof_buttons)
        await UserState.start_register.set()
# ============== admin ================================================================


async def get_phone(message: types.Message):
    await bot.send_message(message.from_user.id, "Укажите номер телефона.")
    await AdminState.get_user_phone.set()



async def findUser_by_phone(message: types.Message):
    try:
        info = user_phone_info(message.text)
    
        if len(info) == 0:
            await bot.send_message(message.from_user.id, "Нет такого пользователя.")
        else:
            await bot.send_message(message.from_user.id, info)
            await MainMenuState.start_menu.set()
    except Exception as e:
        log_error(e)



def startReg(dp=dp):
    dp.register_message_handler(get_phone, commands=["find_phone"], state="*")
    dp.register_message_handler(findUser_by_phone, state=AdminState.get_user_phone)
    dp.register_message_handler(startCommand, commands=["start"], state="*")
    dp.register_message_handler(user_agreement, state=AgreementUser.get_user_info)
    dp.register_message_handler(fio, state=UserState.start_register)
    dp.register_message_handler(ask_phone, state=UserState.get_dateAboutUser_fio)
    dp.register_message_handler(ask_mail, state=UserState.get_dateAboutUser_number)
    dp.register_message_handler(go_to_menu, state=UserState.get_dateAboutUser_mail)
