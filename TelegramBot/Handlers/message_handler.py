from telebot import types
import datetime
import pytz
from MyCalendar.getDate import getDate

async def handle_message(message, bot):
    
    if message.content_type == 'text':
        if not message.entities == None:
            
            #commands handlers
            if message.entities[0].type == 'bot_command':
                
                if message.text == '/start':
                    
                    #Displaying a list of commands in the Telegram command menu
                    await bot.set_my_commands([
                        types.BotCommand("statistic", "Загальні втрати ворога")
                    ])

                    #Sending a message
                    return await bot.send_message(message.chat.id, "Слава Україні 🇺🇦")
                    
                #Setting the current date    
                now_utc = datetime.datetime.now(pytz.UTC)
                gmt2 = pytz.timezone('Etc/GMT-3')
                now_gmt2 = now_utc.astimezone(gmt2)
                year = int(now_gmt2.strftime('%Y'))
                month = int(now_gmt2.strftime('%m'))
                
                    
                #Calling the calendar display function, the commands differ depending on the type of chat    
                if message.chat.type == "supergroup" or message.chat.type == "group":    
                    if message.text == '/statistic@n1tron_bot':
                        return await getDate(bot, message.chat.id, year, month)
                elif message.chat.type == "private":
                    if message.text == '/statistic':
                        return await getDate(bot, message.chat.id, year, month)
            
            return
        return