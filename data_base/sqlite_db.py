# -*- coding: cp1251 -*-
import sqlite3 as sq
from create_bot import dp, bot
from keyboards import kb_client
def sql_start():
    global base, cur
    base = sq.connect('lom_school.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS list(img TEXT, name TEXT PRIMARY KEY, prepod TEXT, description TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO list VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM list').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nПреподаватель: {ret[2]}\nОписание: {ret[-1]}', reply_markup=kb_client)

async def sql_read2():
    return cur.execute('SELECT * FROM list').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM list WHERE name == ?', (data,))
    base.commit()