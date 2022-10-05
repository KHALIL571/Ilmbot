from aiogram.types import Message, CallbackQuery
from loader import dp, bot

from keyboards.inline.zam_sura_inline import zaminline

@dp.message_handler(text='Zam suralar📖')
async def zam(msg: Message):
    await msg.answer("""
<b>1 <i>Sharh</i></b>
<b>2 <i>Tiyn</i></b>
<b>3 <i>Fiyl</i></b>
<b>4 <i>Quraysh</i></b>
<b>5 <i>Ma'un</i>  </b>  
<b>6 <i>Kavsar</i>  </b>
<b>7 <i>Kafirun </i></b> 
<b>8 <i>Nasr</i>   </b>
<b>9 <i>Masad</i></b>
<b>10 <i>Ixlos</i></b>
<b>11 <i>Falaq</i></b>
<b>12 <i>Nas</i></b>
""",reply_markup=zaminline,parse_mode='html')

@dp.callback_query_handler(text='sura1')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1059,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida',message_id=1062,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura2')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1179,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=397,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura3')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1057,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=406,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura4')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1047,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=407,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura5')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1049,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=408,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura6')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1058,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=409,protect_content=True)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='sura7')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1050,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=410,protect_content=True)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='sura8')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1051,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=411,protect_content=True)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='sura9')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1052,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=412,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura10')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1053,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=413,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura11')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1054,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=414,protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura12')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1055,protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=415,protect_content=True)
    await call.answer(cache_time=60)



