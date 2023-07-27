from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton(text='/info')
button_2 = KeyboardButton(text='/route')
button_3 = KeyboardButton(text='/services')
button_4 = KeyboardButton(text='/stock')
button_5 = KeyboardButton(text='/consultation')
button_6 = KeyboardButton(text='/send_contact', request_contact=True)

keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_1, button_2, button_3],
    [button_4, button_5, button_6]
], resize_keyboard=True, one_time_keyboard=True)
