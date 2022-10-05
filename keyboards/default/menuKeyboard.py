from datetime import time

from aiogram.bot import bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery

from keyboards.default.namazKeyboard import namozMenu
from keyboards.inline.kitoblar_Inline import kbsend
from keyboards.inline.sahobalar_inline import sbsend
from loader import dp

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Namoz🕋', callback_data='namozMenu'),
            InlineKeyboardButton(text='Qur\'on📖', callback_data='quronMain'),

        ],
        [
            InlineKeyboardButton(text='Duo va Zikirlar🤲', callback_data='duoMain'),
        ],
        [
            InlineKeyboardButton(text='Sahobalar👳🏻‍♂️️', callback_data='sahobaMain'),
            InlineKeyboardButton(text='Asmaul Husna', callback_data='ismMain'),

        ],
        [
            InlineKeyboardButton(text='Yaqin Masjid🕌️️', callback_data='masjidMain'),
            InlineKeyboardButton(text='Kitoblar📚', callback_data='kitobMain'),

        ],
        [
            InlineKeyboardButton(text='kino', callback_data='kinoMain'),
            InlineKeyboardButton(text='dars', callback_data='darsMain'),

        ],


    ])

@dp.callback_query_handler(text='namozMenu')
async def menuNamaz(call:CallbackQuery):
    await call.message.edit_text("<b>«Ahlingizni namoz (o‘qish)ga buyuring va (o‘zingiz ham) unga (namozga) bardoshli bo‘ling!»</b>\n(Toha, 132).",parse_mode='html')
    await call.message.edit_reply_markup(namozMenu)
    # await call.message.delete()

# @dp.callback_query_handler(text='namazTime')
# async def namaz_time(call: CallbackQuery):
#     await call.message.edit_text()
#     await call.message.edit_reply_markup()

@dp.callback_query_handler(text='kitobMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("01 - Musulmonning odobi\n"
                         "02 - VIjdon azobi\n"
                         "03 - Payg'ambarlar tarixi\n"
                         "04 - Oisha r.a\n"
                         "05 - Qiyomat va Oxirat \n"
                         "06 - Ibodati islomiya\n"
                         "07 - Tarixi Muhammadiy\n"
                         "08 - Saodat asri qissalari\n"
                         "09 - Hadis va Hayot (9 juz)\n"
                         "10 - Qirq hadisi qudusiy")
    await call.message.edit_reply_markup(kbsend)

@dp.callback_query_handler(text='sahobaMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("01 - Abu Bakr As-Siddiq r.a\n"
                         "02 - Umar ibn Xattob r.a\n"
                         "03 - Usmon ibn Affon r.a\n"
                         "04 - Ali ibn Abu Tolib r.a\n"
                         "05 - Talha ibn Ubaydulloh r.a\n"
                         "06 - Sa'd ibn Abu Vaqqos r.a\n"
                         "07 - Abdurahmon ibn Avf r.a\n"
                         "08 - Said ibn Zayd r.a\n"
                         "09 - Abu Ubayda ibn Jarroh r.a\n"
                         "10 - Zubayr ibn Avvom r.a")
    await call.message.edit_reply_markup(sbsend)

@dp.callback_query_handler(text='menu')
async def Umar_callback(call:CallbackQuery):
    await call.message.edit_reply_markup(menu)
    # await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=menu)
    # await call.message.delete()

quron =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qur'onga o'tish📖"),
        ],
        [
            KeyboardButton(text='Bosh menu⬅️')
        ],
],
    resize_keyboard=True)

