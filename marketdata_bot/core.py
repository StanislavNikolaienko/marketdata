from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from decouple import AutoConfig

from marketdata_bot.utils.constanse import BASE_DIR, CONFIG_DIR

config = AutoConfig(search_path=BASE_DIR.joinpath(CONFIG_DIR))


TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
