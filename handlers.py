from aiogram import types, F, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import text
import kb

dp = Dispatcher()
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text=text.start_msg, reply_markup=kb.start_keyboard)

@router.callback_query(F.data == "key_and_api")
async def callback_query_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='тут должна быть регистрация')