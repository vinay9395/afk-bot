import os

if not os.environ.get("TOKEN") or not os.environ.get("DATABASE_URL"):
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

from telegram.ext import filters

BOT_TOKEN = os.environ.get("TOKEN")
DB_URI = os.environ.get("DATABASE_URL")
SUDO_USERS = [
    5086819565
]
SUDO = filters.User(SUDO_USERS)
LOG_CHAT = -1002154467227
