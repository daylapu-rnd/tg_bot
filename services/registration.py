from utils.general import Accounting
from utils.general import log_error
from data import dataAboutUser
import requests
from loader import *

def Authentication(user_tg_id):
    try:
        global dataAboutUser
        dataAboutUser[user_tg_id] = {"user_tg_id": user_tg_id}

        # Register user in the service
        Accounting(dataAboutUser[user_tg_id]["user_tg_id"])

        

        return True
    except Exception as e:
        log_error(e)
        return False



def requestToRegistration(jsonBody):
    try:
        userData = requests.post(f'{BASE_URL}/client/registrations',json= jsonBody)
        return True
    except Exception as e:
        log_error(e)
        return False