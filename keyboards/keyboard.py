from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_1 = KeyboardButton('/info')
button_2 = KeyboardButton('/route')
button_3 = KeyboardButton('/services')
button_4 = KeyboardButton('/stock')
button_5 = KeyboardButton('/consultation')

button_6 = KeyboardButton('/Отправить свой номер телефона', request_contact=True)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(button_2, button_3).add(button_4, button_5).row(button_1)

send_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
send_contact.add(button_6)
