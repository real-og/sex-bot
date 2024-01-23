from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from buttons import *

# begin_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)


menu_kb = InlineKeyboardMarkup()
menu_kb.add(InlineKeyboardButton(get_random_pose_btn, callback_data=get_random_pose_btn))
menu_kb.add(InlineKeyboardButton(feed_back_btn, callback_data=feed_back_btn))
menu_kb.insert(InlineKeyboardButton(info_btn, callback_data=info_btn))

single_menu_kb = InlineKeyboardMarkup()
single_menu_kb.add(InlineKeyboardButton(back_to_menu_btn, callback_data=back_to_menu_btn))




pose_card_kb = InlineKeyboardMarkup()
pose_card_kb.add(InlineKeyboardButton(back_to_menu_btn, callback_data=back_to_menu_btn))
pose_card_kb.insert(InlineKeyboardButton(more_pose_btn, callback_data=more_pose_btn))



