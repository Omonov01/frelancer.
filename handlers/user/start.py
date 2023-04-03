from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.base_window import base_menu 
from keyboards.default.language import language_menu 
from states.forma import userposition
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalom alaykum, {message.from_user.full_name}!")
    await message.answer(f"Hush kelipsiz o'z shaxsiy oynangizni tanlang",reply_markup=base_menu)
    await userposition.baseposition.set()