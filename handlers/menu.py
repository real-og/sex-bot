from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from buttons import *
import logic


@dp.callback_query_handler(state=State.menu)
async def menu_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == get_random_pose_btn:
        image_name = logic.get_random_file()
        with open('images/' + image_name, 'rb') as file:
            await callback.message.answer_photo(file, caption='<i>' + image_name[:-4] + '</i>', reply_markup=kb.pose_card_kb)
        await State.checking_poses.set()
    elif callback.data == on_categories_btn:
        await callback.message.answer(texts.choose_category, reply_markup=kb.categories_kb)
        await State.choosing_category.set()
    elif callback.data == feed_back_btn:
        await callback.message.answer(texts.feedback_instruction, reply_markup=kb.single_menu_kb)
        await State.sending_feedback.set()
    elif callback.data == info_btn:
        await callback.message.answer(texts.info)
        await callback.message.answer(texts.menu, reply_markup=kb.menu_kb)    
        
    await callback.answer()
    