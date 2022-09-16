from aiogram import types

from marketdata_bot.core import dp


@dp.message_handler(commands=["start"])
async def send_welcome(msg: types.Message):
    await msg.reply(
        "Hello World!\nI'm Candle bot.\nEnter a ticker and number of candles\nExamle: aapl 5"
    )
