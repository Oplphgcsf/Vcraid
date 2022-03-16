import asyncio
import datetime
import os
import sys
import time

from pyrogram import Client, filters
from pyrogram.types import Message

from .. import start_time, vcbot, HNDLR, SUDO_USERS

async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time
    
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["baby"], prefixes=HNDLR))
async def ping(_, e: Message):
    st = datetime.datetime.now()
    uptime = await get_time((time.time() - start_time))
    x = await e.reply_text("** 𝐓𝐫𝐨𝐧𝐢𝐱  !!**")
    et = datetime.datetime.now()
    pt = (et-st).microseconds / 1000
    await x.edit_text(f"𝐓𝐫𝐨𝐧𝐢𝐱 𝐍𝐚𝐚𝐦 𝐒𝐮𝐧𝐤𝐞 𝐅𝐥𝐨𝐰𝐞𝐫 𝐒𝐚𝐦𝐣𝐡𝐚 𝐊𝐲𝐚 🔥 𝐇𝐚𝐢 𝐌𝐚𝐢 𝐁𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐛𝐲 @𝐏_𝟒_𝐏𝐄𝐄𝐘𝐔𝐒𝐇")
