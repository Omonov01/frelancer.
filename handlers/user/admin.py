import asyncpg
import asyncio
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
    # frnumbertocategory = await db.call_frnumber_to_category()
    # postnumbertocategory = await db.call_postnumber_to_category()

    report = f"Ish beruvchilar soni {empcount}\n"
    report += f"freelanserlar soni {frcount}\n"
    report += f"postlar soni {postcount}\n"
    report += f"bigemp soni {bigempcount}"
    # report += f"Frelancerlarning kategoriya buyicha soni {frnumbertocategory}"
    # report += f"Postlarning kategoriya buyicha soni {postnumbertocategory}"
    await message.answer(report)
    

@dp.message_handler(text="reklama",state=adminposition.baseadmin)
async def advertisingwindow(message : types.Message,state:FSMContext):
    await message.answer("Reklama beruvchi yunalishini tanlang",reply_markup=categoryMenu)
    await adminposition.reklama.set()

@dp.message_handler(state=adminposition.reklama)
async def advertisingwindow(message : types.Message,state:FSMContext):
    post_category = message.text
    await state.update_data(
        {"post_category":post_category}
    )
    await message.answer("Junatmoqchi bulgan reklama matningizni kiriting!!")
    await adminposition.adv.set()

@dp.message_handler(state=adminposition.adv, content_types=[types.ContentType.PHOTO,types.ContentType.TEXT,types.ContentType.VIDEO])
async def advertisingwindow(message : types.Message,state:FSMContext):
    # adv = message
    
    # await state.update_data(
    #     {"adv": adv}
    # )
    
    advertising = await state.get_data()
    category = advertising.get("post_category")
    # advmessage = advertising.get("adv")
    category_id = await db.call_category_id(category_name=category)
    fr_telegram_id = await db.call_freelancer_id_look_category_id(categoryid=category_id)
    try:
        for telegram_id in fr_telegram_id:
            send_id = telegram_id[0]
            await message.copy_to(chat_id=send_id,reply_markup=message)
            await asyncio.sleep(0.5)
        await message.answer("admin oynasi",reply_markup=admin)
        await adminposition.baseadmin.set()
    except:
        await message.answer("admin oynasi",reply_markup=admin)
        await adminposition.baseadmin.set()
        pass




@dp.message_handler(text="⬅️ Orqaga",state=adminposition.baseadmin)
async def adminrwindow(message : types.Message,state:FSMContext):
    await message.answer("bosh oynaga o'tdingiz",reply_markup=base_menu)
    await userposition.baseposition.set()