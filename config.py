import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "SONG FIRE")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Q_o_ll")
ALIVE_NAME = getenv("ALIVE_NAME", "Help_boot")
BOT_USERNAME = getenv("BOT_USERNAME", "Q_o_ll_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Help_boot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Kn_panda")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CH_SUR")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fa0abbdfcfe3936c6a818.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Not102/nice")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/fa0abbdfcfe3936c6a818.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/fa0abbdfcfe3936c6a818.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/fa0abbdfcfe3936c6a818.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/fa0abbdfcfe3936c6a818.jpg")
