from aiogram import types

from marketdata_bot.core import dp, number_of_candles


@dp.message_handler(content_types=["text"])
async def get_candles(msg):
    arg = msg.text.split(" ")
    x, y = arg[0], arg[1]
    await msg.answer(number_of_candles((str.upper(x)), (int(y))))
