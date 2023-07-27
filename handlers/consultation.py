from creat_bot import bot, dp
from aiogram import types, Dispatcher
from keyboards.keyboard import keyboard, send_contact
from aiogram import F


@dp.message_handler(commands=['consultation'])
async def command_start(message: types.Message):
    my_id = 5375461682
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! \nДля получения консультации, отправьте нам Ваш контакт: ',
                           reply_markup=send_contact)



@dp.message(F.contact)
await message.forward(my_id)