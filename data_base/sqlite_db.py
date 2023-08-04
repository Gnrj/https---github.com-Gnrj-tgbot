# -*- coding: cp1251 -*-
import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('lom_school.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    #словарь предметов
    table = {'inf': 'inf',
             'math': 'math',
             'rus': 'rus',
             'hist': 'hist',
             'bio': 'bio',
             'fiz': 'fiz',
             'lit': 'lit',
             'angl': 'angl',
             'chemic': 'chem',
             'obsh': 'obsh'}
    for key in table:
        base.execute('CREATE TABLE IF NOT EXISTS {}(img TEXT, name TEXT PRIMARY KEY, prepod TEXT, description TEXT)'.format(table[key]))
        base.commit()

