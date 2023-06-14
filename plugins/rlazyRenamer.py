from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import humanize
from info import ADMINS, FLOOD, LAZY_MODE, LAZY_RENAMERS
import random


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    if LAZY_MODE:
        if message.from_user.id in ADMINS:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size)
            filename = file.file_name
            text = f"\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should I do with this file?**\n\n**🎞File Name**: `{filename}`\n\n⚙️**File Size**: `{filesize}`"
            buttons = [
                [InlineKeyboardButton("📝✧✧ Start renaming ✧✧📝", callback_data="rename")],
                [InlineKeyboardButton("⨳ Close ⨳", callback_data="cancel")]
            ]
            await message.reply_text(text=text, reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(buttons))

        elif message.from_user.id in LAZY_RENAMERS:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size)
            filename = file.file_name
            try:
                text = f"\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should I do with this file?**\n\n**🎞File Name**: `{filename}`\n\n⚙️**File Size**: `{filesize}`"
                buttons = [
                    [InlineKeyboardButton("📝✧✧ Start renaming ✧✧📝", callback_data="rename")],
                    [InlineKeyboardButton("⨳ Close ⨳", callback_data="cancel")]
                ]
                await message.reply_text(text=text, reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(buttons))
                await sleep(FLOOD)
            except FloodWait as e:
                await sleep(e.value)
                text = f"\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should I do with this file?**\n\n**🎞File Name**: `{filename}`\n\n⚙️**File Size**: `{filesize}`"
                buttons = [
                    [InlineKeyboardButton("📝✧✧ Start renaming ✧✧📝", callback_data="rename")],
                    [InlineKeyboardButton("⨳ Close ⨳", callback_data="cancel")]
                ]
                await message.reply_text(text=text, reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(buttons))
            except:
                pass
        else:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size)
            filename = file.file_name
            text = f"\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should I do with this file?**\n\n**🎞File Name**: `{filename}`\n\n⚙️**File Size**: `{filesize}`"
            buttons = [
                [InlineKeyboardButton("📝✧✧ Start renaming ✧✧📝", callback_data="requireauth")],
                [InlineKeyboardButton("⨳ Close ⨳", callback_data="cancel")]
            ]
            await message.reply_text(text=text, reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return
