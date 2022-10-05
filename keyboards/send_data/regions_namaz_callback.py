import sqlite3
from aiogram.types import CallbackQuery, Message

from keyboards.inline.obuna_Inline import obunaInlineQar,obunaInlineNuk,obunaInlineQoq,obunaInlineNav,obunaInlineNam,obunaInlineT,obunaInlineS,obunaInlineG,obunaInlineB,obunaInlineA,obunaInlineX,obunaInlineM,obunaInlineJ,namozVaqtInlineT,namozVaqtInlineA,namozVaqtInlineB,namozVaqtInlineG,namozVaqtInlineJ,namozVaqtInlineM,namozVaqtInlineS,namozVaqtInlineX,namozVaqtInlineNuk,namozVaqtInlineNam,namozVaqtInlineNav,namozVaqtInlineQar,namozVaqtInlineQoq
from keyboards.inline.regions_Inline import regionInline

from loader import dp, db, bot
from data.config import ADMINS


#['toshkent', 'andijon','buxoro','guliston','samarqand','namangan','navoi','jizzax','nukus','qarshi','qoqon','xiva','margilon']
@dp.message_handler(text_contains='Namoz vaqtlari⏰')
async def show_menu(message: Message):
    await message.answer('Mintaqa❓',reply_markup=regionInline)

@dp.callback_query_handler(text='toshkent')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Toshkent', subscribe=1, user_id=call.from_user.id):
                await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineT)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineT)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='andijon')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Andijon', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineA)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineA)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='buxoro')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Buxoro', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅",reply_markup=obunaInlineB)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineB)
    except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='guliston')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Guliston', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineG)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineG)
    except sqlite3.IntegrityError as err:
         await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='samarqand')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Samarqand', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineS)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineS)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='namangan')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Namangan', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineNam)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineNam)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='navoi')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Navoiy', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineNav)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineNav)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='jizzax')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Jizzax',subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅",reply_markup=obunaInlineJ)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineJ)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='nukus')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Nukus',subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineNuk)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineNuk)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='qarshi')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Qarshi', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineQar)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineQar)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='qoqon')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Qoqon', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineQoq)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineQoq)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='xiva')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Xiva', subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineX)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineX)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='margilon')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    try:
        if db.select_user(region='Margilon',subscribe=1, user_id=call.from_user.id):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=obunaInlineM)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕 - o'chirilgan❌\nEslatma🔔 - yoqilgan✅", reply_markup=namozVaqtInlineM)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)



@dp.callback_query_handler(text='qaytish')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mintaqa❓",reply_markup=regionInline)




