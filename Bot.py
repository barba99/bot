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
async def binio(message: types.Message
    await message.answer_chat_action('typing'
    ID = message.from_user.
    FIRST = message.from_user.first_name
    BIN = message.text[len('/bin '):]
    if len(BIN) < 6:
        return await message.reply(
                   'Send bin not ass'
        )
    r = requests.get(
               f'http://binchk-api.vercel.app/bin={BIN}'
    ).json()
    INFO = f'''
BIN⇢ <code>{BIN}</code>
Marka⇢ <u>{r["brand"]}</u>
Tip⇢ <u>{r["type"]}</u>
Seviye⇢ <u>{r["level"]}</u>
Banka⇢ <u>{r["bank"]}</u>
Telefon⇢ <u>{r["phone"]}</u>
Para birimi⇢ <u>{r["currency"]}</u>
Ülke⇢ <u>{r["country"]}({r["code"]})[{r["flag"]}]</u>
GÖNDEREN: <a href="tg://user?id={ID}">{FIRST}</a>
BOT⇢ @{BOT_USERNAME}
SAHİBİ⇢ <a href="tg://user?id={OWNER}">LINK</a>
'''
    await message.reply(INFO
print("Corrió con éxito")

Bot.run()


