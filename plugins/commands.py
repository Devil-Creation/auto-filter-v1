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
                            "🎬 🄲🄸🄽🄴🄷🅄🄱", url="https://t.me/cinehub_family")
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
                            "🎬 🄲🄸🄽🄴🄷🅄🄱", url="https://t.me/cinehub_family")
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
    msg = await message.reply("🍿 **සිංහල උපසිරැසි **\n\n\n🎬 ඔන්න ඉතින් ඔයලගෙ පහසුවට අපි සිංහල උපසිරැසි බොට් කෙනෙක්වත් හදලා තියෙනවා \n\n @sub_searcheer_bot ට ᴍᴏᴠɪᴇ එකේ හෝ sᴇʀɪᴇs එකේ Name එක English වලින් type කරන එකයි \n\n\n⚡ **සිංහල උපසිරැසි; @sub_searcher_bot** \n\n\n<a href='https://t.me/sub_searcher_bot'>🤖</a> | Powered By; © <a href='https://t.me/cinehub_family'>🄲🄸🄽🄴🄷🅄🄱</a>", quote=True)
    msg = await message.reply("😇")
