from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    menu = State()
    checking_poses = State()
    sending_feedback = State()
    choosing_category = State()
    checking_poses_with_categories = State()