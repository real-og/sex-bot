from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import buttons

# begin_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)


menu_kb = InlineKeyboardMarkup()
menu_kb.add(InlineKeyboardButton(buttons.get_random_pose_btn, callback_data='random_pose'))
menu_kb.add(InlineKeyboardButton(buttons.info_btn, callback_data='info'))

