from aiogram import types

from marketdata_bot.core import dp
from marketdata_bot.def_func.numb_of_candles import number_of_candles


@dp.message_handler(content_types=["text"])
async def get_candles(msg):
    arg = msg.text.split(" ")
    await msg.answer(number_of_candles((str.upper(arg[0])), (int(arg[1]))))
