from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.keyboard = [
    [types.KeyboardButton('Button 1'), types.KeyboardButton('Button 2')],
    [types.KeyboardButton('Button 3'), types.KeyboardButton('Button 4')]
]
