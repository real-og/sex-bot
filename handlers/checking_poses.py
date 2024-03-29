from loader import dp, DESCRIPTIONS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from buttons import *
import logic


@dp.callback_query_handler(state=State.checking_poses)
async def pose_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == back_to_menu_btn:
        await callback.message.answer(texts.menu, reply_markup=kb.menu_kb)
        await State.menu.set()
    elif callback.data == more_pose_btn:
        image_name = logic.get_random_file()
        with open('images/' + image_name, 'rb') as file:
            await callback.message.answer_photo(file, caption='<i>' + image_name[:-4] + '</i>', reply_markup=kb.pose_card_kb)
    elif callback.data == desc_btn:
        name = callback.message.caption.split('\n')[0]
        caption = name + '\n\n' + DESCRIPTIONS[name]
        try:
            if len(callback.message.caption.split('\n')) > 1:
                await callback.message.edit_caption('<i>' + name + '</i>', reply_markup=kb.pose_card_kb)
            else:
                await callback.message.edit_caption('<i>' + caption + '</i>', reply_markup=kb.pose_card_kb)
        except:
            await callback.message.answer(texts.error)
    await callback.answer()
    