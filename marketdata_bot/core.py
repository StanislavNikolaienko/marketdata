from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from decouple import AutoConfig

from marketdata_bot.utils.constants import BASE_DIR, CONFIG_DIR

config = AutoConfig(search_path=BASE_DIR.joinpath(CONFIG_DIR))


TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
