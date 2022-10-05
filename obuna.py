import datetime
import time
import requests


from data.config import BOT_TOKEN
from loader import db

TOKEN = BOT_TOKEN

def send_text(token:str, chat_id_list: list, text: str):
    for chat_id in chat_id_list:
        requests.post(
            url=f'https://api.telegram.org/bot{token}/sendMessage',
            data={'chat_id': chat_id, 'text': text}
        )

def bomdod(chat_id:list):
    send_text(TOKEN, chat_id, "🌌Bomdod vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")

def quyosh(chat_id:list):
    send_text(TOKEN, chat_id, "🌄Quyosh chiqdi!\n\nAbdulloh ibn Amr ibn Os roziyallohu anhudan rivoyat qilinadi:\n«Rasululloh sollallohu alayhi vasallamdan namozlarning vaqti haqida so‘raldi. Bas, u zot:\n«Bomdod namozining vaqti quyoshning avvalgi shoxi chiqmaguncha…» dedilar».")

def peshin(chat_id:list):
    send_text(TOKEN, chat_id, "🌇Peshin vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")

def asr(chat_id:list):
    send_text(TOKEN, chat_id, "🌆Asr vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")

def shom(chat_id:list):
    send_text(TOKEN, chat_id, "🏙Shom vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")

def xufton(chat_id:list):
    send_text(TOKEN, chat_id, "🌃Xufton vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")

delta = datetime.timedelta(hours=5)
while True:
    for user in db.get_users_subscribe():
        for t in db.get_times():
            if user[3] == t[0]:
                try:
                    if t[1] == (datetime.datetime.now()+delta).strftime('%H:%M'):
                        bomdod([user[1]])
                    if t[2] == (datetime.datetime.now()+delta).strftime('%H:%M'):
                        quyosh([user[1]])
                    if t[3] == (datetime.datetime.now()+delta).strftime('%H:%M'):
                        peshin([user[1]])
                    if t[4] == (datetime.datetime.now()+delta).strftime('%H:%M'):
                        asr([user[1]])
                    if t[5] == (datetime.datetime.now()+delta).strftime('%H:%M'):
                        shom([user[1]])
                    if t[6] == (datetime.datetime.now()+delta).strftime('%H:%M'):
                        xufton([user[1]])
                    print(user[1])
                except Exception as err:
                    print(err)
    time.sleep(60)





