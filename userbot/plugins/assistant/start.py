# Copyright (C) Midhun KM 
# 
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot 🚶

from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
from googletrans import Translator
import re
from math import ceil
from userbot.plugins import inlinestats
from telethon import custom, events, Button
from userbot import CMD_LIST
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
from userbot import Lastupdate, bot
from userbot.plugins.helper_sql.botusers_sql import add_user_to_db
@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    vent = event.chat_id
    starttext = ("Hi! this is An Assistant Bot For My [Owner] ")
    if event.from_id == bot.uid:
        await tgbot.send_message(
           vent,
           message="Hi Master, It's Me Your Assistant.",
           buttons = [
           [Button.url("Repo?", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
            ]
           )
    else:
        await tgbot.send_message(
           event.chat_id,
           message=starttext,
           link_preview=False,
           buttons = [
           [custom.Button.inline("Deploy your Friday 🇮🇳", data="deploy")],
           [Button.url("Help Me ❓", "t.me/Fridayot")]
       ]
      )


# Data's

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
        await event.delete()
        if event.query.user_id is not bot.uid:
            await tgbot.send_message(
                event.chat_id,
                message="You Can Deploy Friday In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own Assistant Bot. \nThank You For Contacting Me.",
                buttons = [
                [Button.url("Deploy Tutorial 📺", "https://youtu.be/xfHcm_e92eQ")],
                [Button.url("Need Help ❓", "t.me/FridaySupportOfficial")]
                 ]
                )

# Bot Permit.
@tgbot.on(events.NewMessage(
    incoming=True,
    func=lambda e: (
        e.is_private
    )
))
async def all_messages_catcher(event):
    sedlyfvro = event.chat_id
    if event.chat_id == bot.uid:
        pass
    else:
        sed = await event.forward_to(bot.uid)


# Add User To Database ,Later For Broadcast Purpose
# (C) @SpecHide
add_user_to_db(
        sed.message_ids,
        sed.from_id,
        sed.message_ids
    )
