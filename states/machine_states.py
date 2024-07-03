"""
Classes with states machines:
- States group for the registration.py process
- States group for the process of creating a trip
- States group for recording information about the car
- States group for the menu status
- States group for the about menu status

Example usage:

menu_about_state = MenuAbout()
menu_about_state.start_state.set()

def menuAll(dp=dp):
    dp.register_message_handler(startCommand, commands=["menu"], states="*")
    dp.register_message_handler(aboutCommand, states=MenuAbout.start_state)
"""


from aiogram.dispatcher.filters.state import State, StatesGroup




class UserState(StatesGroup):
    """Register state"""
    start_register = State()

    get_dateAboutUser_fio = State()
    get_dateAboutUser_mail = State()
    get_dateAboutUser_number = State()
    go_menu = State()



class MainMenuState(StatesGroup):
    """Main menu states"""
    start_menu = State()


class ProfileMenuState(StatesGroup):
    """Profile menu states"""
    start_profile_menu = State()


class ChangeProfileInfoState(StatesGroup):
    start_change_info = State()

    change_name = State()
    change_email = State()
    change_phone = State()

    change_name_confirm = State()
    change_email_confirm = State()
    change_phone_confirm = State()

