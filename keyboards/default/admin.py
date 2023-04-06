from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

admin = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="statistika"),
               KeyboardButton(text="reklama"),
       ],
#        [
#                KeyboardButton(text="csv"),
#        ],
       [       
               KeyboardButton(text=" ⬅️ Orqaga"),
       ],
    ],
    resize_keyboard=True
)