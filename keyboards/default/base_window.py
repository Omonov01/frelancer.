from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

base_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="👩🏻‍💻 Men hodimman/frilanserman"),
               KeyboardButton(text="🧔🏻‍♂️ Men ish beruvchiman"),
       ],
       [
               KeyboardButton(text="📁 Vakansiya e'lon qilish"),
       ],
#        [
#                KeyboardButton(text=" 🔄 Tilni O'zgartirish")
#        ],
#        [
#                KeyboardButton(text="Forma"),
#        ],
    ],
    resize_keyboard=True
)