from marketdata_bot.def_func.numb_of_candles import number_of_candles


def test_candle_numb():
    arg = ["AI", 5]
    assert len(number_of_candles(arg[0], arg[1])[0]) == 4
