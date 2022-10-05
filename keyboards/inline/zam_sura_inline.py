from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


zaminline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='01', callback_data='sura1'),
            InlineKeyboardButton(text='02', callback_data='sura2'),
            InlineKeyboardButton(text='03', callback_data='sura3'),
            InlineKeyboardButton(text='04', callback_data='sura4'),
            InlineKeyboardButton(text='05', callback_data='sura5'),
            InlineKeyboardButton(text='06', callback_data='sura6'),
        ],
        [
            InlineKeyboardButton(text='07', callback_data='sura7'),
            InlineKeyboardButton(text='08', callback_data='sura8'),
            InlineKeyboardButton(text='09', callback_data='sura9'),
            InlineKeyboardButton(text='10', callback_data='sura10'),
            InlineKeyboardButton(text='11', callback_data='sura11'),
            InlineKeyboardButton(text='12', callback_data='sura12'),
        ]
])
