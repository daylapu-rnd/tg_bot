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

def startReg(dp=dp):
    dp.register_message_handler(startCommand, commands=["start"], state="*")
