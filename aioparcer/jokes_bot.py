from aiogram.utils import executor
from aiogram import Bot,Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import aioparcer.parcer


bot = Bot('5450561630:AAEHBe5whhvXWiH-xoeVFxh81P5u3PDFXmk')
dp = Dispatcher(bot)

list_of_jokes = []


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, могу рассказать анекдот', reply_markup=user_kb)


@dp.callback_query_handlers(text='joke_button')
async def get_joke(callback_query: types.CallbackQuery):
    global list_of_jokes
    if len(list_of_jokes) == 0:
        await bot.send_message(callback_query.from_user.id, 'В базе нет анекдотов', reply_markup=update_base_kb)
    else:
        await bot.answer_callback_query(callback_query.id, 'База данных успешно обновлена', show_alert=True)
        await bot.send_message(callback_query.from_user.id, 'Хочешь получить анекдот? Тогда жми кнопку ниже!',
                               reply_markup=user_kb)

@dp.callback_query_handlers(text='update_button')
async def update_base(callback_query: types.CallbackQuery):
    global list_of_jokes
    try:
        list_of_jokes = await aioparcer.percer.run_tasks()
        await bot.answer_callback_query(callback_query.id, 'База данных успешно обновлена', show_alert=True)
        await bot.send_message(callback_query.from_user.id, 'Хочешь получить анекдот? Тогда жми кнопку ниже!',
                               reply_markup=user_kb)
    except Exception as ex:
        await bot.send_message(callback_query.from_user.id, repr(ex), reply_markup=update_base_kb)


"""                  BUTTONS                   """
user_kb = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(InlineKeyboardButton('Получить анекдот', callback_data='joke_button'))

update_base_kb = InlineKeyboardMarkup(resize_keyboard=True)\
    .add(InlineKeyboardButton('Обновить базу данных анекдотов', callback_data='update_button'))

if __name__ == '__main__':
    print('Бот запущен')
    executor.start_polling(dp, skip_updates=True)