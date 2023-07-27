from creat_bot import bot, dp
from aiogram import types, Dispatcher
from keyboards.keyboard import keyboard


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    my_id = 5375461682
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}!', reply_markup=keyboard)
    await bot.send_message(my_id, 'Новый пользовтель использует бота')


# def register_handlers_start(dp : Dispatcher):
#     dp.register_message_handler(command_start, commands=['start'])
