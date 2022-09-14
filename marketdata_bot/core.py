import finnhub
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from decouple import AutoConfig
from pytz import timezone

from marketdata_bot.utils.constants import BASE_DIR, CONFIG_DIR

config = AutoConfig(search_path=BASE_DIR.joinpath(CONFIG_DIR))

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
FINNHUB_API_KEY = config("FINNHUB_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
dp = Dispatcher(bot)


localtz = timezone("US/Eastern")
