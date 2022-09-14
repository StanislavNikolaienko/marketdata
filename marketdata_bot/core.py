import datetime

import finnhub
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from decouple import AutoConfig
from pytz import timezone

from marketdata_bot.utils.constants import BASE_DIR, CONFIG_DIR

config = AutoConfig(search_path=BASE_DIR.joinpath(CONFIG_DIR))


TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

FINNHUB_API_KEY = config("FINNHUB_API_KEY")
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

localtz = timezone("US/Eastern")


def number_of_candles(t, d):
    if d <= 0:
        return []
    n = 174
    ticker = t
    datetime_ends = datetime.datetime.now()
    timestamp_datetime_ends = int(datetime.datetime.timestamp(datetime_ends))
    timestamp_datetime_start = timestamp_datetime_ends - 86400 * n

    response_candle_dict = finnhub_client.stock_candles(
        ticker, "D", timestamp_datetime_start, timestamp_datetime_ends
    )
    close = response_candle_dict.get("c")
    high = response_candle_dict.get("h")
    low = response_candle_dict.get("l")
    o_pen = response_candle_dict.get("o")
    box = [items for items in zip(o_pen, high, low, close)]
    return box[: -d - 1 : -1]
