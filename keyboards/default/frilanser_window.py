from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

frilans_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
        #        KeyboardButton(text="📝 Mening buyurtmalarim"),
               KeyboardButton(text="📥 Buyurtma olish"),
       ],
#        [
#                KeyboardButton(text="🔎 Bajarilgan ishlar ruyxati"),
#                KeyboardButton(text="✅ Yuborgan takliflarim"),
#        ],
       [
               KeyboardButton(text="💸 Mening balansim"),
        #        KeyboardButton(text=" ⚙️ Sozlamalar"),
       ],
       [       
               KeyboardButton(text=" ⬅️ Orqaga"),
       ],
    ],
    resize_keyboard=True
)