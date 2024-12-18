from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import FSInputFile

import os
import pyautogui

router = Router()
def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screen.png')

def main_menu():
    
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="/screen", )  ]], resize_keyboard=True, input_field_placeholder="Выберите действие")
    return keyboard

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет!", reply_markup=main_menu())


@router.message(Command("screen"))
async def handle_screenshot(message: types.Message):
    try:
        screenshot()
        # Используем FSInputFile для передачи файла
        photo = FSInputFile('screen.png')
        await message.reply_photo(photo, caption="📸 Скриншот экрана.")
        os.remove('screen.png')
    except Exception as e:
        await message.reply(f"❌ Ошибка при создании скриншота: {e}", parse_mode=None)


    


