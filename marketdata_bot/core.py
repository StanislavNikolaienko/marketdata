import finnhub
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from decouple import AutoConfig

from marketdata_bot.utils.constants import BASE_DIR, SECRETS_DIR

secret_config = AutoConfig(search_path=BASE_DIR.joinpath(SECRETS_DIR))

TELEGRAM_BOT_TOKEN = secret_config("TELEGRAM_BOT_TOKEN")
FINNHUB_API_KEY = secret_config("FINNHUB_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
dp = Dispatcher(bot)
