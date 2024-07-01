import os
from datetime import datetime


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