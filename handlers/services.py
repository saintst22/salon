from creat_bot import bot, dp
from aiogram import types, Dispatcher
from keyboards.keyboard import keyboard


@dp.message_handler(commands=['services'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! Здесь будут наши услуги!', reply_markup=keyboard)
