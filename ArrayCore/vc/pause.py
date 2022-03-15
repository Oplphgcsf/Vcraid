from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue
from .. import call_py1, vcbot, HNDLR, SUDO_USERS


@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["pause"], prefixes=HNDLR))
async def ping(_, e: Message):
    chat_id = e.chat.id
    if chat_id in QUEUE:
        try:
            await call_py1.pause_stream(chat_id)
            await e.reply_text(f"**ʟᴏ ʏᴀʜᴀ ʙʜɪ ᴘᴀᴜsᴇ ᴋɪᴍᴅ ᴋᴏ ɢᴀᴍɴᴅ ᴍᴀʀɴɪ ᴛʜɪ ʏᴀᴀʀ 🔥🔥:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**ERROR ᴀᴀɢʏᴀ ʙᴄ** \n`{e}`")
    else:
        await e.reply_text("**ᴋᴜᴄʜ ᴘʟᴀʏ ɴᴀ ʜᴏʀᴀ**")
      
