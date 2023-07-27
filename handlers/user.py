from aiogram import types

from creat_bot import bot
from keyboards.keyboard import keyboard
from utils.config import ADMIN_ID


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}!', reply_markup=keyboard)
    await bot.send_message(ADMIN_ID, 'Новый пользовтель использует бота')


async def command_consult(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Привет, {message.from_user.username}! \nДля получения консультации, отправьте нам Ваш контакт: /send_contact')


async def get_contact(message: types.Message):
    await bot.send_message(ADMIN_ID, f"Пользователь отправил контакт для консультации: {message.contact}")
    await bot.send_message(message.from_user.id, f"Вы заскамлены")


async def command_info(message: types.Message):
    await bot.send_message(message.from_user.id, f'🧚🏻‍♂️Топ 5 фактов о нашем салоне красоты:'
                                                 f'\n-Нам доверяют больше 10000 клиентов'
                                                 f'\n- У нас 11 видов услуг,что позволяет экономить время наших клиентов на дорогу и поиск мастеров'
                                                 f'\n-Мы работаем исключительно на качественных материалах '
                                                 f'\n-У нас соблазнительные цены и бонусы для наших любимых клиентов'
                                                 f'\n-У нас всегда найдется время, чтобы сделать вас красивыми '
                                                 f'\n"Твое место силы" - это место, в котором, благодаря,уютному интерьеру, прекрасному персоналу, вкусной чашечки чая/кофе с разнообразными угощениями,аромату свечей и качественным услугам. '
                                                 f'\nТы не только преобразишься, но и наполнишься силами🌸❤️',
                           reply_markup=keyboard)


async def command_route(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'За остановкой Ипподром, спускаемся по лестнице к дому, проходим магазин "Морошка", поворачиваем направо и проходим арку, идем прямо, по правой стороне будет студия танцев "Pink", прям возле нее находится наш салон красоты "Твое место силы".'
                           f'Заходи,наводи красоту и расслабляйся🫶🏻🧚🏻‍♂️')
    await bot.send_photo(message.from_user.id, photo='https://fotohosting.su/image/Vzqvg',
                         reply_markup=keyboard)


async def command_services(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! Здесь будут наши услуги!',
                           reply_markup=keyboard)


async def command_stock(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! Здесь будут наши акции!',
                           reply_markup=keyboard)
