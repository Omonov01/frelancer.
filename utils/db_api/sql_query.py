category_db = """ CREATE TABLE IF NOT EXISTS category_db(
                   category_id SERIAL PRIMARY KEY,
                   category VARCHAR(255) NOT NULL);
                   INSERT INTO category_db(category_id,category)
                   VALUES
                   (1,'IT/DASTURLASH'),
                   (2,'SMM/KOPIRAYTING/TARGETING'),
                   (3,'DIZAYN'),
                   (4,'SEO/TRAFIK'),
                   (5,'TARJIMON'),
                   (6,'AUDIO/VIDEO/MONTAJ'),
                   (7,'BUXGATERIYA/FINANCE'),
                   (8,'OPERATOR/LOGISTIKA/OFFICE_MANAGER'),
                   (9,'SOTUV/MARKETING/HR'),
                   (10,'USTOZ')
                   """

freelanser_db = """ CREATE TABLE IF NOT EXISTS freelancer_db(
                    frelancer_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    fullname VARCHAR(255) NOT NULL,
                    technology VARCHAR(255) NOT NULL,
                    number VARCHAR(255) NOT NULL,
                    telegram_id BIGINT NOT NULL UNIQUE,
                    fk_category_id BIGINT REFERENCES category_db(category_id)
                    );
                    """


employee_db = """ CREATE TABLE IF NOT EXISTS employee_db(
                    employee_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    fullname VARCHAR(255) NOT NULL,
                    number VARCHAR(255) NOT NULL,
                    telegram_id BIGINT NOT NULL UNIQUE
                    );
                    """



post_db = """ CREATE TABLE IF NOT EXISTS post_db(
                post_id SERIAL PRIMARY KEY,
                project_name VARCHAR(255),
                project_description VARCHAR(255),
                project_cost VARCHAR(255),
                project_link VARCHAR(255),
                project_technology VARCHAR(255),
                fk_category_post_id BIGINT REFERENCES category_db(category_id),
                fk_employee_telegram_id BIGINT REFERENCES employee_db(telegram_id)
                );
                """




big_employee = """  CREATE TABLE IF NOT EXISTS big_employee(
                    id SERIAL PRIMARY KEY,
                    telegram_id BIGINT NOT NULL UNIQUE
                    );
"""


