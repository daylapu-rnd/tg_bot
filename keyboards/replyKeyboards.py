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
    btn_agreement_accept = KeyboardButton('Согласиться')

    btn_main_menu = KeyboardButton("Веруться в меню")
    btn_profile = KeyboardButton("Профиль")

    btn_change_profile_info = KeyboardButton("Изменить информацию о профиле")

    btn_change_name = KeyboardButton("Изменить имя")
    btn_change_email = KeyboardButton("Изменить почту")
    btn_change_phone = KeyboardButton("Изменить номер телефона")

    btn_yes = KeyboardButton("Да")
    btn_no = KeyboardButton("Нет")



    # Single keyboards

    # - - - Command Start - - -
    single_btn_command_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    single_btn_command_start.add(btn_command_start)

    single_btn_registration = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    single_btn_registration.add(btn_register).add(btn_about)



    # Group keyboards


 # - - - User Agreement -  - -
    group_agreement = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group_agreement.row(btn_agreement_accept)
    
    group_kb_yes_or_no = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group_kb_yes_or_no.row(btn_yes, btn_no)

    # - - - Main menu - - -
    group_kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group_kb_main_menu.add(btn_profile)

    # - - - Profile menu - - -
    group_kb_profile_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group_kb_profile_menu.add(btn_change_profile_info)

    group_kb_change_info = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    group_kb_change_info.add(btn_change_name, btn_change_email, btn_change_phone)




