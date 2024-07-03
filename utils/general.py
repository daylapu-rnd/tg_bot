import os
from datetime import datetime
from aiogram import types
from loader import BASE_URL
import requests


def get_next_error_number(path):
    """Reads the file and gives the error number"""
    try:
        if os.path.exists(path):
            with open(path, "r") as file:
                if lines := file.readlines():
                    last_line = lines[-1]
                    last_error_number = int(last_line.split(".")[0])
                    return last_error_number + 1
        return 1
    except Exception:
        return 1


def log_error(error_message):
    """Records errors"""
    try:
        timestamp = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")
        error_number = get_next_error_number("data//error_log.txt")
        with open("data/error_log.txt", "a") as file:
            file.write(f"{error_number}. {timestamp} - - - {error_message}\n")
    except Exception as e:
        error_message = str(e)
    else:
        timestamp = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")
        error_number = get_next_error_number("data//error_log.txt")
        with open("data/error_log.txt", "a") as file:
            file.write(f"{error_number}. {timestamp} - - - {error_message}\n")


def Accounting(tg_id):
    """Records the launch of the bot by users"""
    error_number = get_next_error_number("data//accounting.txt")
    now = datetime.now()
    with open('data//accounting.txt', 'a') as f:
        f.write(f'{error_number}. {now.date()} - - - {now.time()} - - - {tg_id}\n')


def format_date_time(date_time: str):
    """Returns the date or time format"""
    if len(date_time) == 8:
        return f"{date_time[:2]}.{date_time[2:4]}.{date_time[4:]}"
    elif len(date_time) == 4:
        return f"{date_time[:2]}:{date_time[2:]}"
    else:
        return []

def get_client_id(client_tg_id):
    return requests.get(f"{BASE_URL}/client/get_client", json={"tg_id": client_tg_id}).json()['data']['client_id']
