import os

if not os.environ.get("TOKEN") or not os.environ.get("DATABASE_URL"):
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

from telegram.ext import Filters

BOT_TOKEN = os.environ.get("7236081501:AAHyQmRW45_VKsl_Rglo42p63CmwIEMxfHw")
DB_URI = os.environ.get("JsUNRj65LRfE9tFh
godpresentfr
mongodb+srv://godpresentfr:JsUNRj65LRfE9tFh@vanshfr.p4mhoke.mongodb.net/?retryWrites=true&w=majority&appName=Vanshfr")
SUDO_USERS = [
    5086819565
]
SUDO = Filters.user(SUDO_USERS)
LOG_CHAT = -1002154467227
