#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("HELP", callback_data="help_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "π¬ π²πΈπ½π΄π·ππ±", url="https://t.me/cinehub_family")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "π¬ π²πΈπ½π΄π·ππ±", url="https://t.me/cinehub_family")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE", url="https://github.com/TroJanzHEX/Auto-Filter-Bot")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

    @Client.on_message(filters.command('sinhala_sub'))
async def play(bot, message):
    msg = await message.reply("πΏ **ΰ·ΰ·ΰΆΰ·ΰΆ½ ΰΆΰΆ΄ΰ·ΰ·ΰΆ»ΰ·ΰ·ΰ· **\n\n\nπ¬ ΰΆΰΆ±ΰ·ΰΆ± ΰΆΰΆ­ΰ·ΰΆ±ΰ· ΰΆΰΆΊΰΆ½ΰΆΰ· ΰΆ΄ΰ·ΰ·ΰ·ΰ·ΰΆ§ ΰΆΰΆ΄ΰ· ΰ·ΰ·ΰΆΰ·ΰΆ½ ΰΆΰΆ΄ΰ·ΰ·ΰΆ»ΰ·ΰ·ΰ· ΰΆΆΰ·ΰΆ§ΰ· ΰΆΰ·ΰΆ±ΰ·ΰΆΰ·ΰ·ΰΆ­ΰ· ΰ·ΰΆ―ΰΆ½ΰ· ΰΆ­ΰ·ΰΆΊΰ·ΰΆ±ΰ·ΰ· \n\n @sub_searcheer_bot ΰΆ§ α΄α΄α΄ Ιͺα΄ ΰΆΰΆΰ· ΰ·ΰ· sα΄ΚΙͺα΄s ΰΆΰΆΰ· Name ΰΆΰΆ English ΰ·ΰΆ½ΰ·ΰΆ±ΰ· type ΰΆΰΆ»ΰΆ± ΰΆΰΆΰΆΊΰ· \n\n\nβ‘ **ΰ·ΰ·ΰΆΰ·ΰΆ½ ΰΆΰΆ΄ΰ·ΰ·ΰΆ»ΰ·ΰ·ΰ·; @sub_searcher_bot** \n\n\n<a href='https://t.me/sub_searcher_bot'>π€</a> | Powered By; Β© <a href='https://t.me/cinehub_family'>π²πΈπ½π΄π·ππ±</a>", quote=True)
    msg = await message.reply("π")
