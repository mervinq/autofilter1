from pyrogram import Client, filters
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            "⚠️ **Note: Mode active ✅**\n\n𝙶𝚒𝚟𝚎 𝚖𝚎 𝚊 𝚌𝚊𝚙𝚝𝚒𝚘𝚗 𝚝𝚘 𝚜𝚎𝚝.\n\n📝 **Example:** `/set_caption {filename}`"
        )
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("✅️ **Your Caption has been saved successfully!**")


@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)
    if not caption:
        return await message.reply_text("⚠️ **Note: Mode active ✅**\n\n😔**Sorry, no caption found...**😔")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("✅️ **Your Caption has been deleted successfully!**")


@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)
    if caption:
        await message.reply_text(f"⚠️ **Note: Mode active ✅**\n\n**Your Caption:**\n\n`{caption}`")
    else:
        await message.reply_text("😔**Sorry, no caption found...**😔")
