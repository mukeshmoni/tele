import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Credentials:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8160540534:AAF8mZO0c9xkBYKsHRQavE2ap9eq8G3x-ug")# from @botfather
    API_ID = int(os.getenv("API_ID", "28338127"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH", "c4cb64de16a18f8685a31716a0e2480e")  # from https://my.telegram.org/apps
   
