# -*- coding: cp1251 -*-
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_polz, inkb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
"""/start"""
async def start(message: types.Message):
    text = 'Здравствуйте, я бот онлайн школы Lomonosov School, что вы хотите узнать?'
    await bot.send_message(message.from_user.id, text, reply_markup=kb_polz)

"""/Что_такое_Lomonosov_School?"""
async def lomsc(message: types.Message):
    text = 'Lomonosov School - это курсы подготовки к ЕГЭ, ДВИ, ОГЭ и олимпиадам. Занятия online с преподавателями, сотрудниками, выпускниками и студентами МГУ им. М.В. Ломоносова.'
    await bot.send_message(message.from_user.id, text = text, reply_markup=InlineKeyboardMarkup().\
                           add(InlineKeyboardButton(text = 'Наш сайт', url = 'https://lomonosov.school/')))
"""/Предметы"""
async def pred(message: types.Message):
    text = 'Выбери предмет'
    await bot.send_message(message.from_user.id, text=text, reply_markup=inkb)




"""Запуск хендлеров"""
def register_handlers_polz(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(lomsc, commands=['help'])
    dp.register_message_handler(pred, commands=['Предметы'])