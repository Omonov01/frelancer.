from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from keyboards.inline.callback import IT_callback,SALES_callback,SEO_callback,SMM_callback,FINANCE_callback,OPERATOR_callback,TARJIMONLIK_callback,TEACHER_callback,DIZAYN_callback,MONTAJ_callback
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="IT va Dasturlash", callback_data="IT"),
    ],
    [
        InlineKeyboardButton(text="Dizayn", callback_data="Dizayn"),
    ],
    [  
        InlineKeyboardButton(text="Seo va Trafik", callback_data="Seo va Trafik"),
    ],
    [    
        InlineKeyboardButton(text="Ijtimoit tarmoq va reklama", callback_data="ijtimoiy tarmoq"),
    ],
    [
        InlineKeyboardButton(text="Tekstlar va tarjimalar", callback_data="Tekstlar va tarjimalar"),
    ],
    [    
        InlineKeyboardButton(text="Audio,Video,Montaj", callback_data="Montaj"),
    ],
    [   
        InlineKeyboardButton(text="Targeting",calback_data="Targeting")
    ],
    [   
        InlineKeyboardButton(text="Tayyor",calback_data="Tayyor")
    ],
    
]
)