from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","DarkxMusic")
BOT_USERNAME = getenv("BOT_USERNAME", "K61TBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Mahmod777777")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "E_L_R_A_S_A_M")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b144db94dc0db0fd86526.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e68855e3be3191ca84624.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5520469387").split()))
