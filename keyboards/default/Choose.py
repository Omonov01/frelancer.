from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

frilans_choose_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="Hodim bo'lib e'lon berish"),
               KeyboardButton(text="Frilanser bo'lib e'lon berish"),
       ],
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

employee_choose_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="Hodim uchun e'lon berish"),
               KeyboardButton(text="Frilanser uchun e'lon berish"),
       ],
    ],
    resize_keyboard=True
)