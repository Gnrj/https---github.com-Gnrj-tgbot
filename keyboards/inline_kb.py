# -*- coding: cp1251 -*-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


lin1 = [InlineKeyboardButton(text='Биология', callback_data='bioil'), InlineKeyboardButton(text='Физика', callback_data='fizika'),\
        InlineKeyboardButton(text='История', callback_data='history'), InlineKeyboardButton(text='Химия', callback_data='chemical')]
lin2 = [InlineKeyboardButton(text='Математика', callback_data='math'), InlineKeyboardButton(text='Русский язык', callback_data='russian'),\
        InlineKeyboardButton(text='Информатика', callback_data='it')]
lin3 = [InlineKeyboardButton(text='Литература', callback_data='litr'), InlineKeyboardButton(text='Английский язык', callback_data='angl'),\
        InlineKeyboardButton(text='Обществознание', callback_data='obsh')]

inkb = InlineKeyboardMarkup(row_width=4).row(*lin1).row(*lin2).row(*lin3)