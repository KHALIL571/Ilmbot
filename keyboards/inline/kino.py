from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

films = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Bilol ibn Raboh', callback_data='Bilol'),
            InlineKeyboardButton(text='Umar ibn hattob', callback_data='Umar'),

        ],


    ])

umarSeries = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='umar1'),
            InlineKeyboardButton(text='2', callback_data='umar2'),
            InlineKeyboardButton(text='3', callback_data='umar3'),
            InlineKeyboardButton(text='4', callback_data='umar4'),
            InlineKeyboardButton(text='5', callback_data='umar5'),
        ],
        [
            InlineKeyboardButton(text='6', callback_data='umar6'),
            InlineKeyboardButton(text='7', callback_data='umar7'),
            InlineKeyboardButton(text='8', callback_data='umar8'),
            InlineKeyboardButton(text='9', callback_data='umar9'),
            InlineKeyboardButton(text='10', callback_data='umar10'),
        ],
        [
            InlineKeyboardButton(text='➡️',callback_data='umarmenu2')
        ]
    ])
umarSeries2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='11', callback_data='umar11'),
            InlineKeyboardButton(text='12', callback_data='umar12'),
            InlineKeyboardButton(text='13', callback_data='umar13'),
            InlineKeyboardButton(text='14', callback_data='umar14'),
            InlineKeyboardButton(text='15', callback_data='umar15'),
        ],
        [
            InlineKeyboardButton(text='16', callback_data='umar16'),
            InlineKeyboardButton(text='17', callback_data='umar17'),
            InlineKeyboardButton(text='18', callback_data='umar18'),
            InlineKeyboardButton(text='19', callback_data='umar19'),
            InlineKeyboardButton(text='20', callback_data='umar20'),
        ],
        [
            InlineKeyboardButton(text='⬅️', callback_data='Umar'),
            InlineKeyboardButton(text='➡️', callback_data='umarmenu3')
        ]

])
umarSeries3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='21', callback_data='umar21'),
            InlineKeyboardButton(text='22', callback_data='umar22'),
            InlineKeyboardButton(text='23', callback_data='umar23'),
            InlineKeyboardButton(text='24', callback_data='umar24'),
            InlineKeyboardButton(text='25', callback_data='umar25'),
        ],
        [
            InlineKeyboardButton(text='26', callback_data='umar26'),
            InlineKeyboardButton(text='27', callback_data='umar27'),
            InlineKeyboardButton(text='28', callback_data='umar28'),
            InlineKeyboardButton(text='29', callback_data='umar29'),
            InlineKeyboardButton(text='30', callback_data='umar30'),
        ],
        [
            InlineKeyboardButton(text='⬅️',callback_data='umarmenu2')
        ]
    ])