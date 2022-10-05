from aiogram import types
from aiogram.bot import bot

from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboard import quron
from keyboards.inline.arab_tili import dars

from keyboards.inline.kino import films
from keyboards.inline.sahobalar_inline import sbsend
from keyboards.default.namazKeyboard import namozMenu
from keyboards.default.duoKeyboard import Menuduolar
from keyboards.inline.kitoblar_Inline import kbsend

from loader import dp
b = bot.Bot
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Bosh menu",reply_markup=menu)

@dp.message_handler(text='Namoz🕋')
async def send_link(message: Message):
    await message.answer("<b>«Ahlingizni namoz (o‘qish)ga buyuring va (o‘zingiz ham) unga (namozga) bardoshli bo‘ling!»</b>\n(Toha, 132).",reply_markup=namozMenu,parse_mode='html')

@dp.message_handler(text='Duo va Zikirlar🤲')
async def send_link(message: Message):
    await message.answer("<i>Alloh vaqtlaringizni o'zining zikri ila xush o'tishini nasib etsin!</i>",reply_markup=Menuduolar, parse_mode='html')

@dp.message_handler(text='Qur\'on📖')
async def send_quran(message: Message):
    await message.answer("""<b>Qur'on karim haqida ma'lumotlar:</b>\n
• <i>Qur'onning ismi Furqon</i>
• <i>Qur'onning laqabi. Majid</i>
• <i>Qur'on nozil bo'lgan yil. 611 milodiy yili</i>
• <i>Qur'on nozil bo'lgan oyi. Ramazon oyi</i>
• <i>Qur'on nozil bo'lgan kecha. Qadr kechasi</i>
• <i>Qur'on nozil bo'lgan joy. Makka Hiro g'ori</i>
• <i>Vahiy farishtasi. <b>Jabroil Alayhi Salom</b></i>
• <i>Vahiyni qabul qilgan. <b>Muhammad Sallohu Alayhi Vasallam</b></i>
• <i>Birinchi nozil bo'lgan sura. Alaq surasining 5 ta oyati</i>
• <i>Oxirgi nozil bölgan sura. Nasr surasi</i>
• <i>Eng buyuk sura. Baqara surasi</i>
• <i>Eng kichkina sura. Kavsar surasi</i>
• <i>Eng barokatli oyat. Oyatul kursi</i>
• <i>Eng buyuk oyat. Baqara suraning 286-oyati</i>
• <i>Qur'onning onasi. Fotiha surasi</i>
• <i>Qur'onni qalbi. Yosin surasi</i>
• <i>Qur'onning  kelini. Rahmon surasi</i>
• <i>Nozil bulgan muddat. 23 yilda</i>
• <i>Qur'on necha juz. 30 juz(pora)</i>
• <i>Qur'onning suralari. 114 ta</i>
• <i>Qur'onning  oyatilari 6236ta(bazi manbalarda 6666)</i>
• <i>Qur'onning sajdalari. 14 sajda</i>
• <i>Qur'onning ruku'lari. 540 ta</i>""",reply_markup=quron,parse_mode="html")

@dp.message_handler(text_contains='Sahobalar👳🏻‍♂️️')
async def send_list(message: Message):
    await message.answer("01 - Abu Bakr As-Siddiq r.a\n"
                         "02 - Umar ibn Xattob r.a\n"
                         "03 - Usmon ibn Affon r.a\n"
                         "04 - Ali ibn Abu Tolib r.a\n"
                         "05 - Talha ibn Ubaydulloh r.a\n"
                         "06 - Sa'd ibn Abu Vaqqos r.a\n"
                         "07 - Abdurahmon ibn Avf r.a\n"
                         "08 - Said ibn Zayd r.a\n"
                         "09 - Abu Ubayda ibn Jarroh r.a\n"
                         "10 - Zubayr ibn Avvom r.a"
                         ,reply_markup=sbsend)

@dp.message_handler(text_contains='Kitoblar📚')
async def send_book(message: Message):
    await message.answer("01 - Musulmonning odobi\n"
                         "02 - VIjdon azobi\n"
                         "03 - Payg'ambarlar tarixi\n"
                         "04 - Oisha r.a\n"
                         "05 - Qiyomat va Oxirat \n"
                         "06 - Ibodati islomiya\n"
                         "07 - Tarixi Muhammadiy\n"
                         "08 - Saodat asri qissalari\n"
                         "09 - Hadis va Hayot (9 juz)\n"
                         "10 - Qirq hadisi qudusiy"
                         ,reply_markup=kbsend)

@dp.message_handler(text_contains='kino')
async def send_kino(message: types.Message):
    if await message.answer("O'zingizga kerakli filmini tanlang!",reply_markup=films):
     await message.delete()










@dp.message_handler(text_contains='dars')
async def send_kino(message: types.Message):


    await message.answer("O'zingizga kerakli darsni tanlang!", reply_markup=dars)

    await message.delete()



@dp.message_handler(text='Bosh menu⬅️')
async def back(message: Message):
    await message.answer("Bosh menu", reply_markup=menu)



