# -*- coding: cp1251 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#������������� ������
b1 = KeyboardButton('/��������')
b2 = KeyboardButton('/help')


kb_polz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_polz.add(b2).add(b1)