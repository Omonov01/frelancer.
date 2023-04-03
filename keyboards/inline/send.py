from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [    
        InlineKeyboardButton(text="Ish beruvchiga bog'lanish", callback_data="bog'lanish"),
    ],
    [   
        InlineKeyboardButton(text="Ulashish",calback_data="Ish")
    ],
    
]
)