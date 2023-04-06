import asyncpg
from aiogram import types
from loader import dp,db
from aiogram.dispatcher import FSMContext
from states.forma import userposition

@dp.message_handler(text="📁 Vakansiya e'lon qilish", state=userposition.baseposition)
async def beginform(message: types.Message, state: FSMContext):
    try:
        await db.add_big_employee(
            telegram_id=message.from_user.id
        )
    except asyncpg.exceptions.UniqueViolationError:
        url = "Vakansiya va Reklama joylashtirish uchun adminga murojaat qiling!!!\n"
        url += "https://t.me/FF_UZ_admin"
        await message.answer(url)
   
