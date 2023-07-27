import asyncio

from creat_bot import dp, bot
from handlers.setup import setup_handlers


async def on_startup(_):
    print('Бот вышел в он-лайн')


async def main() -> None:
    setup_handlers(dp)
    await dp.start_polling(bot,
                           on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())
