# -*- coding: cp1251 -*-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


lin1 = [InlineKeyboardButton(text='��������', callback_data='bioil'), InlineKeyboardButton(text='������', callback_data='fizika'),\
        InlineKeyboardButton(text='�������', callback_data='history'), InlineKeyboardButton(text='�����', callback_data='chemical')]
lin2 = [InlineKeyboardButton(text='����������', callback_data='math'), InlineKeyboardButton(text='������� ����', callback_data='russian'),\
        InlineKeyboardButton(text='�����������', callback_data='it')]
lin3 = [InlineKeyboardButton(text='����������', callback_data='litr'), InlineKeyboardButton(text='���������� ����', callback_data='angl'),\
        InlineKeyboardButton(text='��������������', callback_data='obsh')]

inkb = InlineKeyboardMarkup(row_width=4).row(*lin1).row(*lin2).row(*lin3)