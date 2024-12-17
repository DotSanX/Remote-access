from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram.filters import Command

router = Router()

def main_menu():
    
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Тест")  ]], resize_keyboard=True, input_field_placeholder="Выберите действие")
    return keyboard
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет!", reply_markup=main_menu())


    


