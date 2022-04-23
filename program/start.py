from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["/start", f"/start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**╖ • مرحبا بك في سورس اندرويد**

**╢ • لتشغيل الموسيقي في المحادثات الصوتيه**

**╢ • اضفني مشرف واكتب (انضم)**

**╜ • الحساب المساعد @{ ASSISTANT_NAME}**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "أضف لبوت لمجموعتك ✅",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("<<طريقة التفعيل>>", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("<<الاوامر >>", callback_data="cbcmds"),
                    InlineKeyboardButton("<<المطور >>", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "<<جروب الدعم>>", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "SOURCE 🚨", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝘼 𝙉 𝘿 𝙍 𝙊 𝙄 𝘿 ¦ اندرويد ", url="https://t.me/U_Androld"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(command(["/source", f"/source@{BOT_USERNAME}", "السورس", "سورس اغاني"]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝘼 𝙉 𝘿 𝙍 𝙊 𝙄 𝘿 ¦ اندرويد ", url=f"https://t.me/U_Androld"),
                InlineKeyboardButton(
                    "SOURCE 🚨", url=f"https://t.me/UU_and_rold"
                ),
            ]
        ]
    )

    alive = f"**هلو {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ يعمل البوت بشكل طبيعي\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**شكرًا لإضافتي هنا ، لتشغيل الفيديو والموسيقى على دردشة الفيديو الخاصة بمجموعتك** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )

@Client.on_message(command(["/help", f"/mplay@{BOT_USERNAME}", "الاوامر", "اوامر"]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("SOURCE ", url=f"https://t.me/Q_o_ll"),
                InlineKeyboardButton(
                    "SOURCE 🚨", url=f"https://t.me/UU_and_rold"
                ),
            ]
        ]
    )

    alive = f"""
 » `/play` (song name/link) - play music on video chat
» `/mplay` (song name/link) - play music on video chat
» `/vplay` (video name/link) - play video on video chat
» `/vstream` - play live video from yt live/m3u8
» `/playlist` - show you the playlist
» `/video` (query) - download video from youtube
» `/song` (query) - download song from youtube
» `/lyric` (query) - scrap the song lyric
» `/search` (query) - search a youtube video link
» `/ping` - show the bot ping status
» `/uptime` - show the bot uptime status
» `/alive` - show the bot alive info (in group)""",
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["/ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `البينج مظبوط !!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["/uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )

@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **شكرا لإضافتي إلى المجموعة !**\n\n"
                "**قم بترقيتي كمسؤول عن المجموعة ، وإلا فلن أتمكن من العمل بشكل صحيح ، ولا تنسى الكتابة /userbotjoin لدعوة المساعد.**\n\n"
                "**Once done, type** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("SOURCE 🚨", url=f"https://t.me/UU_and_rold"),
                            InlineKeyboardButton("𝘼 𝙉 𝘿 𝙍 𝙊 𝙄 𝘿 ¦ اندرويد ", url=f"https://t.me/U_Androld")
                        ],

                          [       
                            InlineKeyboardButton("<<HELP>>", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
