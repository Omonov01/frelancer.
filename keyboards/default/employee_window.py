from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

employee_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="📝 Men bergan elonlar"),
               KeyboardButton(text="✅ Bergan elonlarim uchun takliflar"),
       ],
       [
               KeyboardButton(text="📥  Buyurtma yaratish"),
       ], 
       [
               KeyboardButton(text="💸 Balansni to'ldirish"),
        #        KeyboardButton(text="⚙️ Sozlamalar"),
       ],
       [       
               KeyboardButton(text=" ⬅️ Orqaga"),
       ],
    ],
    resize_keyboard=True
)