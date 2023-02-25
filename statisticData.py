from requestsData import *

async def statistic(bot, message, year, month, day):
    
    if len(str(month)) == 1:
        month = "0"+str(month)
    if len(str(day)) == 1:
        day = "0"+str(day)
    date = str(year)+"-"+str(month)+"-"+str(day)
    
    data = getWarStatistic()
    
    text = "<b>Станом на "+str(date)+" загальні втрати ворога складають:\n\n</b>"
    
    for x in data:
        
        text += ("📌 " + x.json()['title'] + " - ")
        
        filter_val = [i for i in x.json()['data'] if i['at'] == date]
        
        if len(filter_val) == 0:
            text += "<b>невідомо</b>\n"
            continue
        text += "<b>" + str(filter_val[0]['val']) + "</b>\n"
                
        
    return await bot.send_message(message.message.chat.id, text, parse_mode="HTML")