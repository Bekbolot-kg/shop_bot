import sqlite3
from pathlib import Path


def init_db():
    """Для создание и соединение с базой данных sqlite"""
    global db, cursor
    NAME_DB = 'my_bot.db'
    PATH_DB = Path(__file__).parent.parent
    db = sqlite3.connect(PATH_DB/NAME_DB)
    cursor = db.cursor()

def create_table():
    """Для создание таблицу"""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
        survey_id INTEGER PRIMARY KEY,
        type_product TEXT,
        name TEXT,
        price TEXT,
        photo TEXT)
    ''')
    db.commit()


def insert_product():
    """Для добавление данных в БД"""
    cursor.execute('''
    INSERT INTO products(type_product, name, price, photo)
    VALUES ('Наушники', 'AirPods', '1000 сом', 'image_products/photo_2.jpg'),
    ('Наушники', 'AirDots', '1200 сом', 'image_products/photo_1.jpg'),
    ('Power Bank', 'Power Bank', '650 - 1800 сом', 'image_products/photo_7.jpg'),
    ('Power Bank', 'Power Bank', '700 - 1500 сом', 'image_products/photo_5.jpg'),
    ('Power Bank', 'Power Bank', '650 - 1500 сом', 'image_products/photo_6.jpg'),
    ('Smart часы', 'Smart часы', '1500', 'image_products/photo_4.jpg'),
    ('Принтеры', 'Мини принтер', '1500', 'image_products/photo_3.jpg')''')
    db.commit()

def delete_product():
    """Для удаление всех данных"""
    cursor.execute('''DROP TABLE IF EXISTS products''')
    db.commit()

def get_product():
    """Для вывода данных в экран"""
    data = cursor.execute("""SELECT * FROM products""")
    return data.fetchall()

