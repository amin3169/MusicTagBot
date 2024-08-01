from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from FallenMusic import BOT_USERNAME
import config

close_key = InlineKeyboardMarkup([[InlineKeyboardButton(text="🎵 ʙᴀĞʟᴀʏɪʀ 🎵", callback_data="close")]])

buttons = InlineKeyboardMarkup(
          [[
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
          ]])

gp_buttons = [
    [
     InlineKeyboardButton(text="Əmrlər Və Köməklər", callback_data="fallen_help")
    ],[
     InlineKeyboardButton(text="Kanal", url=config.SUPPORT_CHANNEL),
     InlineKeyboardButton(text="Dəstək", url=config.SUPPORT_CHAT),
    ],[
     InlineKeyboardButton(text="Qruplara Əlavə Et",url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)
    ],[
     InlineKeyboardButton(text="👨‍💻 Bot Sahibi👨‍💻", user_id=config.OWNER_ID),
    ],]

pm_buttons = [
    [
     InlineKeyboardButton(text="Əmrlər Və Köməklər", callback_data="fallen_help")
    ],[
     InlineKeyboardButton(text="Kanal", url=config.SUPPORT_CHANNEL),
     InlineKeyboardButton(text="Dəstək", url=config.SUPPORT_CHAT),
    ],[
     InlineKeyboardButton(text="Qruplara Əlavə Et",url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)
    ],[
     InlineKeyboardButton(text="Bot Sahibi", user_id=config.OWNER_ID),
    ],]

helpmenu = [
    [
    InlineKeyboardButton(text="Səsli Əmrləri",callback_data="fallen_cb help",),
    InlineKeyboardButton(text="Tağ Əmrləri",callback_data="tagbutton",)
    ],[
    InlineKeyboardButton(text="Admin Əmrləri", callback_data="fallen_cb sudo"),
    InlineKeyboardButton(text="Sahib Əmrləri", callback_data="fallen_cb owner"),
    ],[
    InlineKeyboardButton(text="◄◐ Geri", callback_data="fallen_home"),
    InlineKeyboardButton(text="Menyunu Bağlayır", callback_data="close"),
    ],]

help_back = [
    [
    InlineKeyboardButton(text="◄◐ Geri", callback_data="fallen_help"),
    InlineKeyboardButton(text="🗑 Menyunu Bağlayır", callback_data="close"),
    ],]
