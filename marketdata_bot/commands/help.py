from aiogram import types

from marketdata_bot.core import dp


@dp.message_handler(commands=["help"])
async def send_welcome(msg: types.Message):
    await msg.reply("Hello World!\nI'm Candle bot.\nHow can I help you?!")
