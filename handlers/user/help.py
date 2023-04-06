from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Bot orqali siz uzingizga malakali hodim va frilanserlarni yollashingiz yoki o'zingizga mos ish topishingiz mumkin!")
    
    await message.answer("\n".join(text))
