from creat_bot import bot, dp
from aiogram import types, Dispatcher
from keyboards.keyboard import keyboard


@dp.message_handler(commands=['route'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'За остановкой Ипподром, спускаемся по лестнице к дому, проходим магазин "Морошка", поворачиваем направо и проходим арку, идем прямо, по правой стороне будет студия танцев "Pink", прям возле нее находится наш салон красоты "Твое место силы".'
                                                 f'Заходи,наводи красоту и расслабляйся🫶🏻🧚🏻‍♂️')
    await bot.send_photo(message.from_user.id, photo='https://fotohosting.su/image/Vzqvg', reply_markup=keyboard)