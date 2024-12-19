from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import FSInputFile

import os
import pyautogui
import requests

router = Router()

#Функции
def main_menu():
    
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="/screen", ),KeyboardButton(text="/ip", )]], resize_keyboard=True, input_field_placeholder="Выберите действие")

    return keyboard
def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screen.png')
def get_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        ip_address = response.json().get("ip")
        return f"🌐 Текущий IP-адрес: {ip_address}"
    except requests.RequestException:
        return "❌ Не удалось получить IP-адрес."



#Обработчики
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

@router.message(Command("ip"))
async def handle_ip_address(message: types.Message):
    ip_address = get_ip_address()
    await message.reply(ip_address)


    


