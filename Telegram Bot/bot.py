import os
import asyncio
from telebot.async_telebot import AsyncTeleBot

BOT_TOKEN = "6014690146:AAGca62lt2whWchKgx8DfWfrIUcYivCqyt8"

bot = AsyncTeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
async def send_welcome(message):
    await bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
async def echo_all(message):
    await bot.reply_to(message, message.text)

asyncio.run(bot.infinity_polling())