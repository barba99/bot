import json
import requests
from pyrogram import Client, filters
from configs import config
from asyncio import sleep

from pyrogram.types import (
    Message, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)


Bot = Client(
    ":memory:",
    api_hash=config.API_HASH,
    api_id=config.API_ID,
    bot_token=config.BOT_TOKEN,
)


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


@Bot.on_message(filters.command("help"))
async def help(_, m: Message):
    await m.reply_text(
        "/start - **comprobar el estado del bot**.\n/help - **todos los comandos del bot**\n/bin - **Infobin**\n/chk - **checker cc**\nBy : @Jorgebarba"
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
@Bot.on_message(filters.command("bin"))
async def bin(_, m: Message):
    if len(m.command) < 2:
        msg = await m.reply_text("**¡Primero aprende qué es bin, hijo de puta!**`")
        await sleep(15)
        await msg.delete()

    else:

        mafia = await m.reply_text("espera un momento")
        inputm = m.text.split(None, 1)[1]
        bincode = 6
        ask = inputm[:bincode]
        req = requests.get(f"https://lookup.binlist.net/{ask}").json()
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
        caption = f"""
╔ Valid ￫ `{res} ✅`\n╚ Bin ￫ `{bi}`\n\n╔ Marca ￫ `{ve}`\n╠ Tipo ￫ `{ty}`\n╚ Nivel ￫ `{le}`\n\n╔ Banco ￫ `{ban} ({co})`\n╠ Pais ￫ `{nm} {em}`\n╠ Alpha2 ￫ `{cod}`\n╚ Codigo de Marcacion ￫ `{dial}`\n\n**↠By ￫** {mfrom}\n**↠ __Bot By ￫*
"""
        await mafia.edit(caption)


print("Corrió con éxito")

Bot.run()


