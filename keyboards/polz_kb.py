# -*- coding: cp1251 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#������������� ������
b1 = KeyboardButton('/���_�����_Lomonosov_School?')
b2 = KeyboardButton('/��������')


kb_polz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_polz.add(b2).add(b1)