from aiogram import types

from loader import dp, bot, db
from aiogram.types import CallbackQuery



def bugun(region):

    if db.get_bugun(region):
        return (f""" 
    📍Mintaqa - {db.get_bugun(region)[0][12]}
<b>{db.get_bugun(region)[0][1]}</b> {db.get_bugun(region)[0][0]}<b>2022</b> - <b>{db.get_bugun(region)[0][3]}</b> {db.get_bugun(region)[0][4]} <b>1443</b>

    📆<i>{db.get_bugun(region)[0][5]}</i>
    
    🌌 Bomdod: <b>{db.get_bugun(region)[0][6]}</b>
    🌄 Quyosh: <b>{db.get_bugun(region)[0][7]}</b>
    🌇 Peshin: <b>{db.get_bugun(region)[0][8]}</b>
    🌆 Asr: <b>{db.get_bugun(region)[0][9]}</b>
    🏙 Shom: <b>{db.get_bugun(region)[0][10]}</b>
    🌃 Xufton: <b>{db.get_bugun(region)[0][11]}</b>
    """)
    else:
        pass


"""CALLBACK_QUERY_HANDLER"""

@dp.callback_query_handler(text='bugun:toshkent')
async def inline_today_toshkent(call: CallbackQuery):
    # await call.message.delete()
    # await call.message.answer('bugungi namozlar',reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Toshkent"), parse_mode="html")#,reply_markup=types.ReplyKeyboardRemove()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:andijon')
async def inline_today_andijon(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Andijon"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:buxoro')
async def inline_today_buxoro(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Buxoro"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:guliston')
async def inline_today_guliston(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Guliston"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:samarqand')
async def inline_today_sqmqrqand(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Samarqand"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:namangan')
async def inline_today_namangan(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Namangan"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:navoi')
async def inline_today_navoi(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Navoiy"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:jizzax')
async def inline_today_jizzax(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Jizzax"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:nukus')
async def inline_today_nukus(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Nukus"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:qarshi')
async def inline_today_qarshi(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Qarshi"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:qoqon')
async def inline_today_qoqon(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Qo'qon"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:xiva')
async def inline_today_xiva(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Xiva"), parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:margilon')
async def inline_today_margilon(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Marg'ilon"), parse_mode="html")
    await call.answer(cache_time=60)

