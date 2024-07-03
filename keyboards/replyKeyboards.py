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
    btn_support = KeyboardButton("Поддержка")

    btn_main_menu = KeyboardButton("Вернуться в меню")
    btn_profile = KeyboardButton("Профиль")

    btn_change_profile_info = KeyboardButton("Изменить информацию о профиле")

    btn_change_name = KeyboardButton("Изменить имя")
    btn_change_email = KeyboardButton("Изменить почту")
    btn_change_phone = KeyboardButton("Изменить номер телефона")

    btn_yes = KeyboardButton("Да")
    btn_no = KeyboardButton("Нет")

    btn_my_orders = KeyboardButton("Мои заказы")
    btn_past_orders = KeyboardButton("Прошлые заказы")
    btn_active_orders = KeyboardButton("Активные заказы")


    # Single keyboards

    # - - - Command Start - - -
    single_btn_command_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    single_btn_command_start.add(btn_command_start)
    
    single_btn_registration = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    single_btn_registration.add(btn_register)



    # Group keyboards

    group_kb_yes_or_no = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group_kb_yes_or_no.row(btn_yes, btn_no)

    # - - - Main menu - - -
    group_kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    group_kb_main_menu.add(btn_profile,btn_my_orders,btn_support,btn_about)

    # - - - Profile menu - - -
    group_kb_profile_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group_kb_profile_menu.add(btn_change_profile_info, btn_main_menu)

    group_kb_change_info = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    group_kb_change_info.add(btn_change_name, btn_change_email, btn_change_phone, btn_profile)

    # - - - Orders - - -
    group_kb_orders = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group_kb_orders.add(btn_past_orders,btn_active_orders,btn_main_menu)




