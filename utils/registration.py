import re


def is_valid_email(email):
    # Регулярное выражение для проверки email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Проверка соответствия
    if re.match(regex, email):
        return True
    else:
        return False


def is_valid_phone_number(phone_number: str) -> bool:
    # Убираем пробелы, скобки и тире
    cleaned_number = re.sub(r'[ \(\)\-]', '', phone_number)
    # Проверяем, начинается ли номер с +7 или 8
    if cleaned_number.startswith('+7'):
        # Должно быть 12 символов: +7 и 10 цифр
        return len(cleaned_number) == 12 and cleaned_number[1:].isdigit()
    elif cleaned_number.startswith('8'):
        # Должно быть 11 символов: 8 и 10 цифр
        return len(cleaned_number) == 11 and cleaned_number.isdigit()
    else:
        return False


import re

def format_phone_number(phone_number, format_type=0):
    # Удаляем все символы, кроме цифр
    digits = re.sub(r'\D', '', phone_number)

    # Проверяем, что номер начинается с 8 или +7 и корректируем его
    if digits.startswith('8'):
        digits = '7' + digits[1:]
    elif digits.startswith('7'):
        pass
    else:
        digits = '7' + digits

    if format_type == 0:
        # Форматируем номер телефона в формате +7 (xxx) xxx-xx-xx
        formatted_number = f'+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}'
    elif format_type == 1:
        # Форматируем номер телефона в формате +78005553535
        formatted_number = f'+7{digits[1:]}'
    else:
        raise ValueError("Invalid format_type. Use 0 or 1.")

    return formatted_number
