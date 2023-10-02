import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from movies import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token='6515138891:AAGH1SBp-gJ-o6Xs0sqbIq-Ke4YQIWsQp3w')
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Top 250 movies'),
            types.KeyboardButton(text='Top 250 Tv Shows'),
            types.KeyboardButton(text='Popular movies now'),
            types.KeyboardButton(text='Popular Tv Shows now'),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Make your choice"
    )
    await message.answer('Choose a button', reply_markup=keyboard)


@dp.message(F.text == "Top 250 movies")
async def movies_250(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Top Random'),
            types.KeyboardButton(text='Back'),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Random one?'
    )
    if len(top_250_movies()) > 4095:
        for x in range(0, len(top_250_movies()), 4095):
            await message.answer(top_250_movies()[x:x + 4095], reply_markup=keyboard)
    else:
        await message.answer(top_250_movies(), reply_markup=keyboard)


@dp.message(F.text == "Top Random")
async def random_movie(message: types.Message):
    await message.answer(random_top_250_movie())


@dp.message(F.text == "Top 250 Tv Shows")
async def tv_show_250(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='TV Random'),
            types.KeyboardButton(text='Back'),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Random one?'
    )
    if len(top_250_tv_shows()) > 4095:
        for x in range(0, len(top_250_tv_shows()), 4095):
            await message.answer(top_250_tv_shows()[x:x + 4095], reply_markup=keyboard)
    else:
        await message.answer(top_250_tv_shows(), reply_markup=keyboard)


@dp.message(F.text == "TV Random")
async def random_movie(message: types.Message):
    await message.answer(random_top_250_tv_shows())


@dp.message(F.text == "Popular movies now")
async def popular_100_movie(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Popular Random'),
            types.KeyboardButton(text='Back'),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Random one?'
    )
    if len(popular_100_movies()) > 4095:
        for x in range(0, len(popular_100_movies()), 4095):
            await message.answer(popular_100_movies()[x:x + 4095], reply_markup=keyboard)
    else:
        await message.answer(popular_100_movies(), reply_markup=keyboard)


@dp.message(F.text == "Popular Random")
async def random_movie(message: types.Message):
    await message.answer(random_popular_100_movie())


@dp.message(F.text == "Popular Tv Shows now")
async def popular_100_tv(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Popular TV Random'),
            types.KeyboardButton(text='Back'),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Random one?'
    )
    if len(popular_100_tv_shows()) > 4095:
        for x in range(0, len(popular_100_tv_shows()), 4095):
            await message.answer(popular_100_tv_shows()[x:x + 4095], reply_markup=keyboard)
    else:
        await message.answer(popular_100_tv_shows(), reply_markup=keyboard)


@dp.message(F.text == "Popular TV Random")
async def random_movie(message: types.Message):
    await message.answer(random_popular_100_tv_shows())


@dp.message(F.text == "Back")
async def random_movie(message: types.Message):
    await cmd_start(message)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
