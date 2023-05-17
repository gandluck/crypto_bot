from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

start_b1 = InlineKeyboardButton(text="Enter Binance API and secret key", callback_data="key_and_api")
start_b2 = InlineKeyboardButton(text="How to get API", url='https://www.binance.com/en-BH/support/faq/how-to-create-api-360002502072')
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[start_b1],
                     [start_b2]]
)

key_and_api_b1 = InlineKeyboardButton(text="Enter api", callback_data="api")
key_and_api_b2 = InlineKeyboardButton(text="Enter secret key", callback_data="key")
key_and_api_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[key_and_api_b1],
                     [key_and_api_b2]]
)

