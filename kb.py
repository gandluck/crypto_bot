from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

start_b1 = InlineKeyboardButton(text="Enter Binance API and secret key", callback_data="key_and_api")
start_b2 = InlineKeyboardButton(text="How to get API", url='https://www.binance.com/en-BH/support/faq/how-to-create-api-360002502072')
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[start_b1],
                     [start_b2]]
)

agreement_b1 =InlineKeyboardButton(text="Yes, I agree", callback_data="agreement")
agreement_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[agreement_b1]]
)

agreed_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[start_b1]]
)


