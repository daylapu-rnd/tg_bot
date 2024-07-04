from data import dataAboutUser
import requests
from loader import *
from handlers import *


def user_phone_info(phone):
    global dataAboutUser
    dataAboutUser = requests.post(f'{BASE_URL}/admin/search_user', json={"phone": phone}).json()
    return dataAboutUser["data"]