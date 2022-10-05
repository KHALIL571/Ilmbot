from keyboards.inline.sahobalar_inline import sbsend
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text='s1')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=517)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=983)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=984)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=985)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=986)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=987)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                         "02 - Umar ibn Xattob r.a\n"
                         "03 - Usmon ibn Affon r.a\n"
                         "04 - Ali ibn Abu Tolib r.a\n"
                         "05 - Talha ibn Ubaydulloh r.a\n"
                         "06 - Sa'd ibn Abu Vaqqos r.a\n"
                         "07 - Abdurahmon ibn Avf r.a\n"
                         "08 - Said ibn Zayd r.a\n"
                         "09 - Abu Ubayda ibn Jarroh r.a\n"
                         "10 - Zubayr ibn Avvom r.a",reply_markup=sbsend)
    # await call.message.reply(sbsend)
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='s2')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=520)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=988)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=989)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=990)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=991)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=992)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=993)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=994)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=995)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                         "02 - Umar ibn Xattob r.a\n"
                         "03 - Usmon ibn Affon r.a\n"
                         "04 - Ali ibn Abu Tolib r.a\n"
                         "05 - Talha ibn Ubaydulloh r.a\n"
                         "06 - Sa'd ibn Abu Vaqqos r.a\n"
                         "07 - Abdurahmon ibn Avf r.a\n"
                         "08 - Said ibn Zayd r.a\n"
                         "09 - Abu Ubayda ibn Jarroh r.a\n"
                         "10 - Zubayr ibn Avvom r.a",reply_markup=sbsend)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='s3')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=522)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=996)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=997)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=998)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=999)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='s4')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=524,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1000,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1001,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1002,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1003,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1004,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1005,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1006,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1007,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1008,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1009,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1010,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1011,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1012,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1013,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1014,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1015,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1016,protect_content=True)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='s5')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=526)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1017)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='s6')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=528)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1021)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1022)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='s7')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=530)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1019)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1020)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='s8')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=532)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1023)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='s9')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=534)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1024)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1025)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='s10')
async def send_sb1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=536)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1018)
    await call.message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                              "02 - Umar ibn Xattob r.a\n"
                              "03 - Usmon ibn Affon r.a\n"
                              "04 - Ali ibn Abu Tolib r.a\n"
                              "05 - Talha ibn Ubaydulloh r.a\n"
                              "06 - Sa'd ibn Abu Vaqqos r.a\n"
                              "07 - Abdurahmon ibn Avf r.a\n"
                              "08 - Said ibn Zayd r.a\n"
                              "09 - Abu Ubayda ibn Jarroh r.a\n"
                              "10 - Zubayr ibn Avvom r.a", reply_markup=sbsend)
    await call.answer(cache_time=60)

