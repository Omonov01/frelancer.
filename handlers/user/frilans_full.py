import asyncpg
from aiogram import types
from keyboards.default.base_window import base_menu
from keyboards.default.frilanser_window import frilans_menu 
from keyboards.default.settings import settings_menu 
from keyboards.default.additional_buttons import back_menu,frilans_balans_menu
from loader import dp,db
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
from states.forma import userposition,personaldata

### frilanser oynasiga o'tish
@dp.message_handler(text="👩🏻‍💻 Men hodimman/frilanserman",state=userposition.baseposition)
async def movetofrwindow(message : types.Message,state:FSMContext):
    try:
        if await db.call_freelancer_id(telegramid=message.from_user.id):
            button = await message.answer("Shaxsiy profilingizga hush kelipsiz",reply_markup=frilans_menu)
            employee_position = await userposition.frilansposition.set()
            return [button,employee_position]
        else:
            matn = await message.answer("Assalom alaykum bu bo'limni to'ldirganingizdan keyin biz sizga sizning sohangizga mos bo'lgan ish elonlarini junatamiz")
            ism = await message.answer("Ismingizni kiriting!!!")
            forma_position = await personaldata.name.set()
            return [matn,ism,forma_position]
    except asyncpg.exceptions.UniqueViolationError:
            pass

### Asosiy oynaga qaytish
@dp.message_handler(text="⬅️ Orqaga",state=userposition.frilansposition)
async def backtobasefromfrwindow(message : types.Message,state:FSMContext):
    await message.answer("Asosiy oyna",reply_markup=base_menu)
    await userposition.baseposition.set()

###Buyurtmalarni ko'rish
# @dp.message_handler(text="📝 Mening buyurtmalarim",state=userposition.frilansposition)
# async def movetofroffer(message : types.Message,state:FSMContext):
#     await message.answer("!")
    # await userposition.frilansposition.set()

###Buyurtmalarni ko'rish va ariza topshirish
@dp.message_handler(text="📥 Buyurtma olish",state=userposition.frilansposition)
async def movetofrrequest(message : types.Message,state:FSMContext):
    try:
        posts = await db.call_element_from_post_to_fr()
        for post in posts:
            post_id = post[0]
            project_name = post[1]
            project_description = post[2]
            project_cost = post[3]
            project_link = post[4]
            project_technology = post[5]
            
            elon = f"Siz yaratgan elon tartib raqami : {post_id}\n"
            elon += f"Project nomi : {project_name}\n"
            elon += f"Project haqida:{project_description}\n"
            elon += f"Project narxi : {project_cost}\n"
            elon += f"Bog'lanish uchun link : {project_link}\n"
            elon += f"Ishlatiladigan texnologiyalar : {project_technology}\n"
            # print(elon)
            await message.answer(elon)
    
    except asyncpg.exceptions.UniqueViolationError:
            pass
    #await userposition.frilansposition.set()

###Bajargan buyurtmalarini ko'rish
# @dp.message_handler(text="🔎 Bajarilgan ishlar ruyxati",state=userposition.frilansposition)
# async def movetofrtask(message : types.Message,state:FSMContext):
#     await message.answer("")
    #await userposition.frilansposition.set()

### Ish uchun yuborgan takliflari holatini ko'radi
# @dp.message_handler(text="✅ Yuborgan takliflarim",state=userposition.frilansposition)
# async def movetofrresponse(message : types.Message,state:FSMContext):
#     await message.answer("Hozircha bu finksiya ishlamayapti. Siz tog'ridan to'g'ri mijoz bilan aloqaga chiqishingiz mumkin")
    #await userposition.frilansposition.set()

### Pul yechib olish uchun o'z balansini tekshiradi
@dp.message_handler(text="💸 Mening balansim",state=userposition.frilansposition)
async def movetofrbalans(message : types.Message,state:FSMContext):
    await message.answer("Balans oynasiga o'tdingiz",reply_markup=frilans_balans_menu)
    await userposition.frilansbalansposition.set()

###Frilanser pulni chiqarib oladi
@dp.message_handler(text="💰 Pulni chiqarish",state=userposition.frilansbalansposition)
async def movetofrshot(message : types.Message,state:FSMContext):
    await message.answer("Hozircha bu funksiyamiz ishlamayapti siz to'g'ridan to'gri mijoz bilan kelishishingiz kerak")
    #await userposition.frilansbalansposition.set()

##Frilanser pulni chiqarib oladi
@dp.message_handler(text="⬅️  Orqaga",state=userposition.frilansbalansposition)
async def backtofrwindow(message : types.Message,state:FSMContext):
    await message.answer("Shaxsiy oyna",reply_markup=frilans_menu)
    await userposition.frilansposition.set()

###Frilanser sozlamalar bo'limiga kirib shaxsiy malumotlarini o'zgartiradi
# @dp.message_handler(text="⚙️ Sozlamalar",state=userposition.frilansposition)
# async def movetofr(message : types.Message,state:FSMContext):
#     await message.answer("Sozlamalar oynasiga hush kelibsiz",reply_markup=settings_menu)
#     await userposition.frilanssettinsposition.set()

###sozlamalar bo'limidan Bosh oynaga qaytish
# @dp.message_handler(text="🏠 Bosh menyuga qaytish",state=userposition.frilanssettinsposition)
# async def backtobasefromsettings(message : types.Message,state:FSMContext):
#     await message.answer("Asosiy oyna",reply_markup=base_menu)
#     await userposition.baseposition.set()

