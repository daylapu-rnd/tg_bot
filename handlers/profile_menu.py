from datetime import datetime
from datetime import time
from datetime import timedelta
from aiogram import types
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
import requests


async def profile_menu_handler(message: types.Message):
    if message.text == "Изменить информацию о профиле":
        await bot.send_message(message.from_user.id, txt_profile_menu.what_to_change,
                               reply_markup=GeneralKeyboards.group_kb_change_info)
        await ChangeProfileInfoState.start_change_info.set()
    elif message.text == "Веруться в меню":
        await bot.send_message(message.from_user.id, txt_main_menu.section_main_menu,
                               reply_markup=GeneralKeyboards.group_kb_main_menu)
        await MainMenuState.start_menu.set()


async def change_info_handler(message: types.Message):
    global old_info
    old_info = {}
    tg_id = message.from_user.id
    try:
        old_info[tg_id] = requests.post(f"{BASE_URL}/client/profile",
                                 json={"tg_id": tg_id}).json()['data']
    except Exception as e:
        log_error(e)
        await bot.send_message(message.from_user.id, txt_reg.mistake,
                               reply_markup=GeneralKeyboards.group_kb_main_menu)
        await MainMenuState.start_menu.set()

    if message.text == "Изменить имя":
        await bot.send_message(message.from_user.id, txt_profile_menu.ask_name, reply_markup=ReplyKeyboardRemove())
        await ChangeProfileInfoState.change_name.set()
    elif message.text == "Изменить почту":
        await bot.send_message(message.from_user.id, txt_profile_menu.ask_email, reply_markup=ReplyKeyboardRemove())
        await ChangeProfileInfoState.change_email.set()
    elif message.text == "Изменить номер телефона":
        await bot.send_message(message.from_user.id, txt_profile_menu.ask_phone,
                               reply_markup=ReplyKeyboardRemove())
        await ChangeProfileInfoState.change_phone.set()
    elif message.text == "Веруться в меню":
        await bot.send_message(message.from_user.id, txt_main_menu.section_main_menu,
                               reply_markup=GeneralKeyboards.group_kb_main_menu)
        await MainMenuState.start_menu.set()
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.fool_use_buttons,
                               reply_markup=GeneralKeyboards.group_kb_change_info)
        await ChangeProfileInfoState.start_change_info.set()


async def change_name_handler(message: types.Message):
    global new_name
    new_name = {message.from_user.id: message.text.lower().capitalize()}
    new_name_local = new_name[message.from_user.id]
    if is_valid_name(new_name_local):
        await bot.send_message(message.from_user.id, f'{txt_profile_menu.name_confirmation} {new_name_local}?',
                               reply_markup=GeneralKeyboards.group_kb_yes_or_no)
        await ChangeProfileInfoState.change_name_confirm.set()
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.name_mistake, reply_markup=ReplyKeyboardRemove())
        await ChangeProfileInfoState.change_name.set()


async def change_email_handler(message: types.Message):
    global new_email
    new_email = {message.from_user.id: message.text}
    new_email_local = new_email[message.from_user.id]
    if is_valid_email(new_email_local):
        await bot.send_message(message.from_user.id, f'{txt_profile_menu.email_confirmation[0]}{new_email_local}{txt_profile_menu.email_confirmation[1]}',
                               reply_markup=GeneralKeyboards.group_kb_yes_or_no)
        await ChangeProfileInfoState.change_email_confirm.set()
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.email_mistake)
        await ChangeProfileInfoState.change_email.set()


async def change_phone_handler(message: types.Message):
    global new_phone
    new_phone = {message.from_user.id: message.text}
    new_phone_local = new_phone[message.from_user.id]
    if is_valid_phone_number(new_phone_local):
        await bot.send_message(message.from_user.id, f'{txt_profile_menu.phone_confirmation[0]}{format_phone_number(new_phone_local)}{txt_profile_menu.phone_confirmation[1]}',
                               reply_markup=GeneralKeyboards.group_kb_yes_or_no)
        await ChangeProfileInfoState.change_phone_confirm.set()
    else:
        await bot.send_message(message.from_user.id, txt_mistakes.phone_mistake)
        await ChangeProfileInfoState.change_phone.set()


