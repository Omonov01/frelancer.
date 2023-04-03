##fetch butun ustunni qaytaradi
##fetchrow butun ustunni yagona qiymat qilib qaytaradi
##fetchval bitta qiymat qaytaradi
##execute malumotlar kiritish uchun ishlatiladi
from typing import Union
from utils.db_api.sql_query import employee_db,category_db,freelanser_db,post_db,big_employee
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user="postgres",
            port="5721",
            password="PaswHcvNR1o8Fk1Y1fHO",
            host="containers-us-west-160.railway.app",
            database="railway"
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def employee_db(self):
        await self.execute(employee_db, execute=True)

    async def category_db(self):
        await self.execute(category_db, execute=True)

    async def freelancer_db(self):
        await self.execute(freelanser_db, execute=True)

    async def post_db(self):
        await self.execute(post_db, execute=True)

    async def big_employee(self):
        await self.execute(big_employee, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())
    
    ### freelancer tablega malumotlarni kiritish
    async def add_freelancer_db(self,name,fullname,technology,number,telegram_id,fk_category_id):
        sql = "INSERT INTO freelancer_db (name,fullname,technology,number,telegram_id,fk_category_id) VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql,name,fullname,technology,number,telegram_id,fk_category_id,fetchrow=True)
    
    ### big_employee ga telegram_id kiritish
    async def add_big_employee(self,telegram_id):
        sql = "INSERT INTO big_employee(telegram_id) VALUES($1) returning *"
        return await self.execute(sql,telegram_id,fetchrow=True)
    
    ### employee tablega malumot kirgizish
    async def add_employee_db(self,name,fullname,number,telegram_id):
        sql = "INSERT INTO employee_db(name,fullname,number,telegram_id) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql,name,fullname,number,telegram_id,fetchrow=True)
    
    ### post tablega malumot kirgizish
    async def add_post_db(self,project_name,project_description,project_cost,project_link,project_technology,fk_category_post_id,fk_employee_telegram_id):
        sql = "INSERT INTO post_db(project_name,project_description,project_cost,project_link,project_technology,fk_category_post_id,fk_employee_telegram_id) VALUES($1, $2, $3, $4, $5, $6, $7) returning *"
        return await self.execute(sql,project_name,project_description,project_cost,project_link,project_technology,fk_category_post_id,fk_employee_telegram_id,fetchrow=True)
    
    ### freelancer kategoriyadan malumotlarni telegram idni chaqirib olish
    async def call_freelancer_id(self,telegramid):
        sql = "SELECT telegram_id FROM freelancer_db WHERE freelancer_db.telegram_id = $1"
        return await self.execute(sql,telegramid,fetchval=True)
    
    ### categoriyaga categoriya nomini berib undan idni qaytarib oladi
    async def call_category_id(self,category_name):
        sql = "SELECT category_id FROM category_db WHERE category_db.category = $1"
        return await self.execute(sql,category_name,fetchval=True)
    
    ### employee kategoriyadan malumotlarni telegram idni chaqirib olish
    async def call_employee_id(self,telegramid):
        sql = "SELECT telegram_id FROM employee_db WHERE employee_db.telegram_id = $1"
        return await self.execute(sql,telegramid,fetchval=True)
    
    ### employee kategoriyadan malumotlarni telegram idni chaqirib olish
    async def call_element_from_post(self,telegramid):
        sql = "SELECT * FROM post_db WHERE post_db.fk_employee_telegram_id = $1"
        return await self.execute(sql,telegramid,fetch=True)
    
    ### freelancer uchun barcha elonlarni ko'rsatish
    async def call_element_from_post_to_fr(self):
        sql = "SELECT * FROM post_db"
        return await self.execute(sql,fetch=True)
    
    ###empdagi jami ruyxatdan o'tganlar soni
    async def call_count_emp(self):
        sql = "SELECT COUNT(*) FROM employee_db"
        return await self.execute(sql,fetchval=True)
    
    ###frdagi jami ustunlarni chaqiradi
    async def call_count_fr(self):
        sql = "SELECT COUNT(*)   FROM freelancer_db"
        return await self.execute(sql,fetchval=True)
    
    ###postdagi barcha elonlarni chiqarish
    async def call_count_post(self):
        sql = "SELECT COUNT(*) FROM post_db"
        return await self.execute(sql,fetchval=True)
    
    async def call_count_big_emp(self):
        sql = "SELECT COUNT(*) FROM big_employee"
        return await self.execute(sql,fetchval=True)
    
    # ### employeega o'zi haqidagi malumotlarni uzatish
    # async def call_employee_information(self,telegramid):
    #     sql = "SELECT * FROM employee_db WHERE employee_db.telegram_id = $1"
    #     return await self.execute(sql,telegramid,fetchrow=True)

    # ###employeni nameni o'zgartirish
    # async def update_emp_username(self, username, telegram_id):
    #     sql = "UPDATE employee_db SET name=$1 WHERE telegram_id=$2"
    #     return await self.execute(sql, username, telegram_id, execute=True)
    
    # ###employeni fullnameni o'zgartirish
    # async def update_emp_fullname(self, fullname, telegram_id):
    #     sql = "UPDATE employee_db SET fullname=$1 WHERE telegram_id=$2"
    #     return await self.execute(sql, fullname, telegram_id, execute=True)

    # ### employee bergan elonni uchirish
    # async def delete_emp_offer(self,id,telegram_id):
    #     sql = "DELETE post_db WHERE post_id=$1 AND post_db.fk_employee_telegram_id=$2"
    #     return await self.execute(sql,id,telegram_id, execute=True)
    