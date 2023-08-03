# -*- coding: cp1251 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#инициализация кнопок
b1 = KeyboardButton('/Что_такое_Lomonosov_School?')
b2 = KeyboardButton('/Предметы')


kb_polz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_polz.add(b2).add(b1)