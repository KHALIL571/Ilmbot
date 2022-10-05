from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from data.config import ADMINS
from loader import dp, bot, db
from keyboards.default.adminKeyboard import adminMenu


@dp.message_handler(Command("admins"),user_id=ADMINS)
async def show_menu(message: Message):
    await message.answer("Admin menu",reply_markup=adminMenu)

@dp.message_handler(text="All users", user_id=ADMINS)
async def get_all_users(message: Message):
    users = f"XAMMA USERSLAR:{db.select_all_users()}"
#   def show():
#       msg = ""
#       for i, us in enumerate(db.select_one()):
#           msg += f"{i + 1}.<b>{us[1]}</b>({us[0]})\n"
#       return msg
#    await bot.send_message(chat_id=message.from_user.id,text=show())
    await bot.send_message(chat_id=message.from_user.id, text=users)


@dp.message_handler(text="Follow namaz", user_id=ADMINS)
async def count_obuna(message: Message):
    def count():
        msg = ""
        i = ""
        for i, us in enumerate(db.count_obuna()):
            msg += f"""{i+1}.<b>{us[1]}</b>({us[2]})\n"""
            i += i
        return f"{msg}\n\nObunachilar soni {i}"
    await bot.send_message(chat_id=message.from_user.id, text=count())

from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import types

from aiogram_broadcaster import MessageBroadcaster

@dp.message_handler(text='Broadcast', user_id=ADMINS)
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Xammaga jonatish uchun(EHTIYOT BO\'LING):')
    await state.set_state('broadcast_text')

@dp.message_handler(state='broadcast_text', content_types=types.ContentTypes.ANY)
async def start_broadcast(msg: Message, state: FSMContext):
    await state.finish()
    users = db.select_all_users2()
    for user in users:
        await MessageBroadcaster(user[0], msg).run()



# @dp.message_handler(text="/cleandb", user_id=ADMINS)
# async def clean_all_users(message: types.Message):
#     db.delete_users()
#     await message.answer("Baza tozalandi!")
