from aiogram.types import CallbackQuery
from aiogram.types import Message

from keyboards.default.menuKeyboard import menu
from keyboards.inline.dars import QuranTartli, QuranTartli2, QuranTartli3
from loader import dp, bot


@dp.callback_query_handler(text='tartili')
async def tartili_Menu1(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()

@dp.callback_query_handler(text='main')
async def tartili_Menu2(call:CallbackQuery):
    await call.message.answer("menuni tanlang👇",reply_markup=menu)
    await call.message.delete()


@dp.callback_query_handler(text='tartiliMenu2')
async def tartili_Menu2(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()

@dp.callback_query_handler(text='tartiliMenu3')
async def tartili_Menu3(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()

@dp.callback_query_handler(text='tartili1')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1330)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili2')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1331)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili3')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1332)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili4')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1333)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili5')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1334)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili6')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1335)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili7')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1336)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili8')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1337)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili9')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1338)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili10')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1339)
    await call.message.answer("O'zingizga kerakli darsni tanlang👇",reply_markup=QuranTartli)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili11')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1340)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili12')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1341)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili13')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1342)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili14')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1343)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili15')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1344)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili16')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1345)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili17')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1346)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili18')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1347)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili19')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1348)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili20')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1349)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili21')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1350)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili22')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1351)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili23')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1352)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili24')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1353)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili25')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1354)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili26')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1355)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili27')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1356)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili28')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1357)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili29')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1358)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili30')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1359)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='tartili31')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1360)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=QuranTartli3)
    await call.message.delete()
    await call.answer(cache_time=60)