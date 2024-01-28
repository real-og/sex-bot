from loader import dp, DESCRIPTIONS
from aiogram import types
from aiogram.types import InputMediaPhoto
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
        folder_name += 'classic/'

    elif category == advanced_btn:
        index = int(data.get('advanced_index', -1))
        folder_name += 'advanced/'

    elif category == exotic_btn:
        index = int(data.get('exotic_index', -1))
        folder_name += 'exotic/'

    image_name, new_index = logic.get_next_by_categories(category, index)
    
    with open(folder_name + image_name, 'rb') as file:
        await callback.message.answer_photo(file, caption='<i>' + image_name[:-4] + '</i>', reply_markup=kb.pose_card_with_category_kb)
    

    if category == classic_btn:
        await state.update_data(classic_index=new_index)
    elif category == advanced_btn:
        await state.update_data(advanced_index=new_index)
    elif category == exotic_btn:
        await state.update_data(exotic_index=new_index)
    
    await State.checking_poses_with_categories.set()
    await callback.answer()


@dp.callback_query_handler(state=State.checking_poses_with_categories)
async def pose_handler(callback: types.CallbackQuery, state: FSMContext):

    if callback.data == back_to_menu_btn:
        await callback.message.answer(texts.menu, reply_markup=kb.menu_kb)
        await State.menu.set()
        await callback.answer()
        return
    
    if callback.data == desc_btn:
        name = callback.message.caption.split('\n')[0]
        caption = name + '\n\n' + DESCRIPTIONS[name]
        try:
            if len(callback.message.caption.split('\n')) > 1:
                await callback.message.edit_caption('<i>' + name + '</i>', reply_markup=kb.pose_card_with_category_kb)
            else:
                await callback.message.edit_caption('<i>' + caption + '</i>', reply_markup=kb.pose_card_with_category_kb)
        except:
            await callback.message.answer(texts.error)
        await callback.answer()
        return

    
    data = await state.get_data()
    category = data.get('category')
    folder_name = 'categories/'
    if category == classic_btn:
        index = data.get('classic_index', 0)
        folder_name += 'classic/'
    elif category == advanced_btn:
        index = data.get('advanced_index', 0)
        folder_name += 'advanced/'
    elif category == exotic_btn:
        index = data.get('exotic_index', 0)
        folder_name += 'exotic/'

    if callback.data == next_btn:
        image_name, new_index = logic.get_next_by_categories(category, index)   
    elif callback.data == prev_btn:
        image_name, new_index = logic.get_prev_by_categories(category, index)

    with open(folder_name + image_name, 'rb') as file:
        await callback.message.edit_media(InputMediaPhoto(file, caption='<i>' + image_name[:-4] + '</i>'), reply_markup=kb.pose_card_with_category_kb)

    if category == classic_btn:
        await state.update_data(classic_index=new_index)
    elif category == advanced_btn:
        await state.update_data(advanced_index=new_index)
    elif category == exotic_btn:
        await state.update_data(exotic_index=new_index)
    await callback.answer()

