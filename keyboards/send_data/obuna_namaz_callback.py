from keyboards.inline.obuna_Inline import obunaInlineNuk,obunaInlineQar,obunaInlineQoq,obunaInlineJ,obunaInlineM,obunaInlineX,obunaInlineNam,obunaInlineNav,obunaInlineA,obunaInlineB,obunaInlineG,obunaInlineS,obunaInlineT, namozVaqtInlineT,namozVaqtInlineA,namozVaqtInlineB,namozVaqtInlineG,namozVaqtInlineJ,namozVaqtInlineM,namozVaqtInlineS,namozVaqtInlineX,namozVaqtInlineNuk,namozVaqtInlineNam,namozVaqtInlineNav,namozVaqtInlineQar,namozVaqtInlineQoq
from data.config import ADMINS
from loader import dp, bot, db

import sqlite3
from aiogram.types import CallbackQuery

#['obuna:toshkent','obuna:buxoro','obuna:andijon','obuna:guliston','obuna:jizzax','obuna:margilon','obuna:namangan','obuna:navoi','obuna:nukus','obuna:qoqon','obuna:qarshi','obuna:samarqand','obuna:xiva'])
#['ochir:toshkent','ochir:buxoro','ochir:andijon','ochir:guliston','ochir:jizzax','ochir:margilon','ochir:namangan','ochir:navoi','ochir:nukus','ochir:qoqon','ochir:qarshi','ochir:samarqand','ochir:xiva'])

@dp.callback_query_handler(text='obuna:toshkent')
async def inline_follow1(call:CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineT)
    try:
        db.update_user(region='Toshkent', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ochir:toshkent')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineT)
    try:
        db.update_user(region='Toshkent', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)
""""Buxoro"""
@dp.callback_query_handler(text='obuna:buxoro')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineB)
    try:
        db.update_user(region='Buxoro', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:buxoro')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineB)
    try:
        db.update_user(region='Buxoro', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Andijon"""
@dp.callback_query_handler(text='obuna:andijon')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineA)
    try:
        db.update_user(region='Andijon', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:andijon')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineA)
    try:
        db.update_user(region='Andijon', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Guliston"""
@dp.callback_query_handler(text='obuna:guliston')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineG)
    try:
        db.update_user(region='Guliston', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:guliston')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineG)
    try:
        db.update_user(region='Guliston', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Jizzax"""
@dp.callback_query_handler(text='obuna:jizzax')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineJ)
    try:
        db.update_user(region='Jizzax', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:jizzax')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineJ)
    try:
        db.update_user(region='Jizzax', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)
""""Margilon"""
@dp.callback_query_handler(text='obuna:margilon')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineM)
    try:
        db.update_user(region='Marg\'ilon', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:margilon')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineM)
    try:
        db.update_user(region='Marg\'ilon', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Namangan"""
@dp.callback_query_handler(text='obuna:namangan')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineNam)
    try:
        db.update_user(region='Namangan', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:namangan')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineNam)
    try:
        db.update_user(region='Namangan', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)
""""Navoiy"""
@dp.callback_query_handler(text='obuna:navoi')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineNav)
    try:
        db.update_user(region='Navoiy', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:navoi')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineNav)
    try:
        db.update_user(region='Navoiy', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Nukus"""
@dp.callback_query_handler(text='obuna:nukus')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineNuk)
    try:
        db.update_user(region='Nukus', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:nukus')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineNuk)
    try:
        db.update_user(region='Nukus', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Qoqon"""
@dp.callback_query_handler(text='obuna:qoqon')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineQoq)
    try:
        db.update_user(region='Qo\'qon', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:qoqon')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineQoq)
    try:
        db.update_user(region='Qo\'qon', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Qarshi"""
@dp.callback_query_handler(text='obuna:qarshi')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineQar)
    try:
        db.update_user(region='Qarshi', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ochir:qarshi')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineQar)
    try:
        db.update_user(region='Qarshi', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Samarqand"""
@dp.callback_query_handler(text='obuna:samarqand')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineS)
    try:
        db.update_user(region='Samarqand', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:samarqand')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineS)
    try:
        db.update_user(region='Samarqand', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)

""""Xiva"""
@dp.callback_query_handler(text='obuna:xiva')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=obunaInlineX)
    try:
        db.update_user(region='Xiva', subscribe=1, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ochir:xiva')
async def inline_follow1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineX)
    try:
        db.update_user(region='Xiva', subscribe=0, user_id=call.from_user.id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")
    await call.answer(cache_time=60)








