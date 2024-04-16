!pip install aiogram
import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

API_TOKEN = '7112549885:AAH5uICZ8Yk2AI9zg4YamhrsxFdHp2QNQ6I'
BOT = Bot(token=API_TOKEN)
DP = Dispatcher()

@DP.message(Command('start'))
async def cmd_start(message: types.Message):
    button = types.KeyboardButton(text='Как пройти в библиотеку?')
    button2 = types.KeyboardButton(text='Сколько времени?')
    button3 = types.KeyboardButton(text='Сколько времени?')
    button4 = types.KeyboardButton(text='Сколько времени?')
    button5 = types.KeyboardButton(text='Сколько времени?')
    kb = types.ReplyKeyboardMarkup(keyboard=[[button], [button2], [button3], [button4], [button5]],
                                   one_time_keyboard=True)
    await message.answer('Привет!',
                         reply_markup=kb)

@DP.message(F.text == 'Как пройти в библиотеку?')
async def library(message: types.Message):
    await message.answer('Направо и налево.',
                         reply_markup=types.ReplyKeyboardRemove())
    kb = InlineKeyboardBuilder()
    button = types.InlineKeyboardButton(text='В меню',
                                        callback_data='В меню')
    kb.row(button)
    await message.answer('Желаете вернуться в меню?',
                         reply_markup=kb.as_markup())

@DP.callback_query(F.data == 'В меню')
async def cb_menu(callback: types.CallbackQuery):
    await callback.message.answer('А меню у меня пока нет :(')
    await callback.answer()

@DP.message()
async def cmd_any(message: types.Message):
    await message.answer(message.text)

async def main():
    await DP.start_polling(BOT)

import nest_asyncio
nest_asyncio.apply()

asyncio.run(main())
