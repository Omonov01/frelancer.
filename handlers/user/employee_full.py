import asyncpg
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.base_window import base_menu
from keyboards.default.employee_window import employee_menu 
from keyboards.default.settings import settings_menu 
from keyboards.default.additional_buttons import back_menu,employee_balans_menu
from loader import dp,db
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.forma import userposition,emppersonaldata

### ish beruvchi oynasiga o'tish
@dp.message_handler(text="🧔🏻‍♂️ Men ish beruvchiman",state=userposition.baseposition)
async def movetoempwindow(message : types.Message,state:FSMContext):
    try:
        if await db.call_employee_id(telegramid=message.from_user.id):
            button =   await message.answer("Shaxsiy profilingizga hush kelipsiz",reply_markup=employee_menu) 
            employee_position =  await userposition.employeeposition.set()
            return [button,employee_position]
        else:
            matn = await message.answer("Assalom alaykum shaxsiy oynangizni yaratganingizdan keyin siz freelancerlar uchun ish e'lonlarini yaratishingiz mumkin.")
            ism = await message.answer("Ismingizni kiriting!!!",reply_markup=ReplyKeyboardRemove())
            forma_position = await emppersonaldata.empname.set()
            return [matn,ism,forma_position]
    except asyncpg.exceptions.UniqueViolationError:
            pass

### Asosiy oynaga qaytish
@dp.message_handler(text="⬅️ Orqaga",state=userposition.employeeposition)
async def backtobasefromempwindow(message : types.Message,state:FSMContext):
    await message.answer("Asosiy oyna",reply_markup=base_menu)
    await userposition.baseposition.set()

###Berilgan buyurtmalarni ko'rish
@dp.message_handler(text="📝 Men bergan elonlar",state=userposition.employeeposition)
async def movetoempoffer(message : types.Message,state:FSMContext):
    try:
        posts = await db.call_element_from_post(message.from_user.id)
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
            if post == 0:
                 await message.answer("Siz hali bironta ham e'lon yaratmagansiz!!!")
    except asyncpg.exceptions.UniqueViolationError:
            pass
    
    #await userposition.frilansposition.set()

###Kelgan takliflarni ko'rish
@dp.message_handler(text="✅ Bergan elonlarim uchun takliflar",state=userposition.employeeposition)
async def movetoemprequest(message : types.Message,state:FSMContext):
    await message.answer("Bu oynamiz hozir ishlagani yuq. Biz siz bergan e'lonni tog'ridan to'g'ri botga yuklaymiz va shu kategoriya bilan ruyxatdan o'tgan frilanserlarga junatamiz. Bog'lanish uchun qoldirgan linkingiz orqali ular sizga bog'lanishadi.Rahmat")
    #await userposition.frilansposition.set()


### Balansni to'ldirish
@dp.message_handler(text="💸 Balansni to'ldirish",state=userposition.employeeposition)
async def movetoempbalans(message : types.Message,state:FSMContext):
    await message.answer("Balans oynasi",reply_markup=employee_balans_menu)
    await userposition.employeebalansposition.set()

###Frilanser pulni chiqarib oladi
@dp.message_handler(text="💰 Hisobni to'ldirish",state=userposition.employeebalansposition)
async def movetoempshot(message : types.Message,state:FSMContext):
    await message.answer("Hozircha bu funksiyamiz ishlamayapti siz to'g'ridan to'gri mijoz bilan kelishishingiz kerak")
    #await userposition.employeebalansposition.set()

###Frilanser pulni chiqarib oladi
@dp.message_handler(text="⬅️  Orqaga",state=userposition.employeebalansposition)
async def backtoempwindow(message : types.Message,state:FSMContext):
    await message.answer("Shaxsiy oyna",reply_markup=employee_menu)
    await userposition.employeeposition.set()

###Frilanser sozlamalar bo'limiga kirib shaxsiy malumotlarini o'zgartiradi
# @dp.message_handler(text="⚙️ Sozlamalar",state=userposition.employeeposition)
# async def movetoemp(message : types.Message,state:FSMContext):
#     await message.answer("Sozlamalar oynasiga hush kelibsiz",reply_markup=settings_menu)
#     await userposition.employeesettingsposition.set()

####settings bulimi 
# @dp.message_handler(text="Ismni o'zgartirish",state=userposition.employeesettingsposition)
# async def changename(message : types.Message,state:FSMContext):
#     await message.answer("Yangi ism kiriting:")
#     await db.update_emp_username(
#         username=message.text,
#         telegram_id=message.from_user.id
#     )
#     await message.answer("Ismingiz o'zgartirildi.")

# @dp.message_handler(text="familiyani o'zgartirish",state=userposition.employeesettingsposition)
# async def changefullname(message : types.Message,state:FSMContext):
#     await message.answer("Yangi familiyani kiriting:")
#     await db.update_emp_fullname(
#         fullname=message.text,
#         telegram_id=message.from_user.id
#     )

# @dp.message_handler(text="Berilgan elonni o'chirish",state=userposition.employeesettingsposition)
# async def deleteoffer(message : types.Message,state:FSMContext):
#     await message.answer("O'chirmoqchi bo'lgan e'loningiz idsini kiriting.\n Idni 📝 Men bergan elonlar bo'limidan olishingiz mumkun!")
#     try:
#         if await db.delete_emp_offer(id=message.text,telegram_id=message.from_user.id):
#             await message.answer("E'loningiz o'chirildi")
#         else:
#             await message.answer("Siz faqat o'z eloningizni o'chira olasiz")
#     except asyncpg.exceptions.UniqueViolationError:
#             pass

# @dp.message_handler(text="Men haqimdagi malumotlar",state=userposition.employeesettingsposition)
# async def info_about_me(message : types.Message,state:FSMContext):
#     try:
#         emp_inf = await db.call_employee_information(
#             telegramid=message.from_user.id
#         )
#         ism = emp_inf[1]
#         familiya = emp_inf[2]
#         raqam = emp_inf[3]
#         info = "Shaxsiy malumotlaringiz. \n"
#         info += f"Ismingiz : {ism}\n"
#         info += f"Familiyangiz : {familiya} \n"
#         info += f"Telefon raqamingiz : {raqam}"
#         await message.answer(info)
#     except asyncpg.exceptions.UniqueViolationError:
#             pass


###sozlamalar bo'limidan Bosh oynaga qaytish
# @dp.message_handler(text="🏠 Bosh menyuga qaytish",state=userposition.employeesettingsposition)
# async def backtobasefromsettings(message : types.Message,state=FSMContext):
#     await message.answer("Asosiy oyna",reply_markup=base_menu)
#     await userposition.baseposition.set()

