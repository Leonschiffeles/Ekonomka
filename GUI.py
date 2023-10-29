import sqlite3
import datetime
def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))
def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

with sqlite3.connect('bd/baza.db') as bd:
    cursor = bd.cursor()
    zapros = """ CREATE TABLE  Оплата(id INTEGER, Сумма REAL, Дата_платежа INTEGER, Тип платежа INTEGER)"""

    cursor.execute(zapros)
    bd.commit()
