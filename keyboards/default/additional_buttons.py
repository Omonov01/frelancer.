from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

###Frelansers balans sheet button
frilans_balans_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="💰 Pulni chiqarish"),
       ],
       [       
               KeyboardButton(text="⬅️  Orqaga"),
             
       ],
    ],
    resize_keyboard=True
)

# Employee balans sheet button
employee_balans_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="💰 Hisobni to'ldirish"),
       ],
       [       
               KeyboardButton(text="⬅️  Orqaga"),
             
       ],
    ],
    resize_keyboard=True
)
###back buttom
back_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
               KeyboardButton(text="⬅️ Orqaga"),
             
       ],
    ],
    resize_keyboard=True
)


###Button for take user's phone number
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phonenumber = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Telefon raqamingizni ulashing', request_contact=True),
        ],
    ],
    resize_keyboard=True
)
###ha yoki yuq
yes_no = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ha'),
        ],
         [
            KeyboardButton(text="Yo'q"),
        ],
    ],
    resize_keyboard=True
)