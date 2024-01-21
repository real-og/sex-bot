from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from buttons import *


@dp.callback_query_handler(state=State.menu)
async def menu_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == get_random_pose_btn:
        pass
    elif callback.data == info_btn:
        await callback.message.answer(texts.info)
        await callback.message.answer(texts.menu, reply_markup=kb.menu_kb)    
        
    await callback.answer()
    