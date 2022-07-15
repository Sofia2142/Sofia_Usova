from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_kb = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(KeyboardButton('Пн'), KeyboardButton('Вт'), KeyboardButton('Ср'), KeyboardButton('Чт'))\
    .row(KeyboardButton('Пт'), KeyboardButton('Сб'), KeyboardButton('Сегодня'), KeyboardButton('Завтра'))
