from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)


bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

HELP_TEXT = """
ʜᴇʏᴀ! {}
✘ Hello I Am Lucky The AI Based Chat Bot You Can Add Me In ChatGroup To Improve Your Group Reach 💕.
"""

@bot.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client, message):
        await message.reply_text(f"{HELP_TEXT}".format(message.from_user.mention()),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕 Add Me In Your Group", url=f"https://t.me/Thevocalsbot?startgroup=true")
                ]
           ]
        ),
    )


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

        chatdb = MongoClient(MONGO_URL)
        chatai = chatdb["Word"]["WordDb"]
        if not message.reply_to_message:
                await bot.send_chat_action(message.chat.id, "typing")
                is_chat = chatai.find({"word": message.text})
                K = [x['text'] for x in is_chat]
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text['check']
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if Yo != "sticker":
                        await message.reply_text(f"{hey}")
        if message.reply_to_message:            
                getme = await bot.get_me()
                bot_id = getme.id
                if message.reply_to_message.from_user.id == bot_id:                    
                        await bot.send_chat_action(message.chat.id, "typing")
                        is_chat = chatai.find({"word": message.text})
                        K = [x['text'] for x in is_chat]
                        hey = random.choice(K)
                        is_text = chatai.find_one({"text": hey})
                        Yo = is_text['check']
                        if Yo == "sticker":
                            await message.reply_sticker(f"{hey}")
                        if Yo != "sticker":
                                await message.reply_text(f"{hey}")
                if message.reply_to_message.from_user.id != bot_id:          
                        if message.sticker:
                            is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
                            if not is_chat:
                                chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
                        if message.text:                 
                            is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
                            if not is_chat:
                                chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

        chatdb = MongoClient(MONGO_URL)
        chatai = chatdb["Word"]["WordDb"]
        if not message.reply_to_message:
                await bot.send_chat_action(message.chat.id, "typing")
                is_chat = chatai.find({"word": message.sticker.file_unique_id})
                K = [x['text'] for x in is_chat]
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text['check']
                if Yo == "text":
                    await message.reply_text(f"{hey}")
                if Yo != "text":
                        await message.reply_sticker(f"{hey}")
        if message.reply_to_message:            
                getme = await bot.get_me()
                bot_id = getme.id
                if message.reply_to_message.from_user.id == bot_id:                    
                        await bot.send_chat_action(message.chat.id, "typing")
                        is_chat = chatai.find({"word": message.sticker.file_unique_id})
                        K = [x['text'] for x in is_chat]
                        hey = random.choice(K)
                        is_text = chatai.find_one({"text": hey})
                        Yo = is_text['check']
                        if Yo == "text":
                            await message.reply_text(f"{hey}")
                        if Yo != "text":
                                await message.reply_sticker(f"{hey}")
                if message.reply_to_message.from_user.id != bot_id:          
                        if message.text:
                            is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
                            if not is_chat:
                                toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
                        if message.sticker:                 
                            is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
                            if not is_chat:
                                chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               

@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):

        chatdb = MongoClient(MONGO_URL)
        chatai = chatdb["Word"]["WordDb"]
        if not message.reply_to_message: 
                await bot.send_chat_action(message.chat.id, "typing")
                is_chat = chatai.find({"word": message.text})
                K = [x['text'] for x in is_chat]
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text['check']
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if Yo != "sticker":
                        await message.reply_text(f"{hey}")
        if message.reply_to_message:            
                getme = await bot.get_me()
                bot_id = getme.id
                if message.reply_to_message.from_user.id == bot_id:                    
                        await bot.send_chat_action(message.chat.id, "typing")
                        is_chat = chatai.find({"word": message.text})
                        K = [x['text'] for x in is_chat]
                        hey = random.choice(K)
                        is_text = chatai.find_one({"text": hey})
                        Yo = is_text['check']
                        if Yo == "sticker":
                            await message.reply_sticker(f"{hey}")
                        if Yo != "sticker":
                                await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivatesticker(client: Client, message: Message):

        chatdb = MongoClient(MONGO_URL)
        chatai = chatdb["Word"]["WordDb"]
        if not message.reply_to_message:
                await bot.send_chat_action(message.chat.id, "typing")
                is_chat = chatai.find({"word": message.sticker.file_unique_id})
                K = [x['text'] for x in is_chat]
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text['check']
                if Yo == "text":
                    await message.reply_text(f"{hey}")
                if Yo != "text":
                        await message.reply_sticker(f"{hey}")
        if message.reply_to_message:            
                getme = await bot.get_me()
                bot_id = getme.id
                if message.reply_to_message.from_user.id == bot_id:                    
                        await bot.send_chat_action(message.chat.id, "typing")
                        is_chat = chatai.find({"word": message.sticker.file_unique_id})
                        K = [x['text'] for x in is_chat]
                        hey = random.choice(K)
                        is_text = chatai.find_one({"text": hey})
                        Yo = is_text['check']
                        if Yo == "text":
                            await message.reply_text(f"{hey}")
                        if Yo != "text":
                                await message.reply_sticker(f"{hey}")
       
bot.run()
