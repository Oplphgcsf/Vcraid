#@TheVenomXD randi

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from .. import vcbot, SUDO_USERS, HNDLR, hl, START_VID, ALIVE_PIC

# @vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["start"], prefixes=HNDLR))
# async def start(_, e: Message):
   # video=START_VID,
  # await vcbot.send_video(e.chat.id, video, f"Vc Raid Bot Is Working Fine. \nSend `{hl}help` To Know Your Commands. \n\n< Powered By @ArrayCore >")

Array = ALIVE_PIC or "https://te.legra.ph/file/045d419efd37fd56e8562.jpg"
Hn = "/"
@vcbot.on_message(filters.private & filters.incoming & filters.command(['start'], prefixes=Hn))
async def _start(_, ok: Message):
        Array_msg = f"**Hello [{ok.from_user.first_name}](tg://user?id={ok.from_user.id}) !** \n\n __ • I'm Tronix Vc King 👑 An Advance And Simple Group Voice Call Bot__ \n\n **Click Below Buttons for More Info**"
        await ok.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="tg://settings"),
                    InlineKeyboardButton(
                        "• Support •", url="tg://settings")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="tg://settings")
                ]]
            ))
