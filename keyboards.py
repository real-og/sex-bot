from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from buttons import *

# begin_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)


menu_kb = InlineKeyboardMarkup()
menu_kb.add(InlineKeyboardButton(get_random_pose_btn, callback_data=get_random_pose_btn))
menu_kb.add(InlineKeyboardButton(info_btn, callback_data=info_btn))

