"""text for tg_bot"""


class txt_reg:
    """
    A class representing text for use in bot scripts

    IMPORTANT: The text is mainly before registration.py and during registration.py

    Example of using a class:
    """
    welcome = 'Привет!'
    mistake = "Упс... Ошибочка вышла 🤷‍♂️"


class txt_mistakes:
    fool_use_buttons = "Пожалуйста, используй предложенные кнопки!"
    phone_mistake = "Пожалуйста, введи корректный номер телефона!"
    email_mistake = "Пожалуйста, введи корректный адрес электронной почты!"


class txt_main_menu:
    section_main_menu = "Раздел: Главное меню"


class txt_profile_menu:
    what_to_change = "Что ты хочешь изменить?"

    ask_name = "Отправь новое имя текстом"
    ask_email = "Отправь новую почту текстом"
    ask_phone = "Отправь новый номер телефона текстом"

    name_confirmation = "Ты уверен, что тебя зовут"
    email_confirmation = ('Ты уверен, что "', '" - твоя почта?')
    phone_confirmation = ('Ты уверен, что "', '" - твой номер телефона?')