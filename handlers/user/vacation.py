import asyncpg
from aiogram import types
from loader import dp,db
from aiogram.dispatcher import FSMContext
from states.forma import userposition

@dp.message_handler(text="📁 Vakansiya e'lon qilish", state=userposition.baseposition)
async def beginform(message: types.Message, state: FSMContext):
    await db.add_big_employee(
        telegram_id=message.from_user.id
    )
    await message.answer("Bu tugma bosilganda reklama shartlari yozilgan kanal linki chiqadi")
   
