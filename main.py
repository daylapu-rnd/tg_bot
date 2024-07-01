from aiogram.utils import executor
from loader import dp
from loader import bot
from handlers import *


# Launching grouped registered handlers
startReg(dp)


# Starting pooling and skipping messages during the deactivation of the bot
executor.start_polling(dp, skip_updates=True)


