from marketdata_bot.core import dp
from marketdata_bot.services.stock_candles import receive_candles


@dp.message_handler(content_types=["text"])
async def get_candles(msg):
    inp_ticker, inp_days = msg.text.split(" ")
    await msg.answer(receive_candles(ticker=inp_ticker.upper(), days=int(inp_days)))
