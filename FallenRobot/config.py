class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25378186
    API_HASH = "b8f77d40f8f7b955f5d34c3539a0e287"

    CASH_API_KEY = "0XYNIGBARN825UR4"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://wfzwsndx:xNwxRIZIHhCJ2OtYOupsiKEEDz_TnyZP@silly.db.elephantsql.com/wfzwsndx"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001870229808)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://idmn1:idmn1@cluster0.vuda5r7.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/0503186cae8a355ef894b.jpg"

    SUPPORT_CHAT = "DanteXSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6686694921:AAHQrYTROu3dAYBZ5M7HM3aH_1vxDSb9mmY"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "AZ8RZLD3B2TS"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5527218059  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
