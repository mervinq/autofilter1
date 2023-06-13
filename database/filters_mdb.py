import pymongo
from pyrogram import enums
from info import DATABASE_URI, DATABASE_NAME
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

myclient = pymongo.MongoClient(DATABASE_URI)
mydb = myclient[DATABASE_NAME]


async def add_filter(grp_id, text, reply_text, button_text, file_size, file_name):
    mycol = mydb[str(grp_id)]

    data = {
        'text': str(text),
        'reply': str(reply_text),
        'button': str(button_text),
        'file_size': str(file_size),
        'file_name': str(file_name)
    }

    try:
        mycol.update_one({'text': str(text)}, {"$set": data}, upsert=True)
    except:
        logger.exception('Some error occurred!', exc_info=True)


async def find_filter(group_id, name):
    mycol = mydb[str(group_id)]

    query = mycol.find({"text": name})
    try:
        for file in query:
            reply_text = file['reply']
            button_text = file['button']
            file_size = file['file_size']
            file_name = file['file_name']
            try:
                alert = file['alert']
            except:
                alert = None
        return reply_text, button_text, alert, file_size, file_name
    except:
        return None, None, None, None, None


async def get_filters(group_id):
    mycol = mydb[str(group_id)]

    texts = []
    query = mycol.find()
    try:
        for file in query:
            text = file['text']
            texts.append(text)
    except:
        pass
    return texts


async def delete_filter(message, text, group_id):
    mycol = mydb[str(group_id)]

    myquery = {'text': text}
    query = mycol.count_documents(myquery)
    if query == 1:
        mycol.delete_one(myquery)
        await message.reply_text(
            f"'`{text}`' deleted. I'll not respond to that filter anymore.",
            quote=True,
            parse_mode=enums.ParseMode.MARKDOWN
        )
    else:
        await message.reply_text("Couldn't find that filter!", quote=True)


async def del_all(message, group_id, title):
    if str(group_id) not in mydb.list_collection_names():
        await message.edit_text(f"Nothing to remove in {title}!")
        return

    mycol = mydb[str(group_id)]
    try:
        mycol.drop()
        await message.edit_text(f"All filters from {title} have been removed.")
    except:
        await message.edit_text("Couldn't remove all filters from the group!")
        return


async def count_filters(group_id):
    mycol = mydb[str(group_id)]

    count = mycol.count_documents({})
    return False if count == 0 else count


async def filter_stats():
    collections = mydb.list_collection_names()

    if "CONNECTION" in collections:
        collections.remove("CONNECTION")

    total_count = 0
    for collection in collections:
        mycol = mydb[collection]
        count = mycol.count_documents({})
        total_count += count

    total_collections = len(collections)

    return total_collections, total_count
