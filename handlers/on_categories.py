from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from buttons import *
import logic


@dp.callback_query_handler(state=State.choosing_category)
async def pose_handler(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data
    data = await state.get_data()
    await state.update_data(category=category)
    folder_name = 'categories/'
    if category == classic_btn:
        index = int(data.get('classic_index', -1))
        folder_name +='classic/'

    elif category == advanced_btn:
        index = int(data.get('advanced_index', -1))
        folder_name += 'advanced/'

    elif category == exotic_btn:
        index = int(data.get('exotic_index', -1))
        folder_name += 'exotic/'

    image_name = logic.get_next_by_categories(category, index)
    with open(folder_name + image_name, 'rb') as file:
        await callback.message.answer_photo(file, caption='<i>' + image_name[:-4] + '</i>', reply_markup=kb.pose_card_with_category_kb)
    await State.checking_poses_with_categories.set()
    await callback.answer()

