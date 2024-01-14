from aiogram import Bot, Dispatcher, types, executor
import logging
from Base import Database
from list_words import words
import bot_token as tk

BOT_TOKEN = tk.BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

db = Database('explanatory')

@dp.message_handler()
async def echo(msg: types.Message):
    user_text = msg.text
    if user_text.upper() in words:
        await msg.answer(*db.ret_description(user_text.upper())[0])
    else:
        await msg.answer('Данные не корректны!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)