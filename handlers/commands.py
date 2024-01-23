from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from aiotables import append_user
from datetime import datetime

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.start_message)
    await message.answer(texts.menu, reply_markup=kb.menu_kb)
    await State.menu.set()
    await append_user(datetime.now().strftime('%d/%m/%Y, %H:%M:%S'), message.from_id, message.from_user.username)


@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)