async def change_name_confirmation_handler(message: types.Message):
    global new_name, old_info
    tg_id = old_info[message.from_user.id]["tg_id"]
    new_name_local = new_name[message.from_user.id]
    old_email = old_info[message.from_user.id]["email"]
    old_phone = old_info[message.from_user.id]["phone"]

    if message.text == "Да":
        try:
            requests.post(f"{BASE_URL}/client/profile/change_info",
                           json={"tg_id": tg_id, "name": new_name_local, "email": old_email, "phone": old_phone}).json()
            await bot.send_message(message.from_user.id, "Имя успешно обновлено!",
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()
        except Exception as e:
            log_error(e)
            await bot.send_message(message.from_user.id, txt_reg.mistake,
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()
    else:
        await bot.send_message(message.from_user.id, txt_profile_menu.ask_name, reply_markup=ReplyKeyboardRemove())
        await ChangeProfileInfoState.change_name.set()


async def change_email_confirmation_handler(message: types.Message):
    global new_email, old_info
    tg_id = old_info[message.from_user.id]["tg_id"]
    new_email_local = new_email[message.from_user.id]
    old_name = old_info[message.from_user.id]["name"]
    old_phone = old_info[message.from_user.id]["phone"]

    if message.text == "Да":
        try:
            requests.post(f"{BASE_URL}/client/profile/change_info",
                           json={"tg_id": tg_id,"name": old_name, "email": new_email_local, "phone": old_phone}).json()
            await bot.send_message(message.from_user.id, "Почта успешно обновлена!",
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()
        except Exception as e:
            log_error(e)
            await bot.send_message(message.from_user.id, txt_reg.mistake,
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()
    else:
        await bot.send_message(message.from_user.id, txt_profile_menu.ask_email, reply_markup=ReplyKeyboardRemove())
        await ChangeProfileInfoState.change_email.set()


async def change_phone_confirmation_handler(message: types.Message):
    global new_phone, old_info
    tg_id = old_info[message.from_user.id]["tg_id"]
    new_phone_local = new_phone[message.from_user.id]
    old_email = old_info[message.from_user.id]["email"]
    old_name = old_info[message.from_user.id]["name"]

    if message.text == "Да":
        try:
            requests.post(f"{BASE_URL}/client/profile/change_info",
                           json={"tg_id": tg_id,"name": old_name, "email": old_email, "phone": format_phone_number(new_phone_local, 1)}).json()
            await bot.send_message(message.from_user.id, "Номер телефона успешно обновлен!",
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()
        except Exception as e:
            log_error(e)
            await bot.send_message(message.from_user.id, txt_reg.mistake,
                                   reply_markup=GeneralKeyboards.group_kb_main_menu)
            await MainMenuState.start_menu.set()
    else:
        await bot.send_message(message.from_user.id, txt_profile_menu.ask_phone, reply_markup=ReplyKeyboardRemove())
        await ChangeProfileInfoState.change_phone.set()


# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _
def profile_menu_reg(dp=dp):
    # - - - Message handlers - - -
    dp.register_message_handler(profile_menu_handler, state=ProfileMenuState.start_profile_menu)
    dp.register_message_handler(change_info_handler, state=ChangeProfileInfoState.start_change_info)

    dp.register_message_handler(change_name_handler, state=ChangeProfileInfoState.change_name)
    dp.register_message_handler(change_email_handler, state=ChangeProfileInfoState.change_email)
    dp.register_message_handler(change_phone_handler, state=ChangeProfileInfoState.change_phone)

    dp.register_message_handler(change_name_confirmation_handler, state=ChangeProfileInfoState.change_name_confirm)
    dp.register_message_handler(change_email_confirmation_handler, state=ChangeProfileInfoState.change_email_confirm)
    dp.register_message_handler(change_phone_confirmation_handler, state=ChangeProfileInfoState.change_phone_confirm)


    # - - - Callback handlers - - -