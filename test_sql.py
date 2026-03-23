import sqlite3

con = sqlite3.connect('db.sqlite')

# Создаём специальный объект cursor для работы с БД.
# Вся дальнейшая работа будет вестись через методы этого объекта.
cur = con.cursor()

# Готовим SQL-запросы.
# Для читаемости запрос обрамлён в тройные кавычки и разбит построчно.
query_1 = '''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    birth_year INTEGER
);
'''
query_2 = '''
CREATE TABLE IF NOT EXISTS video_products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    product_type TEXT,
    release_year INTEGER
);
'''

# Применяем запросы.
cur.execute(query_1)
cur.execute(query_2)

...

directors = [
    (1, 'Текс Эйвери', 1908),
    (2, 'Роберт Земекис', 1952),
    (3, 'Джерри Чиникей', 1912),
]
video_products = [
    (2, 'Кто подставил кролика Роджера', 'Фильм', 1988),
    (3, 'Безумные мелодии Луни Тюнз', 'Мультсериал', 1931),
    (4, 'Розовая пантера: Контроль за вредителями', 'Мультфильм', 1969)
]

cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)
cur.executemany('INSERT INTO video_products VALUES(?, ?, ?, ?);', video_products)

con.commit()
con.close()