from loader import dp
from aiogram.types import CallbackQuery, Message

from keyboards.inline.namozturlar_Inline import namozTurlari, birinchi, ikkinchi, uchinchi, tortinchi, qoidalar

@dp.message_handler(text='Namoz turlari🧎')
async def namozTuri(msg:Message):
    await msg.answer("Namoz haqida to'liq malumotni\n<b>«Hadis va Hayot»(<i>Shayx Muhammad Sodiq Muhammad Yusuf</i>)</b> kitobining 6-juzidan topshingiz mumkun...",reply_markup=namozTurlari,parse_mode="html")

@dp.callback_query_handler(text='namozqoidalari')
async def namozqoidalari(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("NAMOZDAGI AMALLAR:",reply_markup=qoidalar)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="namF")
async def farz(call:CallbackQuery):
    await call.message.answer("<b>• Farz namozlari</b> - Alloh taoloning amri bilan har bir musulmon zimmasida burch hisoblangan bеsh vaqt namoz (bomdod, pеshin, asr, shom, xufton) va juma namozi hamda (musulmonlardan ba'zilarining oʻqishi bilan boshqalardan soqit boʻluvchi) janoza namozi.",reply_markup=birinchi,parse_mode="html")
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="namV")
async def vojib(call: CallbackQuery):
    await call.message.answer("<b>• Vojib namozlar</b> – har kuni xuftondan soʻng oʻqiladigan vitr namozi, ramazon va qurbon hayiti namozlari, Baytullohdagi tavof namozi.", reply_markup=ikkinchi, parse_mode="html")
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="namS")
async def sunnat(call: CallbackQuery):
    await call.message.answer("""Sunnat namozi - Bizda farz namozlarga tobe’ bo‘lganlarini sunnat, boshqalarini nafl namoz, deyish urf bo‘lgan.""", reply_markup=uchinchi, parse_mode="html")
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="namN")
async def nafl(call: CallbackQuery):
    await call.message.answer("""
«Nafl namozi» deb kishi o‘z ixtiyori bilan farzga qo‘shimcha tarzda o‘qiydigan namozga aytiladi. Bu namozni Alloh taolo mo‘minlar zimmasiga farz kabi majburiy qilmagan, balki ixtiyoriy suratda ado etilsa, savob bo‘ladi.""", reply_markup=tortinchi, parse_mode="html")
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="namozturlariga")
async def turlari(call:CallbackQuery):
    await call.message.answer("Namoz haqida to'liq malumotni\n<b>«Hadis va Hayot»(<i>Shayx Muhammad Sodiq Muhammad Yusuf</i>)</b> kitobining\n 6-juzidan topshingiz mumkun...", reply_markup=namozTurlari, parse_mode="html")
    await call.message.delete()
    await call.answer(cache_time=60)

