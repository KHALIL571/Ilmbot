from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


QuranTartli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1-dars', callback_data='tartili1'),
            InlineKeyboardButton(text='2-dars', callback_data='tartili2'),
            InlineKeyboardButton(text='3-dars', callback_data='tartili3'),
            InlineKeyboardButton(text='4-dars', callback_data='tartili4'),
            InlineKeyboardButton(text='5-dars', callback_data='tartili5'),
        ],
        [
            InlineKeyboardButton(text='6-dars', callback_data='tartili6'),
            InlineKeyboardButton(text='7-dars', callback_data='tartili7'),
            InlineKeyboardButton(text='8-dars', callback_data='tartili8'),
            InlineKeyboardButton(text='9-dars', callback_data='tartili9'),
            InlineKeyboardButton(text='10-dars', callback_data='tartili10'),
        ],
        [
            InlineKeyboardButton(text='➡️',callback_data='tartiliMenu2')
        ]
    ])
QuranTartli2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='11-dars', callback_data='tartili11'),
            InlineKeyboardButton(text='12-dars', callback_data='tartili12'),
            InlineKeyboardButton(text='13-dars', callback_data='tartili13'),
            InlineKeyboardButton(text='14-dars', callback_data='tartili14'),
            InlineKeyboardButton(text='15-dars', callback_data='tartili15'),
        ],
        [
            InlineKeyboardButton(text='16-dars', callback_data='tartili16'),
            InlineKeyboardButton(text='17-dars', callback_data='tartili17'),
            InlineKeyboardButton(text='18-dars', callback_data='tartili18'),
            InlineKeyboardButton(text='19-dars', callback_data='tartili19'),
            InlineKeyboardButton(text='20-dars', callback_data='tartili20'),
        ],
        [
            InlineKeyboardButton(text='⬅️', callback_data='tartili'),
            InlineKeyboardButton(text='➡️', callback_data='tartiliMenu3')
        ]
        # [
        #     InlineKeyboardButton(text='Asosiy menuga qaytish',callback_data='main')
        # ]

])
QuranTartli3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='21-dars', callback_data='tartili21'),
            InlineKeyboardButton(text='22-dars', callback_data='tartili22'),
            InlineKeyboardButton(text='23-dars', callback_data='tartili23'),
            InlineKeyboardButton(text='24-dars', callback_data='tartili24'),
            InlineKeyboardButton(text='25-dars', callback_data='tartili25'),
        ],
        [
            InlineKeyboardButton(text='26-dars', callback_data='tartili26'),
            InlineKeyboardButton(text='27-dars', callback_data='tartili27'),
            InlineKeyboardButton(text='28-dars', callback_data='tartili28'),
            InlineKeyboardButton(text='29-dars', callback_data='tartili29'),
            InlineKeyboardButton(text='30-dars', callback_data='tartili30'),
        ],
        [
            InlineKeyboardButton(text='31-dars', callback_data='tartili31'),
        ],
        [
            InlineKeyboardButton(text='⬅️',callback_data='tartiliMenu2')
        ]
    ])