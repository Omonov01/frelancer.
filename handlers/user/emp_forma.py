import asyncpg
from aiogram import types
from loader import dp,db
from aiogram.dispatcher import FSMContext
from states.forma import emppersonaldata
from states.forma import userposition
from keyboards.default.additional_buttons import phonenumber,yes_no
from keyboards.default.base_window import base_menu
from keyboards.default.employee_window import employee_menu


###ismni olish
@dp.message_handler(state=emppersonaldata.empname)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )

    await message.answer("Familiyangizni kiriting!!!")
    await emppersonaldata.empfullname.set()

###personaldata familiyani kiriting
@dp.message_handler(state=emppersonaldata.empfullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"fullname":fullname}
    )
    await message.answer("Telefon raqamingizni  kiriting!!!",reply_markup=phonenumber)
    await emppersonaldata.empnumber.set()

###Personaldata nomerni olish
@dp.message_handler(content_types=types.ContentType.CONTACT,state=emppersonaldata.empnumber)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.contact["phone_number"]
    await state.update_data(
        {"phone": phone}
    )

    await message.answer("Malumotlaringiz to'gri kiritilganmi?")
    data = await state.get_data()
    name = data.get("name")
    fullname = data.get("fullname")
    phone = data.get("phone")
   

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Familiyangiz - {fullname}\n"
    msg += f"Telefon: - {phone}\n"

    await message.answer(msg)
    await message.answer("Malumotlaringiz To'g'ri kiritilganmi?",reply_markup=yes_no)
    await emppersonaldata.empyes_no.set()   

@dp.message_handler(state=emppersonaldata.empyes_no)
async def funcyes_no(message : types.Message, state : FSMContext):
    data = await state.get_data()
    ism = data.get("name")
    familiya = data.get("fullname")
    raqam = data.get("phone")
    if message.text == "Ha":
        try:
            await db.add_employee_db(
                name=ism,
                fullname=familiya,
                number=raqam,
                telegram_id=message.from_user.id
            )
        except asyncpg.exceptions.UniqueViolationError:
            pass
        await message.answer("Barcha malumotlaringiz muvaffaqqiyatli saqlandi.Siz shaxsiy oynangizda oz elonlarinigizni nazorat qilishingiz mumkin.!!!",reply_markup=employee_menu)
        await userposition.employeeposition.set()
    elif message.text == "Yo'q":
        await message.answer("Malumotlaringizni boshqattan kiriting",reply_markup=base_menu)
        await userposition.baseposition.set()
