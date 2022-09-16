from marketdata_bot.services.stock_candles import receive_candles


def test_candle_numb():
    ticker, days = ["AI", 5]
    assert len(receive_candles(ticker, days)[0]) == 4
