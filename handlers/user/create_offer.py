import asyncpg
import asyncio
from aiogram import types
from loader import dp,db
from aiogram.dispatcher import FSMContext
from states.forma import project
from states.forma import userposition
from keyboards.default.additional_buttons import yes_no
from keyboards.default.employee_window import employee_menu
from keyboards.default.category import categoryMenu
from data.config import channel
###Forma ni ishga tushirish
@dp.message_handler(text="📥  Buyurtma yaratish", state=userposition.employeeposition)
async def beginform(message: types.Message, state: FSMContext):
    await message.answer("Assalom alaykum bu bo'limni to'ldirganingizdan biz siz yaratgan elonni shu sohada mutaxasislariga junatamiz!!")
    await message.answer("Loyihangiz nomini kiriting!!!")
    await project.projectname.set()

###project nomini olish
@dp.message_handler(state=project.projectname)
async def answer_name(message: types.Message, state: FSMContext):
    projectname = message.text

    await state.update_data(
        {"projectname": projectname}
    )

    await message.answer("Loyiha haqida malumot kiriting!!!")
    await project.projectdescription.set()

###project descriptionini olish
@dp.message_handler(state=project.projectdescription)
async def answer_descriotion(message: types.Message, state: FSMContext):
    projectdescription = message.text

    await state.update_data(
        {"projectdescription":projectdescription}
    )
    await message.answer("Siz bilan bog'lanish uchun malumot qoldiring \n Telefon raqamingiz yoki telegram akkauntingiz!!!")
    await project.projectlink.set()

###project linkini olish
@dp.message_handler(state=project.projectlink)
async def answer_link(message: types.Message, state: FSMContext):
    projectlink = message.text
    await state.update_data(
        {"projectlink": projectlink}
    )
    await message.answer("Project uchun ajratgan mablag'ingizni kiriting.\n Masalan 500.000 so'm")
    await project.projectcost.set()

###project costini olish
@dp.message_handler(state=project.projectcost)
async def answer_cost(message: types.Message, state: FSMContext):
    projectcost = message.text
    await state.update_data(
        {"projectcost": projectcost}
    )

    await message.answer("Projectingizni qurishda qaysi texnologiyalardan foydalanishni istaysiz? ")
    await project.projecttechnologies.set()

###project texnologiyasini olish
@dp.message_handler(state=project.projecttechnologies)
async def answer_technology(message: types.Message, state: FSMContext):
    projecttechnologies = message.text
    await state.update_data(
        {"projecttechnologies": projecttechnologies}
    )

    await message.answer("Bergan ish eloningiz qaysi soha hodimlariga ko'rsatilishini hoxlaysiz?",reply_markup=categoryMenu)
    await project.projectcategoriya.set()

### project categoriyasini olish va malumotlarni userga junatish
@dp.message_handler(state=project.projectcategoriya)
async def answer_category(message: types.Message,state : FSMContext):
    projectcategory = message.text
    await state.update_data(
        {"projectcategory":projectcategory}
    )
    await message.answer("Malumotlaringiz to'gri kiritilganmi?")
    data = await state.get_data()
    projectname = data.get("projectname")
    projectdescription = data.get("projectdescription")
    projectlink = data.get("projectlink")
    projectcost = data.get("projectcost")
    projecttechnologies = data.get("projecttechnologies")
    projectcategory = data.get("projectcategory")
   

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Project nomi - {projectname}\n"
    msg += f"Project haqida malumot - {projectdescription}\n"
    msg += f"Bog'lanish uchun manbaa - {projectlink}\n"
    msg += f"Project uchun ajratilgan mablag' - {projectcost}\n"
    msg += f"Projectda ishlatiladigan texnologiyalar - {projecttechnologies}\n"
    msg += f"Project categoriyasi: - {projectcategory}\n"

    await message.answer(msg)
    await message.answer("Malumotlaringiz To'g'ri kiritilganmi?",reply_markup=yes_no)
    await project.projectempyes_no.set()   

### project malumotlarini saqlash
@dp.message_handler(state=project.projectempyes_no)
async def funcyes_no(message : types.Message, state : FSMContext):
    data = await state.get_data()
    projectname = data.get("projectname")
    projectdescription = data.get("projectdescription")
    projectlink = data.get("projectlink")
    projectcost = data.get("projectcost")
    projecttechnologies = data.get("projecttechnologies")
    projectcategory = data.get("projectcategory")
    if message.text == "Ha":
        try:
            categoriya = await db.call_category_id(projectcategory)
            await db.add_post_db(
                project_name=projectname,
                project_description=projectdescription,
                project_link=projectlink,
                project_cost=projectcost,
                project_technology=projecttechnologies,
                fk_category_post_id=categoriya,
                fk_employee_telegram_id=message.from_user.id
            )

        except:
            pass
        

        await message.answer("Barcha malumotlaringiz muvaffaqqiyatli saqlandi.Siz shaxsiy oynangizda oz elonlarinigizni nazorat qilishingiz mumkin.!!!",reply_markup=employee_menu)
        await userposition.employeeposition.set()
    elif message.text == "Yo'q":
        await message.answer("Malumotlaringizni boshqattan kiriting",reply_markup=employee_menu)
        await userposition.employeeposition.set()
