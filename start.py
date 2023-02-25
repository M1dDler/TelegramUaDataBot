import asyncio
import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from requestsData import *
from getDate import *
from telebot import types
from statisticData import *
from flaskWeb import keep_alive
import datetime
import pytz

load_dotenv()
token = os.getenv("TOKEN")
bot = AsyncTeleBot(token)

@bot.message_handler(func=lambda message: True)
async def handle_all_messages(message):
    if message.content_type == 'text':
        if not message.entities == None:
            if message.entities[0].type == 'bot_command':
                
                if message.text == '/start':
                    
                    await bot.set_my_commands([
                        types.BotCommand("statistic", "Загальні втрати ворога")
                    ])
                
                    return await bot.send_message(message.chat.id, "Слава Україні 🇺🇦")
                    
                now_utc = datetime.datetime.now(pytz.UTC)
    
                gmt2 = pytz.timezone('Etc/GMT-2')
                now_gmt2 = now_utc.astimezone(gmt2)
                year = now_gmt2.strftime('%Y')
                month = now_gmt2.strftime('%m')
                
                if str(month)[0] == "0":
                    month = str(month)[1]
                    
                if message.chat.type == "group":    
                    if message.text == '/statistic@n1tron_bot':
                        return await getDate(bot, message.chat.id, year, month)
                elif message.chat.type == "private":
                    if message.text == '/statistic':
                        return await getDate(bot, message.chat.id, 2023, 2)
            
            return
        return

@bot.callback_query_handler(func=lambda query: True)
async def balance_calldata(query):
    data = query.data.split("_")
    
    if data[0] == "Date": 
        markup = types.InlineKeyboardMarkup(row_width=3)
        
        continue_btn = types.InlineKeyboardButton("Залишити поточний місяць", callback_data="Next_"+str(data[1])+"_"+str(data[2]))
        dec_btn = types.InlineKeyboardButton("Грудень", callback_data="Next_"+str(data[1])+"_12")
        jan_btn = types.InlineKeyboardButton("Січень", callback_data="Next_"+str(data[1])+"_1")
        feb_btn = types.InlineKeyboardButton("Лютий", callback_data="Next_"+str(data[1])+"_2")
        mar_btn = types.InlineKeyboardButton("Березень", callback_data="Next_"+str(data[1])+"_3")
        apr_btn = types.InlineKeyboardButton("Квітень", callback_data="Next_"+str(data[1])+"_4")
        may_btn = types.InlineKeyboardButton("Травень", callback_data="Next_"+str(data[1])+"_5")
        jun_btn = types.InlineKeyboardButton("Червень", callback_data="Next_"+str(data[1])+"_6")
        jul_btn = types.InlineKeyboardButton("Липень", callback_data="Next_"+str(data[1])+"_7")
        aug_btn = types.InlineKeyboardButton("Серпень", callback_data="Next_"+str(data[1])+"_8")
        sep_btn = types.InlineKeyboardButton("Вересень", callback_data="Next_"+str(data[1])+"_9")
        oct_btn = types.InlineKeyboardButton("Жовтень", callback_data="Next_"+str(data[1])+"_10")
        nov_btn = types.InlineKeyboardButton("Листопад", callback_data="Next_"+str(data[1])+"_11")
        
        markup.add(continue_btn)
        markup.add( dec_btn, jan_btn, feb_btn, 
                   mar_btn, apr_btn, may_btn, 
                   jun_btn, jul_btn, aug_btn, 
                   sep_btn, oct_btn, nov_btn)
        
        await bot.delete_message(query.message.chat.id, query.message.id)
        await bot.send_message(query.message.chat.id, "Вкажіть бажаний місяць року: ", reply_markup=markup)
        
    if data[0] == "Next":
        
        markup = types.InlineKeyboardMarkup(row_width=3)
        
        continue_btn = types.InlineKeyboardButton("Залишити поточний рік", callback_data="Enddate_"+str(data[1])+"_"+str(data[2]))
        twenty_two_btn = types.InlineKeyboardButton("2022", callback_data="Enddate_2022_"+str(data[2]))
        twenty_three_btn = types.InlineKeyboardButton("2023", callback_data="Enddate_2023_"+str(data[2]))
        markup.add(continue_btn)
        markup.add(twenty_two_btn, twenty_three_btn)
    
        await bot.delete_message(query.message.chat.id, query.message.id)
        await bot.send_message(query.message.chat.id, "Оберіть бажаний рік", reply_markup=markup)
        
    if data[0] == "Enddate":
        await getDate(bot, query.message.chat.id, int(data[1]), int(data[2]))
        
    if data[0] == "Choose":
        await statistic(bot, query, data[1], data[2], data[3])
        
keep_alive()        
asyncio.run(bot.infinity_polling())