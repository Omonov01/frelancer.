import asyncpg
from aiogram import types
from keyboards.default.admin import admin
from keyboards.default.base_window import base_menu
from keyboards.default.category import categoryMenu
from loader import dp,db
from aiogram.dispatcher import filters
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from states.forma import adminposition,userposition

@dp.message_handler(filters.IDFilter(user_id=ADMINS) , text="admin",state=userposition.baseposition)
async def adminrwindow(message : types.Message,state:FSMContext):
    await message.answer("admin oynasiga xush kelibsiz",reply_markup=admin)
    await adminposition.baseadmin.set()


@dp.message_handler(text="statistika",state=adminposition.baseadmin)
async def adminrwindow(message : types.Message,state:FSMContext):
    await message.answer("statistika hisobotlari")
    empcount = await db.call_count_emp()
    frcount = await db.call_count_fr()
    postcount = await db.call_count_post()
    bigempcount = await db.call_count_big_emp()

    report = f"Ish beruvchilar soni {empcount}\n"
    report += f"freelanserlar soni {frcount}\n"
    report += f"postlar soni {postcount}\n"
    report += f"bigemp soni {bigempcount}"
    await message.answer(report)

@dp.message_handler(text="reklama",state=adminposition.baseadmin)
async def advertisingwindow(message : types.Message,state:FSMContext):
    await message.answer("reklama matnini kiriting")
    await adminposition.reklama()

    
@dp.message_handler(state=adminposition.reklama, content_types=[types.ContentType.PHOTO,types.ContentType.TEXT,types.ContentType.VIDEO])
async def advertisingwindow(message : types.Message,state:FSMContext):
    adv = message

    await state.update_data(
        {"name": adv}
    )
    await message.answer("Reklama yuboriluvchi guruhni aniqlang",reply_markup=categoryMenu)
    await adminposition.adv()

@dp.message_handler(state=adminposition.adv)
async def advertisingwindow(message : types.Message,state:FSMContext):
    post_category = message.text()

    await state.update_data(
        {"post_category":post_category}
    )

    data = await state.get_data()
    adv = data.get("name")
    category = data.get(post_category)
    category_id = await db.call_category_id(
        category_name=category
    )
    

@dp.message_handler(text="csv",state=adminposition.baseadmin)
async def adminrwindow(message : types.Message,state:FSMContext):
    await message.answer("Malumotlarni csv formatga ajratib olish")
    

@dp.message_handler(text="⬅️ Orqaga",state=adminposition.baseadmin)
async def adminrwindow(message : types.Message,state:FSMContext):
    await message.answer("bosh oynaga o'tdingiz",reply_markup=base_menu)