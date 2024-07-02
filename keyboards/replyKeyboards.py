from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# General section
class GeneralKeyboards:
    """
    Class with buttons for the bot.

    Attributes:
    - Buttons
    - Single keyboards
    - Group keyboards

    Example usage:
    my_keyboards = GeneralKeyboards()
    start_menu_keyboard = my_keyboards.group_startMenu

    reply_markup=GeneralKeyboards.mainMenu)
    """
    # Buttons
    btn_command_start = KeyboardButton("/start")
    btn_register = KeyboardButton("Зарегистрироваться")
    btn_about = KeyboardButton("О сервисе")

    # Single keyboards

    # - - - Command Start - - -
    single_btn_command_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    single_btn_command_start.add(btn_command_start)
    
    single_btn_registration = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    single_btn_registration.add(btn_register).add(btn_about)



    # Group keyboards




