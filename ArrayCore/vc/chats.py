from pyrogram import filters
from pyrogram.types import Message

from .. import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, HNDLR,
                    SUDO_USERS, vcbot)


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
async def join(_, e: Message):
    inp = e.text[6:]
    count = 0
    if not inp:
        return await e.reply_text("Chat Username Ya Link Chhaiye Grp Ka Bsdk.")
    if inp.isnumeric():
        return await e.reply_text("ɪᴛɴᴇ ʙᴜʀᴇ ᴅɪɴ ɴᴀɪ ᴀᴀʏᴇ ᴋɪ ᴄʜᴀᴛ ɪᴅ sᴇ ᴊᴏɪɴ ᴋʀᴜ ʙɪsɪ 🔥")
    try:
        if Venom1:
            await Venom1.join_chat(inp)
            count += 1
        if Venom2:
            await Venom2.join_chat(inp)
            count += 1
        if Venom3:
            await Venom3.join_chat(inp)
            count += 1
        if Venom4:
            await Venom4.join_chat(inp)
            count += 1
        if Venom5:
            await Venom5.join_chat(inp)
            count += 1
        if Venom6:
            await Venom6.join_chat(inp)
            count += 1
        if Venom7:
            await Venom7.join_chat(inp)
            count += 1
        if Venom8:
            await Venom8.join_chat(inp)
            count += 1
        if Venom9:
            await Venom9.join_chat(inp)
            count += 1
        if Venom10:
            await Venom10.join_chat(inp)
            count += 1
        if Venom11:
            await Venom11.join_chat(inp)
            count += 1
        if Venom12:
            await Venom12.join_chat(inp)
            count += 1
        if Venom13:
            await Venom13.join_chat(inp)
            count += 1
        if Venom14:
            await Venom14.join_chat(inp)
            count += 1
        if Venom15:
            await Venom15.join_chat(inp)
            count += 1
        await e.reply_text(f"**ᴏʜᴏ ᴊᴏɪɴ ʜᴏɢʏᴀ ʙɪsɪ** `{count}` **ɪᴛɴᴇ ᴀᴄᴄᴏᴜɴᴛs sᴇ**")
    except Exception as ex:
        await e.reply_text(f"**ERROR ᴀᴀɢʏᴀ ʙᴄ:** \n\n{str(ex)}")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
async def leave(_, e: Message):
    inp = e.text[7:]
    count = 0
    if not inp:
        return await e.reply_text("ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ʏᴀ ᴘʜɪʀ ɪᴅ ʜɪ ᴅᴇᴅᴇ ʟᴇᴀᴠᴇ ᴋʀʟᴜɴɢᴀ")
    try:
        if Venom1:
            await Venom1.leave_chat(inp)
            count += 1
        if Venom2:
            await Venom2.leave_chat(inp)
            count += 1
        if Venom3:
            await Venom3.leave_chat(inp)
            count += 1
        if Venom4:
            await Venom4.leave_chat(inp)
            count += 1
        if Venom5:
            await Venom5.leave_chat(inp)
            count += 1
        if Venom6:
            await Venom6.leave_chat(inp)
            count += 1
        if Venom7:
            await Venom7.leave_chat(inp)
            count += 1
        if Venom8:
            await Venom8.leave_chat(inp)
            count += 1
        if Venom9:
            await Venom9.leave_chat(inp)
            count += 1
        if Venom10:
            await Venom10.leave_chat(inp)
            count += 1
        if Venom11:
            await Venom11.leave_chat(inp)
            count += 1
        if Venom12:
            await Venom12.leave_chat(inp)
            count += 1
        if Venom13:
            await Venom13.leave_chat(inp)
            count += 1
        if Venom14:
            await Venom14.leave_chat(inp)
            count += 1
        if Venom15:
            await Venom15.leave_chat(inp)
            count += 1
        await e.reply_text(f"**ʜᴜʜ ʙᴄ ʙᴀᴄʜ ɢʏᴀ ʏᴇ ᴋɪᴍᴅ** `{count}` **ʟᴇᴀᴠᴇᴅ ᴛʜɪs ғᴜᴄᴋɪɴɢ ɢʀᴘ**")
    except Exception as ex:
        await e.reply_text(f"**ERROR ᴀᴀɢʏᴀ ʙᴄ:** \n\n{str(ex)}")
