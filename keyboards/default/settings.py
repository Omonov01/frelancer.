from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

settings_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="Ismni o'zgartirish"),
               KeyboardButton(text="familiyani o'zgartirish"),
       ],
       [
               KeyboardButton(text="Men haqimdagi malumotlar"),
       ],
       [
               KeyboardButton(text="Berilgan elonni o'chirish"),
       ],
       [
               KeyboardButton(text="🏠 Bosh menyuga qaytish"),
       ],
    ],
    resize_keyboard=True
)