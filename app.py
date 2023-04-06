from aiogram import executor
from loader import dp,db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    ### Database connection
    await db.create()
    # print("Railwayga ulandik")
    # ### Bazalarni yaratish
    # await db.employee_db()
    # print("employee_db yaratildi")
    # await db.category_db()
    # print("category_db yaratildi. Keyingi safar uchurib quy")
    # await db.freelancer_db()
    # print("freelancer_db yaratildi")
    # await db.post_db()
    # print("post_db yaratildi")
    # await db.big_employee()
    # print("big_employee yaratildi")
    # print("Barcha bazalar yasaldi")
    #Birlamchi komandalar (/star va /help)
    
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
    