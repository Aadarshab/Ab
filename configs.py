import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "24236993"))
    API_HASH = os.getenv("API_HASH", "0a56df2f25eefcace1c2e8948106dd66")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6045872657:AAEz9NwDGtDvIQ9HP9ofGNkUaMhfGnKWhcw")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "Mdisk_movie_1bot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "BQBnZu7CaL9l2T133ZI6-pxHonhYRypH4iHmv9tNi4ZN8w4C6mdb4-P7LVhMgqJFKaiRjr8naL5sLhZSmnHTAB-2Ps0Oce2CRwj3s8zP0S6tuLxHWd9Zj6Cfa_QZhdoQ9qr2388UuK-Qhu-fImVcZjyabxZpuCsATpXyp9SHnHNDX8z9pg-fS2ctu9qkb7Drz67LMi1hYo6qOU5iss0I22FZAkOSVQge_ixdAKwB6k6iVTyA27VRWtaW9dnsWjrDGMCpoPDBTWgs-kj1Es0vlFgbbX14Nn2E1vn17znUNGvrhh-n4l1-JNxiNBdKglauhhk4-6UeMFFBiy1B-XK2fO94TvE8hgA")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001726693463")) 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisk_movie_1bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "1324432518"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "ab_cracker")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "abcracked_movie)
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", """**Hᴇʏ {}, 

I ᴀᴍ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Rᴏʙᴏᴛ 🔍.

I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Eᴠᴇʀʏ Mᴏᴠɪᴇ Iɴ Mᴅɪsᴋ Lɪɴᴋ 🔗

Jᴜsᴛ Tʏᴘᴇ ᴀ Mᴏᴠɪᴇ Nᴀᴍᴇ 🎬**""" ) 
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/7d357b72c29a6aa21fb78.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", """ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.

ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001711559487")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Movie:abmovieabmovie@cluster0.nvvmjvm.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001742165971"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "abcracked_movie")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 60))
    MDISK_API = os.getenv("MDISK_API", "x6DSI0QSU6rVSWemLmaJ")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! 

ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, 

i ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.

 🤖""" )
    ABOUT_WATCH_TEXT = """
ʜᴇʏ ʙᴜᴅᴅʏ, 

ᴍᴅɪsᴋ - ᴀɢᴀʀ ᴀᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴍᴅɪsᴋ ʟɪɴᴋ sᴇ ᴍᴏᴠɪᴇ ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴍᴅɪsᴋ ᴡᴀʟᴇ ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ 

"""