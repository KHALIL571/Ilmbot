from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kbsend = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='01', callback_data='k1'),
            InlineKeyboardButton(text='02', callback_data='k2'),
            InlineKeyboardButton(text='03', callback_data='k3'),
            InlineKeyboardButton(text='04', callback_data='k4'),
            InlineKeyboardButton(text='05', callback_data='k5'),


        ],
        [
            InlineKeyboardButton(text='06', callback_data='k6'),
            InlineKeyboardButton(text='07', callback_data='k7'),
            InlineKeyboardButton(text='08', callback_data='k8'),
            InlineKeyboardButton(text='09', callback_data='k9'),
            InlineKeyboardButton(text='10', callback_data='k10'),



        ],
        [
            InlineKeyboardButton(text='➡️', callback_data='page2')
        ]


    ])
kbsend2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='11', callback_data='k11'),
            InlineKeyboardButton(text='12', callback_data='k12'),
            InlineKeyboardButton(text='13', callback_data='k13'),
            InlineKeyboardButton(text='14', callback_data='k14'),
            InlineKeyboardButton(text='15', callback_data='k15'),


        ],
        [
            InlineKeyboardButton(text='16', callback_data='k16'),
            InlineKeyboardButton(text='17', callback_data='k17'),
            InlineKeyboardButton(text='18', callback_data='k18'),
            InlineKeyboardButton(text='19', callback_data='k19'),
            InlineKeyboardButton(text='20', callback_data='k20'),

        ],
        [
            InlineKeyboardButton(text='⬅️', callback_data='page1')
        ]


])


