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
    """Register states"""
    start_register = State()
