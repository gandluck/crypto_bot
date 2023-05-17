from aiogram import types, F, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import text
import kb
import states

user = states.User()
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text=text.start_msg, reply_markup=kb.start_keyboard)

@router.callback_query(F.data == "key_and_api")
async def callback_query_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(states.UserStates.unregistered)
    await callback_query.message.answer(text='Please, send your Binance API')

@router.message(states.UserStates.unregistered)
async def get_api(msg: Message, state: FSMContext):
    user.api = msg.text
    await msg.answer(text='Please, send your secret key')
    await state.set_state(states.UserStates.unregistered_with_api)

@router.message(states.UserStates.unregistered_with_api)
async def get_secret_key(msg: Message, state: FSMContext):
    user.secret_key = msg.text
    await msg.answer(text=f'Your API:{user.api}\nYour secret key: {user.secret_key}')
    await msg.answer(text='Здесь заглушка проверки на правильность данных')

#     @router.callback_query(F.data == "api")
#     async def callback_query_api_handler(callback_query: types.CallbackQuery):
#         await callback_query.message.answer(text='Send API')
#
#         @router.message()
#         async def api_handler(msg: Message):
#             user_api = msg.text
#             await msg.answer(text=f'Your Binance API: {user_api}')
#             await msg.answer(text='Send secret key')
#
#             @router.message()
#             async def key_handler(msg: Message):
#                 user_key = msg.text
#                 await msg.answer(text=f'Your secret key: {user_key}')
#                 await msg.answer(text='Please, wait')
#
#     @router.callback_query(F.data == "key")
#     async def callback_query_key_handler(callback_query: types.CallbackQuery):
#         await callback_query.message.answer(text='Please, send secret key')
#
#         @router.message()
#         async def key_handler(msg: Message):
#             user_key = msg.text
#             await msg.answer(text=f'Your secret key: {user_key}')
#             await msg.answer(text='Please, send API')
#
#             @router.message()
#             async def api_handler(msg: Message):
#                 user_api = msg.text
#                 await msg.answer(text=f'You Binance API: {user_api}')
#                 await msg.answer(text='Please,wait')


