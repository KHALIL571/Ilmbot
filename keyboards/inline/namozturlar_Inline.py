from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


namozTurlari = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='NAMOZ QOIDALARI', callback_data='namozqoidalari')
        ],
        [
            InlineKeyboardButton(text='FARZ NAMOZLAR', callback_data='namF')
        ],
        [
            InlineKeyboardButton(text='VOJIB NAMOZLAR', callback_data='namV')
        ],
        [
            InlineKeyboardButton(text='SUNNAT NAMOZLAR', callback_data='namS')
        ],
        [
            InlineKeyboardButton(text='NAFL NAMOZLAR', callback_data='namN')
        ],
    ])

qoidalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Farz', callback_data='amalF'),
            InlineKeyboardButton(text='Vojib', callback_data='amalV'),
            InlineKeyboardButton(text='Sunnat', callback_data='amalS'),
        ],
        [
            InlineKeyboardButton(text='Mustahab', callback_data='mustahab'),
            InlineKeyboardButton(text='Harom', callback_data='harom'),
            InlineKeyboardButton(text='Muboh', callback_data='muboh')
        ],
        [
            InlineKeyboardButton(text='Makruh Bo\'lgan', callback_data='makruh1'),
            InlineKeyboardButton(text='Makruh Bo\'lmagan', callback_data='makruh2'),
        ],
        [
            InlineKeyboardButton(text='Namoz Odoblari', callback_data='odob'),
            InlineKeyboardButton(text='Namozni Buzuvchi', callback_data='buzuvchi')
        ],
        [
            InlineKeyboardButton(text='Sajdai Sahv ', callback_data='sajda'),
            InlineKeyboardButton(text='Sutra', callback_data='sutra')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])


birinchi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌄️Bomdod Namozi', callback_data='f:bomdod')
        ],
        [
            InlineKeyboardButton(text='🌇Peshin Namozi', callback_data='f:peshin')
        ],
        [
            InlineKeyboardButton(text='🌆Asr Namozi', callback_data='f:asr')
        ],
        [
            InlineKeyboardButton(text='️🏙Shom Namozi', callback_data='f:shom')
        ],
        [
            InlineKeyboardButton(text='🌃Xufton Namozi', callback_data='f:xufton')
        ],
        [
            InlineKeyboardButton(text='Juma Namozi(Jamoat)', callback_data='juma')
        ],
        [
            InlineKeyboardButton(text='Janoza Namozi(Jamoat)', callback_data='janoza')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])

ikkinchi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Vitr Namozi', callback_data='vitr')
        ],
        [
            InlineKeyboardButton(text='Ramazon va Qurbon Hayit Namozlari', callback_data='hayit')
        ],
        [
            InlineKeyboardButton(text='Baytullohdagi Tavof Namozi', callback_data='tavof')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])

uchinchi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌄️Bomdod namozi', callback_data='s:bomdod')
        ],
        [
            InlineKeyboardButton(text='🌇Peshin namozi(4 rakat)', callback_data='s:peshin4')
        ],
        [
            InlineKeyboardButton(text='🌇Peshin namozi(2 rakat)', callback_data='s:peshin2')
        ],
        [
            InlineKeyboardButton(text='️🏙Shom namozi', callback_data='s:shom')
        ],
        [
            InlineKeyboardButton(text='🌃Xufton namozi', callback_data='s:xufton')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])


tortinchi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='ISTIXORA NAMOZI', callback_data='in'),
            InlineKeyboardButton(text='TAHAJJUT NAMOZI', callback_data='tn')
        ],
        [
            InlineKeyboardButton(text='TAHIYYATUL MASJID NAMOZI', callback_data='mn'),
            InlineKeyboardButton(text='SHURUQ (ISHROQ) NAMOZI', callback_data='shn')
        ],
        [
            InlineKeyboardButton(text='ZUHO (CHOSHGOH) NAMOZI', callback_data='zn'),
            InlineKeyboardButton(text='SHUKRI VUZU’ NAMOZI', callback_data='shn2')
        ],
        [
            InlineKeyboardButton(text='HOJAT NAMOZI', callback_data='hn'),
            InlineKeyboardButton(text='AVVOBIYN NAMOZI', callback_data='an')
        ],
        [
            InlineKeyboardButton(text='TАVBА NАMOZI', callback_data='tavban'),
            InlineKeyboardButton(text='TАSBEH NАMOZI', callback_data='tasbeh')
        ],
        [
            InlineKeyboardButton(text='MАRKАBDА NАMOZ OʼQISH', callback_data='markab')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])


gusl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='G\'usl', callback_data='gusl')
        ],
        [
            InlineKeyboardButton(text='Tahorat', callback_data='tahorat')
        ],

    ])
