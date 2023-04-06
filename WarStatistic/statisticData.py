from Requests.uaDataRequest import getWarStatistic
from MyCalendar.getDate import getDate

async def statistic(bot, message, year, month, day):
    
    #Create temporaryMessage to user information
    temporaryMessage = await bot.send_message(message.message.chat.id, "🔎 Пошук статистичних даних...")
    
    #Date formatting
    if len(str(month)) == 1:
        month = "0"+str(month)
    if len(str(day)) == 1:
        day = "0"+str(day)
    date = str(year)+"-"+str(month)+"-"+str(day)
    
    #Loading statistics
    data = getWarStatistic()
    
    #Text design of statistical data
    text = "<b>Станом на "+str(date)+" загальні втрати ворога складають:\n\n</b>"
    for x in data:
        text += ("📌 " + x.json()['title'] + " - ")
        filter_val = [i for i in x.json()['data'] if i['at'] == date]
        if len(filter_val) == 0:
            text += "<b>невідомо</b>\n"
            continue
        text += "<b>" + str(filter_val[0]['val']) + "</b>\n"
                
    #Deleting temporaryMessage
    await bot.delete_message(message.message.chat.id, temporaryMessage.id)
    
    #Deleting calendar
    await bot.delete_message(message.message.chat.id, message.message.id)
    
    #Sending statistical data by Telegram bot
    await bot.send_message(message.message.chat.id, text, parse_mode="HTML")

    #Display calendar below statistic information
    return await getDate(bot, message.message.chat.id, int(year), int(month))    