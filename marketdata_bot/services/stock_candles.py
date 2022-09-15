import datetime

from marketdata_bot.core import finnhub_client
from marketdata_bot.utils.constants import FINNHUB_MAX_DAYS, ONE_DAY_TIMESTAMP


def receive_candles(ticker, days):
    if days <= 0:
        return []
    datetime_ends = datetime.datetime.now()
    timestamp_datetime_ends = int(datetime.datetime.timestamp(datetime_ends))
    timestamp_datetime_start = (
        timestamp_datetime_ends - ONE_DAY_TIMESTAMP * FINNHUB_MAX_DAYS
    )

    response_candle_dict = finnhub_client.stock_candles(
        ticker, "D", timestamp_datetime_start, timestamp_datetime_ends
    )
    close_c = response_candle_dict.get("c")
    high_c = response_candle_dict.get("h")
    low_c = response_candle_dict.get("l")
    open_c = response_candle_dict.get("o")
    box = [items for items in zip(open_c, high_c, low_c, close_c)]
    return box[: -days - 1 : -1]
