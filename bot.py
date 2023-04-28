import time
import youtube_dl, time
from youtube_search import YoutubeSearch
import requests
import json
import requests
from pyrogram import Client, filters
from asyncio import sleep
import os
from logging import INFO
from pyrogram import Client, filters
from pytube import YouTube, exceptions
import os
import requests
import logging
import sys
from autologging import logged, traced

# Enable logging
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
api_id = int (808192)
api_hash = 'd2a1c1fe0d574f98068c63d4928aee8a'
bot_token = '5625085207:AAE6sgDvBNbyDPvvI69bixP6S3RNUHouY-Q'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
with app:
    botname = app.get_me().username
# on_progress_callback takes 4 parameters.
def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
    percent = (100*(file_size-remaining))/file_size
    print("{:00.0f}% downloaded".format(percent))
#BAM
# Enable logging
logging.basicConfig(
    format='%(asctime)s  - %(message)s', level=INFO)
logger = logging.getLogger(__name__)

#bienvenids
@app.on_message(filters.new_chat_members)
async def start(client, message):
    messy = message.from_user.mention
    await message.reply_text(f"Hola! {messy} Bienvenido al grupo",)

@app.on_message(filters.left_chat_member)
async def end(client, message):
    await message.reply_text("Hasta nunca")

#start
@app.on_message(filters.command("start"))
async def start(client, message):
    messy = message.from_user.mention
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Soporte", url="https://t.me/d0b3rm4nn"),InlineKeyboardButton("Desarrollador", url="https://t.me/Jorgebarba"),],[InlineKeyboardButton("grupo", url="https://t.me/termuxcomunidad")],])
    await message.reply_text(f"Hola! {messy} \nBot hecho por  @Jorgebarba\nUse /ayuda ver todos los comandos",reply_markup=keyboard,)
#ayuda
@app.on_message(filters.command("ayuda"))
async def ayuda(client, message):
    await message.reply_text("╔/start    - **Estado del Bot**.\n╠/ayuda  - **Muestra Este Mensaje**\n╠/bin       - **Informacion De un Bin**\n╠/chk      - **checker cc**\n╠/audio - **cancion de youtube**\n╚/video - **Video de Youtube** \nBy : @Jorgebarba")
#chk
@traced
@logged
@app.on_message(filters.command("chk"))
async def chk(client, message):
    await message.reply_text("**En Mantenimiento**")
#bin
@traced
@logged
@app.on_message(filters.command("video"))
def video(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 Buscando Video en Youtube...')
    ydl_opts = {"format": "webm"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('No se encontro nada\n**Ejemplo** `/video fabed`')
            return
    except Exception as e:
        m.edit(
            "✖️ Found Nothing. Sorry.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    m.edit("⏬ Descargando.")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎧 **Titulo**: [{title[:35]}]({link})\n⏳ **Duracion**: `{duration}`\n👁‍🗨 **Vistas**: `{views}`'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('❌ Error')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@traced
@logged
@app.on_message(filters.command("audio"))
def audio(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 Buscando Audio en Youtube...')
    ydl_opts = {"format": "m4a"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
         # resultados = YoutubeSearch(consulta, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # imprimir (resultados)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('No se encontro nada\n**Ejemplo** `/audio fabed`')
            return
    except Exception as e:
        m.edit(
            "✖️ Found Nothing. Sorry.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    m.edit("⏬ Descargando.")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎧 **Titulo**: [{title[:35]}]({link})\n⏳ **Duracion**: `{duration}`\n👁‍🗨 **Vistas**: `{views}`'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('❌ Error')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

print("\033[1;31mBot on\033[0m")


try:
    app.run()
except KeyboardInterrupt:
    print("\033[1;31mDetenido por el usuario\033[0m")
