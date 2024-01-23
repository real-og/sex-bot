from loader import dp, ADMIN_ID, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from buttons import *
import logic


@dp.callback_query_handler(state=State.sending_feedback)
async def pose_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == back_to_menu_btn:
        await callback.message.answer(texts.menu, reply_markup=kb.menu_kb)
        await State.menu.set() 
    await callback.answer()


@dp.message_handler(state=State.sending_feedback, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    await bot.send_message(ADMIN_ID, f'{message.from_user.id} - {message.from_user.username}')
    await message.send_copy(ADMIN_ID)
    await message.answer(texts.feed_back_accepted)
    await message.answer(texts.menu, reply_markup=kb.menu_kb)
    await State.menu.set()
