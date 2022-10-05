from aiogram.types import CallbackQuery

from keyboards.inline.arab_tili import dars1, dars2,dars5,dars6,dars3,dars4,dars7,dars8
from loader import dp, bot


@dp.callback_query_handler(text='m_s_dars')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars1)
    await call.message.delete()

@dp.callback_query_handler(text='dars1')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars1)
    await call.message.delete()

@dp.callback_query_handler(text='dars2')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars2)
    await call.message.delete()

@dp.callback_query_handler(text='dars3')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars3)
    await call.message.delete()

@dp.callback_query_handler(text='dars4')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars4)
    await call.message.delete()

@dp.callback_query_handler(text='dars5')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars5)
    await call.message.delete()

@dp.callback_query_handler(text='dars6')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars6)
    await call.message.delete()

@dp.callback_query_handler(text='dars7')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars7)
    await call.message.delete()

@dp.callback_query_handler(text='dars8')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli darslikni tanlang👇",reply_markup=dars8)
    await call.message.delete()






@dp.callback_query_handler(text='ms1')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1257)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms2')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1258)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms3')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1259)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms4')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1260)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms5')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1261)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms6')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1262)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms7')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1263)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms8')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1264)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms9')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1265)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms10')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1266)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars1)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms11')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1267)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms12')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1268)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms13')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1269)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms14')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1270)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms15')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1271)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms16')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1272)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms17')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1273)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms18')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1274)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms19')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1275)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms20')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1276)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms21')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1277)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms22')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1278)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms23')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1279)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms24')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1280)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms25')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1281)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms26')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1282)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms27')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1283)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms28')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1284)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms29')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1285)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms30')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1286)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms31')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1287)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms32')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1288)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms33')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1289)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms34')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1290)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms35')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1291)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms36')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1292)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms37')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1294)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms38')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1295)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms39')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1296)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms40')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1297)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms41')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1298)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms42')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1299)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms43')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1300)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms44')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1301)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms45')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1302)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms46')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1303)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms47')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1304)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms48')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1305)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms49')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1306)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms50')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1307)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms51')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1308)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms52')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1309)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms53')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1310)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms54')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1311)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms55')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1312)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms56')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1313)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms57')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1314)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms58')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1315)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms59')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1316)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms60')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1317)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms61')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1318)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms62')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1319)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms63')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1320)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms64')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1321)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms65')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1322)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms66')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1323)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms67')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1324)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms68')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1325)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms69')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1326)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms70')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1327)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars7)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ms71')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1328)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars8)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ms72')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1329)
    await call.message.answer("O'zingizga kerakli serani tanlang👇", reply_markup=dars8)
    await call.message.delete()
    await call.answer(cache_time=60)
