from loader import dp, bot
from aiogram.types import CallbackQuery
from keyboards.inline.namozturlar_Inline import qoidalar


# FARZ_____________________


@dp.callback_query_handler(text='f:bomdod')
async def send_sura(call: CallbackQuery):
    # await bot.delete_message()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=686, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=692,protect_content=True)
@dp.callback_query_handler(text='f:peshin')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=680, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=694, protect_content=True)

@dp.callback_query_handler(text='f:asr')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=681, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=696, protect_content=True)

@dp.callback_query_handler(text='f:shom')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=682, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=697, protect_content=True)

@dp.callback_query_handler(text='f:xufton')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=684, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=699, protect_content=True)
@dp.callback_query_handler(text='juma')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=689, protect_content=True)

@dp.callback_query_handler(text='janoza')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=690, protect_content=True)

# SUNNAT__________________


@dp.callback_query_handler(text='s:bomdod')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=685, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=691,protect_content=True)

@dp.callback_query_handler(text='s:peshin2')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=679, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=695, protect_content=True)
@dp.callback_query_handler(text='s:peshin4')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=678, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=693,protect_content=True)

@dp.callback_query_handler(text='s:shom')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=683, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=698, protect_content=True)
@dp.callback_query_handler(text='s:xufton')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=705, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=700, protect_content=True)



# VOJIB _______________________

@dp.callback_query_handler(text='vitr')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=702, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=701, protect_content=True)

@dp.callback_query_handler(text='hayit')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=703, protect_content=True)

# NAMOZ TURLARI ______________________

@dp.callback_query_handler(text='in')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1186, protect_content=True)

@dp.callback_query_handler(text='tn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1193, protect_content=True)


@dp.callback_query_handler(text='mn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1187,
                           protect_content=True)


@dp.callback_query_handler(text='shn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1188,
                           protect_content=True)


@dp.callback_query_handler(text='zn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1189,
                           protect_content=True)


@dp.callback_query_handler(text='shn2')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1190,
                           protect_content=True)


@dp.callback_query_handler(text='tavban')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1194,
                           protect_content=True)


@dp.callback_query_handler(text='tasbeh')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1195,
                           protect_content=True)

@dp.callback_query_handler(text='hn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1191,
                           protect_content=True)


@dp.callback_query_handler(text='an')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1192,
                           protect_content=True)


@dp.callback_query_handler(text='markab')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1196,
                           protect_content=True)

@dp.callback_query_handler(text="amalF")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1197,protect_content=True)

@dp.callback_query_handler(text="amalV")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1198,protect_content=True)

@dp.callback_query_handler(text="amalS")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1199,protect_content=True)

@dp.callback_query_handler(text="mustahab")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1200,protect_content=True)

@dp.callback_query_handler(text="harom")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1201,protect_content=True)

@dp.callback_query_handler(text="muboh")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1202,protect_content=True)

@dp.callback_query_handler(text="makruh1")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1203,protect_content=True)

@dp.callback_query_handler(text="makruh2")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1204,protect_content=True)

@dp.callback_query_handler(text="odob")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1205,protect_content=True)

@dp.callback_query_handler(text="buzuvchi")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1208,protect_content=True)

@dp.callback_query_handler(text="sajda")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1206,protect_content=True)

@dp.callback_query_handler(text="sutra")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1207,protect_content=True)


