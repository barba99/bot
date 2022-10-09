import youtube_dl, time
from youtube_search import YoutubeSearch
import requests
import json
import requests
from pyrogram import Client, filters
from asyncio import sleep
import os
from pyrogram.types import (
    Message, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)
from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "808192"))
    API_HASH = getenv("API_HASH", "d2a1c1fe0d574f98068c63d4928aee8a")
    BOT_TOKEN = getenv("BOT_TOKEN", "1819174855:AAFdKupTR5oUEM6aitsduq8TVyLIBaa4lVs")

config = Config()

Bot = Client(
    ":memory:",
    api_hash=config.API_HASH,
    api_id=config.API_ID,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins"),
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
# import main

# @Client.on_message(filters.text & filters.private)
@Bot.on_message(filters.new_chat_members)
async def start(_, m: Message):
    await m.reply_text("Hola :)")

@Bot.on_message(filters.left_chat_member)
async def end(_, m: Message):
    await m.reply_text("Hasta nunca")

@Bot.on_message(filters.command("start"))
async def start(_, m: Message):
    messy = m.from_user.mention
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Soporte", url="https://t.me/d0b3rm4nn"),
                InlineKeyboardButton("Desarrollador", url="https://t.me/Jorgebarba"),
            ],
            [
                InlineKeyboardButton(
                    "grupo", url="https://t.me/termuxcomunidad"
                )
            ],
        ]
    )
    await m.reply_text(
        f"Hola! {messy} \nBot hecho por  @Jorgebarba\nUse /help ver todos los comandos",
        reply_markup=keyboard,
    )
@Bot.on_message(filters.command("sk"))
async def sk(_, m: Message):
    await m.reply_text(
        "**Under Maintainance"
    )

@Bot.on_message(filters.command("bin"))
async def bin(_, m: Message):
    if len(m.command) < 2:
        msg = await m.reply_text("*Bin no valido\n*ejemplo `*/bin 415233*'*`")
        await sleep(15)
        await msg.delete()

    else:

        mafia = await m.reply_text("Checking Bin, Hold On....")
        inputm = m.text.split(None, 1)[1]
        bincode = 6
        ask = inputm[:bincode]
        req = requests.get(f"https://bin-check-dr4g.herokuapp.com/api/{ask}").json()
        res = req["result"]

        if res == False:
            return await mafia.edit("❌ #INVALID_BIN \nTry Again ;)")
        da = req["data"]
        bi = da["bin"]
        ve = da["vendor"]
        ty = da["type"]
        le = da["level"]
        ban = da["bank"]
        co = da["country"]
        cc = da["countryInfo"]
        nm = cc["name"]
        em = cc["emoji"]
        cod = cc["code"]
        dial = cc["dialCode"]

        mfrom = m.from_user.mention
        caption = (f"""╔ Valid ￫ {res} ✅
╠ Bin ￫ {bi}
╠ Brand ￫ {ve}
╠ Type ￫ {ty}
╠ Level ￫ {le}
╠ Bank ￫ {ban}
╠ Country ￫ {nm} {em}
╠ codigo de area ￫ {dial}
╠ Alpha2 ￫ {cod}
↠ Checked By ￫ {mfrom}↠ __Bot By ￫ [HECKER]\n (t.me/fakehecker__""")
        await mafia.edit(caption)


@Bot.on_message(filters.command("help"))
async def help(_, m: Message):
    await m.reply_text(
        "/start - **comprobar el estado del bot**.\n/help - **todos los comandos del bot**\n/bin - **Infobin**\n/chk - **checker cc**\n/cancion ***cancion de youtube*** By : @Jorgebarba"
    )

@Bot.on_message(filters.command("sk"))
async def sk(_, m: Message):
    await m.reply_text(
        "**Under Maintainance"
    )
