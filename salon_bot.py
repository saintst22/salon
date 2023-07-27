from aiogram import executor
from creat_bot import dp
import handlers


async def on_startup(_):
    print('Бот вышел в он-лайн')


# from handlers import start
# start.register_handlers_start(dp)


executor.start_polling(dp,
                       skip_updates=True,
                       on_startup=on_startup)
