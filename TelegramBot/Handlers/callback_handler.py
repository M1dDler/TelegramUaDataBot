from TelegramBot.Callbacks.change_month import changeMonth
from TelegramBot.Callbacks.change_year import changeYear
from MyCalendar.getDate import getDate
from WarStatistic.statisticData import statistic

async def handle_callback(query, bot):
    data = query.data.split("_")
    
    #Call the function of changing the month
    if data[0] == "ChangeMonth": 
        year = data[1]
        month = data[2]
        return await changeMonth(bot, query, year, month)
        
    #Call the year change function
    if data[0] == "ChangeYear":
        year = data[1]
        month = data[2]
        return await changeYear(bot, query, year, month)
    
    #Completing the date change, displaying the new Telegram bot calendar
    if data[0] == "EndChangeDate":
        await bot.delete_message(query.message.chat.id, query.message.id)
        return await getDate(bot, query.message.chat.id, int(data[1]), int(data[2]))
    
    #Calling the statistics display function
    if data[0] == "ShowStatistic":
        return await statistic(bot, query, data[1], data[2], data[3])