import asyncpg
from aiogram import types
from loader import dp,db
from aiogram.dispatcher import FSMContext
from states.forma import personaldata
from states.forma import userposition
from keyboards.default.additional_buttons import phonenumber,yes_no
from keyboards.default.category import categoryMenu
from keyboards.default.base_window import base_menu
from keyboards.default.frilanser_window import frilans_menu

###ismni olish
@dp.message_handler(state=personaldata.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )

    await message.answer("Familiyangizni kiriting!!!")
    await personaldata.fullname.set()

###personaldata familiyani kiriting
@dp.message_handler(state=personaldata.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"fullname":fullname}
    )
    await message.answer("Telefon raqamingizni  kiriting!!!",reply_markup=phonenumber)
    await personaldata.number.set()

###Personaldata nomerni olish
@dp.message_handler(content_types=types.ContentType.CONTACT,state=personaldata.number)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.contact["phone_number"]
    await state.update_data(
        {"phone": phone}
    )

    await message.answer("Quyidagilardan qaysi sohada faoliyat yuritasiz.Sohangizni belgilagandan keyin Tayyor tugmasini bosing!",reply_markup=categoryMenu)
    await personaldata.categoriya.set()

###personaldata categoriyani olish
@dp.message_handler(state=personaldata.categoriya)
async def answer_category(message : types.Message, state: FSMContext):
    categoriya = message.text
    category_list = []
    if message.text != "TAYYOR":
        category_list.append(categoriya)
        # print(category_list)
        for a in category_list:
            await state.update_data(
            {"categoriya":a}
            )
    elif message.text == "TAYYOR":
        await message.answer("Siz foydalanadigan texnologiyalarni kiriting.\n 200 ta belgidan oshirmang.")
        await personaldata.technologies.set()
   
    

# Ma`lumotlarni qayta o'qiymiz
@dp.message_handler(state=personaldata.technologies)
async def answer_technology(message : types.Message , state: FSMContext):
   
    technology = message.text
    await state.update_data(
        {"technology":technology}
    )
    data = await state.get_data()
    name = data.get("name")
    fullname = data.get("fullname")
    phone = data.get("phone")
    category = data.get("categoriya")
    technology = data.get("technology")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Familiyangiz - {fullname}\n"
    msg += f"Telefon: - {phone}\n"
    msg += f"Kategoriyangiz {category}\n"
    msg += f"Texnologiyalar {technology}\n"
    await message.answer(msg)
    await message.answer("Malumotlaringiz To'g'ri kiritilganmi?",reply_markup=yes_no)
    await personaldata.yes_no.set()   

@dp.message_handler(state=personaldata.yes_no)
async def funcyes_no(message : types.Message, state : FSMContext):
    data = await state.get_data()
    ism = data.get("name")
    familiya = data.get("fullname")
    raqam = data.get("phone")
    kategoriya = data.get("categoriya")
    texnologiya = data.get("technology")
    if message.text == "Ha":
        try:
            category_id = await db.call_category_id(
                category_name=kategoriya
            )
            await db.add_freelancer_db(
                name=ism,
                fullname=familiya,
                number=raqam,
                technology=texnologiya,
                telegram_id=message.from_user.id,
                fk_category_id=category_id
            )
        except asyncpg.exceptions.UniqueViolationError:
            pass
        await message.answer("Barcha malumotlaringiz muvaffaqqiyatli saqlandi.Sizga loyiq ish topilishi bilan sizga murojaat qilamiz!!!",reply_markup=frilans_menu)
        await userposition.frilansposition.set()
    elif message.text == "Yo'q":
        await message.answer("Malumotlaringizni boshqattan kiriting",reply_markup=base_menu)
        await userposition.baseposition.set()
