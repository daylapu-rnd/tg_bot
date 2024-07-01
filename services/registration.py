from utils.general import Accounting
from utils.general import log_error
from data import dataAboutUser

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



