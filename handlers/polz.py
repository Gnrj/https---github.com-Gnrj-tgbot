# -*- coding: cp1251 -*-
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_polz, inkb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
"""/start"""
async def start(message: types.Message):
    text = '������������, � ��� ������ ����� Lomonosov School, ��� �� ������ ������?'
    await bot.send_message(message.from_user.id, text, reply_markup=kb_polz)

"""/���_�����_Lomonosov_School?"""
async def lomsc(message: types.Message):
    text = 'Lomonosov School - ��� ����� ���������� � ���, ���, ��� � ����������. ������� online � ���������������, ������������, ������������ � ���������� ��� ��. �.�. ����������.'
    await bot.send_message(message.from_user.id, text = text, reply_markup=InlineKeyboardMarkup().\
                           add(InlineKeyboardButton(text = '��� ����', url = 'https://lomonosov.school/')))
"""/��������"""
async def pred(message: types.Message):
    text = '������ �������'
    await bot.send_message(message.from_user.id, text=text, reply_markup=inkb)




"""������ ���������"""
def register_handlers_polz(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(lomsc, commands=['help'])
    dp.register_message_handler(pred, commands=['��������'])