@Bot.on_message(filters.command("chk"))
async def chk(_, m: Message):
    if len(m.command) < 5:
        msg = await m.reply_text("Ingrese un CC válido")
        await sleep(999999999)
        await msg.delete()
      
    else: 

        mafia = await m.reply_text("CC -» N/A\nSTATUS -» APROBADO ✅\nResponse -» SUCCESSFULLY CHARGED $1\nGATE -» STRIPE CHARGE\nRISK  -» HIGHEST \nREQUEST BY -» /{mpfrom}\nBOT BY -» @fakehecker")




@Bot.on_message(filters.command("start"))
async def help(_, m: Message):
    await m.reply_text(
        "/start - **Para comprobar el estado del bot**.\n/iniciar - **Para verificar los comandos del bot**\n/bin Query - **To check Bin\n/chk - **Stripe CHARGE\n")

@Bot.on_message(filters.command(['cancion']))
def cancion(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 Searching the song...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
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
            m.edit('Found nothing. Try changing the spelling a little.')
            return
    except Exception as e:
        m.edit(
            "✖️ Found Nothing. Sorry.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    m.edit("⏬ Downloading.")
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




@Bot.on_message(filters.command("gen"))
async def gen(_, m: Message):
    try:
        banned_bins = open('files/bannedbin.txt', 'r').readlines()
        verified_gps = open('files/groups.txt', 'r').readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text= group_not_allowed,reply_to_message_id=message.message_id)
        else:
            if message.reply_to_message is not None:
                message.text = message.reply_to_message.text
            text = f"""<b>WAIT FOR RESULTS</b>"""
            msg = await message.reply_text(text=text,reply_to_message_id=message.message_id)
            await Client.send_chat_action(message.chat.id, "typing")
            find = maindb.find_one({"_id": message.from_user.id})
            if isinstance(find, type(None)) == True:
                await msg.edit_text(use_not_registered)
            elif find['status'] == "F" and message.chat.type == 'private':
                await msg.edit_text(buy_premium)
            else:
                input = re.findall(r"[0-9]+", message.text)
                if len(input) == 0:
                    await msg.edit_text("Your Bin Is Empty")
                if len(input) == 1:
                    cc = input[0]
                    mes = 'x'
                    ano = 'x'
                    cvv = 'x'
                elif len(input[0]) < 6 or len(input[0]) > 16:
                    await msg.edit_text("Your Bin Is Incorrect")
                if len(input) == 2:
                    cc = input[0]
                    mes = input[1]
                    ano = 'x'
                    cvv = 'x'
                if len(input) == 3:
                    cc = input[0]
                    mes = input[1]
                    ano = input[2]
                    cvv = 'x'
                if len(input) == 4:
                    cc = input[0]
                    mes = input[1]
                    ano = input[2]
                    cvv = input[3]
                else:
                    if len(cc) > 15:
                        await msg.edit_text("Your Bin Is Invalid.")
                    else:
                        # lista = cc + "|" + mes + "|" + ano + "|" + cvv
                        bin = cc[:6]
                        res = requests.get("https://jocastabins.herokuapp.com/api/" + bin)
                        if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
                            await msg.edit_text("Your Bin Is Invalid.")
                        elif str(bin) + "\n"in banned_bins or "PREPAID" in res.text:
                            await msg.edit_text("Your Bin Is Banned.")
                        else:
                            bin_data = json.loads(res.text)
                            cc_gen(cc,mes,ano,cvv)
                            cards = ''.join(ccs)
                            ccs.clear()
                            text = f"""
<b>〄</b> CC GENRATOR
<b>○</b> YOUR DATA = {cc}|{mes}|{ano}|{cvv}.
<b>○</b> BANK INFO: <b>{bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})</b>
<b>○</b> BIN INFO: <code>{bin}</code> - <b>{bin_data['data']['level']}</b> - <b>{bin_data['data']['type']}</b>

<code>{cards} </code>"""       
                            buttons = [[InlineKeyboardButton('GEN AGAIN', callback_data='gen')]]   
                            reply_markup = InlineKeyboardMarkup(buttons)
                            await msg.edit_text(text,reply_markup=reply_markup)
    except Exception as e:
        print(e)


print("Corrió con éxito")

try:
    Bot.run()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("adios")
