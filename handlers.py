from aiogram import types, F, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

import text
import kb
import states

user = states.User()
router = Router()
agreement = FSInputFile("agreement.docx")

# Хендлер для начальной команды /start
@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(states.UserStates.unconfirmed)
    await msg.answer(text=text.start_text,
                     reply_markup=kb.start_keyboard)

# Хендлер для начала регистрации
@router.callback_query(F.data == "key_and_api")
async def agreement(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Please read our user agreement and accept it\nЗдесь будет прикреплен документ',
                                        reply_markup=kb.agreement_keyboard)

#Хендлер для согласия с пользовательским соглашением
@router.callback_query(F.data == "agreement")
async def agreed(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(states.UserStates.unregistered)
    await callback_query.message.answer(text='You have successfully accepted the agreement!',
                                        reply_markup=kb.agreed_keyboard)

#Хендлер для начала ввода API
@router.callback_query(F.data == "api")
async def callback_query_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Please, send your Binance API', reply_markup=kb.manual_keyboard)

#Хендлер для присланного API
@router.message(states.UserStates.unregistered)
async def get_api(msg: Message, state: FSMContext):
    user.api = msg.text
    await msg.answer(text='Please, send your secret key')
    await state.set_state(states.UserStates.unregistered_with_api)

#Хендлер для присланного secret key
@router.message(states.UserStates.unregistered_with_api)
async def get_secret_key(msg: Message, state: FSMContext):
    user.secret_key = msg.text
    await msg.answer(text=f'Your API: {user.api}\nYour secret key: {user.secret_key}')
    await msg.answer(text='Здесь заглушка проверки на правильность данных. Предположим, что проверка прошла успешно.')
    await state.set_state(states.UserStates.registered)
    await msg.answer(text=text.registration_text, reply_markup=kb.menu_keyboard)

# Хендлер для списка трейдеров
@router.callback_query(F.data == "list_of_traders")
async def list_of_traders(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будет список трейдеров')
#Хендлер для пополнения баланса
@router.callback_query(F.data == "top_up")
async def top_up_balance(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будет пополнение аккаунта')
#Хендлер для инструкций
@router.callback_query(F.data == "instructions")
async def instructions(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будут инструкции')


