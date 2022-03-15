import asyncio
import datetime
import os
import sys
import time

from pyrogram import Client, filters
from pyrogram.types import Message

from .. import start_time, vcbot, HNDLR, SUDO_USERS

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["baby"], prefixes=HNDLR))
async def ping(_, e: Message):
    st = datetime.datetime.now()
    uptime = await get_time((time.time() - start_time))
    x = await e.reply_text("** 𝐓𝐫𝐨𝐧𝐢𝐱  !!**")
    et = datetime.datetime.now()
    pt = (et-st).microseconds / 1000
    await x.edit_text(f"𝐓𝐫𝐨𝐧𝐢𝐱 𝐍𝐚𝐚𝐦 𝐒𝐮𝐧𝐤𝐞 𝐅𝐥𝐨𝐰𝐞𝐫 𝐒𝐚𝐦𝐣𝐡𝐚 𝐊𝐲𝐚 🔥 𝐇𝐚𝐢 𝐌𝐚𝐢 𝐁𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐛𝐲 @𝐏_𝟒_𝐏𝐄𝐄𝐘𝐔𝐒𝐇")