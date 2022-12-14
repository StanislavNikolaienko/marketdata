from aiogram.utils import executor
from commands.help import send_help
from commands.start import send_welcome

from marketdata_bot.core import dp

from commands.get_candles import get_candles  # isort:skip


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
