# -*- coding: cp1251 -*-
from aiogram import executor
from create_bot import dp
from handlers import polz

async def on_startup(_):
    print('Bot online')



polz.register_handlers_polz(dp)






executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
