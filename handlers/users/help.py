from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(),state=None)
async def bot_help(message: types.Message):
    text = ("Bu botda siz namoz haqida ma'lumotlarni va vaqtlarini, islomiy kitoblarni, sahoblar haqida ma'lumotlarni, ozingizga yaqin masjidlarni va qisqa Duo va zikirlarni olishingiz mumkin ")
    
    await message.answer((text))
