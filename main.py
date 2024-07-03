from aiogram.utils import executor
from handlers import *
from loader import dp
from loader import bot



# Launching grouped registered handlers
startReg(dp)
main_menu_reg(dp)
profile_menu_reg(dp)


# Starting pooling and skipping messages during the deactivation of the bot
executor.start_polling(dp, skip_updates=True)


