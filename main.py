from aiogram.utils import executor
from handlers import *
from handlers.orders import orders_reg
from loader import dp
from loader import bot



# Launching grouped registered handlers
main_menu_reg(dp)
startReg(dp)
orders_reg(dp)
profile_menu_reg(dp)

# Starting pooling and skipping messages during the deactivation of the bot
executor.start_polling(dp, skip_updates=True)


