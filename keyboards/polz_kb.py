# -*- coding: cp1251 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#инициализация кнопок
b1 = KeyboardButton('/Предметы')
b2 = KeyboardButton('/help')


kb_polz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_polz.add(b2).add(b1)