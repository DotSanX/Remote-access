import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT_TOKEN

#инициализация
bot = Bot(token= BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

#хэндлер на команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    kb = [
        [types.KeyboardButton(text="1")],
        [types.KeyboardButton(text="2")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text="Hello!", reply_markup=keyboard)
