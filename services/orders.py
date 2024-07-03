from utils.general import log_error
from data import dataAboutUser
import requests
from loader import *

def pretty_print_dict(dictionary):
    """
    Функция для красивого вывода словаря в Telegram.
    """
    # Перевод ключей на русский язык
    russian_keys = {
        'apartment': 'Квартира',
        'building': 'Здание',
        'city': 'Город',
        'client_id': 'ID клиента',
        'district': 'Район',
        'end_date': 'Дата окончания',
        'end_time': 'Время окончания',
        'house': 'Дом',
        'options': 'Опции',
        'order_id': 'Номер заказа',
        'pet_id': 'ID животного',
        'region': 'Регион',
        'service_details': 'Детали услуги',
        'service_type': 'Тип услуги',
        'start_date': 'Дата начала',
        'start_time': 'Время начала',
        'status': 'Статус',
        'street': 'Улица'
    }

    # Формируем текст для вывода
    output_text = ''
    for key, value in dictionary.items():
        output_text += f'{russian_keys[key]}: {value}\n'

    return output_text
