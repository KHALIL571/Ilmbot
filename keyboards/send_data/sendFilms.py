from keyboards.inline.kino import umarSeries, umarSeries2, umarSeries3
from loader import dp, bot
from aiogram.types import CallbackQuery, message


@dp.callback_query_handler(text='Bilol')
async def bilol_callback(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1362, protect_content=True)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='Umar')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()

@dp.callback_query_handler(text='umar1')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1363, protect_content=True)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar2')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1364, protect_content=True)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar3')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1365)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar4')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1366)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar5')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1367)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar6')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1368)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar7')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1369)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar8')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1370)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar9')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1371)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='umar10')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1372)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='umarmenu2')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()

@dp.callback_query_handler(text='umarmenu3')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()

@dp.callback_query_handler(text='umar11')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1373)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar12')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1374)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar13')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1375)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar14')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1376)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar15')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1377)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar16')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1378)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar17')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1379)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar18')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1380)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar19')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1381)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar20')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1382)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar21')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1383)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar22')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1384)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar23')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1385)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar24')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1386)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar25')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1387)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar26')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1388)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar27')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1389)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar28')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1390)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar29')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1391)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar30')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1392)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)
#
# @dp.callback_query_handler(text='umar30')
# async def send_umar1(call: CallbackQuery):
#     await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1393)
#     await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
#     await call.message.delete()
#     await call.answer(cache_time=60)
