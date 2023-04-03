from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

language_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="🇺🇿 O'zbek tili"),
               KeyboardButton(text="🇷🇺 Rus tili"),
               KeyboardButton(text="🇺🇸 Englis tili"),
       ],
    ],
    resize_keyboard=True
)