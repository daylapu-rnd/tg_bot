from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


UserAgreement = InlineKeyboardMarkup(row_width= 1)
url_agreement = InlineKeyboardButton('Пользовательское соглашение', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
UserAgreement.add(url_agreement)
