from telethon import TelegramClient
import config
import logging

logging.basicConfig(level=logging.INFO,format='%(name)s - [%(levelname)s] - %(message)s')
LOGGER = logging.getLogger(__name__)
api_id = config.API_ID
api_hash = config.API_HASH
bot_token = config.BOT_TOKEN
dejavu = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
print(">> Bot işləyir narahat olmayın.\n\n@DejavuTeam & @DejavuSuopport Məlumat almaq üçün <<")
dejavu.run_until_disconnected()
