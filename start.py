import asyncio
import os
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
from API.app import keep_alive
from TelegramBot.Handlers.message_handler import handle_message
from TelegramBot.Handlers.callback_handler import handle_callback

#Loading data from an .env file
load_dotenv()

#Telegram bot connection settings
token = os.getenv("TOKEN")
bot = AsyncTeleBot(token)

#Registration of message handlers
bot.register_message_handler(lambda message: handle_message(message, bot))
bot.register_callback_query_handler(lambda query: handle_callback(query, bot), func=lambda query: True)

#Running flask and telegram bot
keep_alive()        
asyncio.run(bot.infinity_polling())