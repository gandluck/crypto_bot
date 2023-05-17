from aiogram.types import CallbackQuery
from aiogram import types, F, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.enums.parse_mode import ParseMode

import text
import kb
import states


user = states.User()
router = Router()
agreement = FSInputFile("agreement.docx")

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(states.UserStates.unconfirmed)
    await msg.answer(text=text.start_text, reply_markup=kb.start_keyboard)


@router.callback_query(states.UserStates.unconfirmed, F.data == "key_and_api")
async def agreement(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Please read our user agreement and accept it', reply_markup=kb.agreement_keyboard)

@router.callback_query(F.data == "agreement")
async def agreed(msg: Message, state: FSMContext):
    await state.set_state(states.UserStates.unregistered)
    await msg.answer(text='You have successfully accepted the agreement!', reply_markup=kb.agreed_keyboard)


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
    await msg.answer(text=f'Your API: {user.api}\nYour secret key: {user.secret_key}')
    await msg.answer(text='Здесь заглушка проверки на правильность данных. Предположим, что проверка прошла успешно.')
