import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """ 👋☺️ʜɪ Hᴇʟʟᴏ ,

🔎 I Aᴍ  𝗗𝗕 𝗠𝗢𝗩𝗜𝗘 𝗙𝗜𝗟𝗘𝗦 𝗦𝗘𝗔𝗥𝗖𝗛 𝗕𝗢𝗧 🧐🕵️

Hᴇʀᴇ Yᴏᴜ Cᴀɴ Sᴇᴀʀᴄʜ Mᴏᴠɪᴇs Fɪʟᴇs Iɴ Iɴʟɪɴᴇ Mᴏᴅᴇ , Aɴᴅ Aʟsᴏᴏ I Aᴍ Pʀᴏᴠɪᴅᴇ Yᴏᴜ Sᴀᴍᴇ As Aᴜᴛᴏ Fɪʟᴛᴇʀs Iɴ Gʀᴏᴜᴘ Aɴᴅ Pʀɪᴠᴀᴛᴇ Mᴇssᴀɢᴇ Aʟsᴏᴏ ,🤩

🤔𝐇𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 !?🤯

🔘Pʀᴇss Tʜᴇ [ Sᴇᴀʀᴄʜ Mᴏᴠɪᴇs...] Bᴜᴛᴛᴏɴ ,

🔸ᴀɴᴅ Eɴᴛᴇʀ Uʀs Mᴏᴠɪᴇ Nᴀᴍᴇ Oʀ Mᴇᴅɪᴀ Nᴀᴍᴇ 

📝𝗡𝗼𝘁𝗲 :- Oɴʟʏ Eɴᴛᴇʀ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢs { Sᴀᴍᴇ Iɴ Gʀᴏᴜᴘ Aʟsᴏᴏ }

🔎𝗦𝗲𝗮𝗿𝗰𝗵 𝗙𝗼𝗿𝗺𝗮𝘁𝗲 :- [ Mᴏᴠɪᴇ Nᴀᴍᴇ ]( Mᴏᴠɪᴇ Yᴇᴀʀ )✔️

ᴏʀ Usᴇ  @imdb Lɪɴᴋ Tᴏ Pᴇʀғᴇᴄᴛ Mᴏᴠɪᴇ Sᴘᴇʟʟɪɴɢ.🏷️

🕵️ᴀɴᴅ Aғᴛᴇʀ Yᴏᴜ Gᴏᴛ Tʜᴇ Lɪɴᴋs Pʀᴇss Aɴʏ Oɴᴇ Bᴜᴛᴛᴏɴ, 

🧐ᴀɴᴅ Pʀᴇss Sᴛᴀʀᴛ Bᴜᴛᴛᴏɴ, Aɴᴅ Eɴᴊᴏʏ Tʜᴇ Mᴏᴠɪᴇ Fɪʟᴇ.🤩 

🤖𝐁𝐎𝐓𝐬 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 :- @DB_ROBOTS📡

🆕𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 :- @DB_HELPER """

START_MSG = environ.get('START_MSG', default_start_msg)
