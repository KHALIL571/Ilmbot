import sqlite3

from aiogram import executor

import data,middlewares,handlers,keyboards
from loader import dp, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands



async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    try:
        db.create_table_users()
    except Exception and sqlite3.Error as sq:
        print()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)




