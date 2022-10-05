from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Boshlang"),
            types.BotCommand("help", "Bot haqida"),
            types.BotCommand("menu", "Asosiy menu"),
            # types.BotCommand("admins", "Adminlar"),
        ]
    )
