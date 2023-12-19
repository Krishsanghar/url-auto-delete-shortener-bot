import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('27180565,''))
API_HASH = environ.get('f5e58af893794d014273c52de9e58948''')
BOT_TOKEN = environ.get('6753973405:AAHD-fdfsKUu_S52FZScRxPaMgBct62xVUM,"")

#Port
PORT = environ.get("PORT", "8080")

# Bot settings
CACHE_TIME = int(environ.get('300', 300))
USE_CAPTION_FILTER = bool(environ.get('False', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/b806ad314d0c415571bde.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(6618248423) if id_pattern.search 6618248423) else admin for admin in environ.get('2001653136').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('6618248423, '1').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('2001653136').split()]
AUTH_USERS = (auth_users +6618248423) if auth_users else []
auth_channel = environ.get('6618248423','')
auth_grp = environ.get('6618248423')
AUTH_CHANNEL = int(6618248423) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('mongodb+srv://krish72:krish72@cluster0.rj1oic0.mongodb.net/?retryWrites=true&w=majority', "")
DATABASE_NAME = environ.get('Cluster0', "Cluster0")
COLLECTION_NAME = environ.get('python', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('6618248423, ''))
SUPPORT_CHAT = environ.get('6618248423', 'search_zone_support')
P_TTI_SHOW_OFF = is_enabled((environ.get('True', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('True")), False)
CUSTOM_FILE_CAPTION = environ.get( <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [GreyMatter's Bot](https://t.me/greymatter_bots)</b>")
BATCH_FILE_CAPTION = environ.get( <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [GreyMatter's Bot](https://t.me/greymatter_bots)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @GreyMatter_Bots")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("True"), True)
MAX_LIST_ELM = environ.get(None)
INDEX_REQ_CHANNEL = int(environ.get(,6618248423 ))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('6618248423')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get("True")), True)
PROTECT_CONTENT = is_enabled((environ.get("False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get("False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('mongodb+srv://krish72:krish72@cluster0.rj1oic0.mongodb.net/?retryWrites=true&w=majority', 'omegalinks.in')
URL_SHORTNER_WEBSITE_API = environ.get('mongodb+srv://krish72:krish72@cluster0.rj1oic0.mongodb.net/?retryWrites=true&w=majority')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('3000', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://youtu.be/A6_YkUKgbgo"

   # Custom Caption Under Button #
CAPTION_BUTTON = "Subscribe"
CAPTION_BUTTON_URL = "https://youtube.com/@GreyMattersYT"

   # Auto Delete For Bot Sending Files #
