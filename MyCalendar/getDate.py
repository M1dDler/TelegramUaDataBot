from telebot import types
import calendar

async def getDate(bot, message, year, month):

    #Generates days of the month by week
    cal = calendar.monthcalendar(year, month)
    
    #Names of months in Ukrainian language
    month_list = [' ', 'Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']

    #Abbreviated names of days of the week in Ukrainian language
    days = ["Пн","Вт","Ср","Чт","Пт","Сб","Нд"]
    
    #Creating a container with calendar buttons in the Telegram bot
    markup = types.InlineKeyboardMarkup(row_width=7)
    
    #Button for choosing month and year
    change_date_btn = types.InlineKeyboardButton(("< "+str(month_list[month])+" - "+str(year)+" >"), callback_data = "ChangeMonth_"+str(year)+"_"+str(month))
    markup.add(change_date_btn)
    
    #Displaying the names of the days of the week (do not perform any functionality)
    week_days = []
    for day in days:
        day_name_btn = types.InlineKeyboardButton(day, callback_data = " ")
        week_days.append(day_name_btn)    
    markup.add(*week_days)
    
    #Displaying the numbers of the days of the month, which the user must choose
    for i in range(5):
        number_days = []
        for j in range(7):
            if cal[i][j] == 0:
                day_number_btn = types.InlineKeyboardButton(" ", callback_data = " ")
            else:
                day_number_btn = types.InlineKeyboardButton(cal[i][j], callback_data = "ShowStatistic_"+str(year)+"_"+str(month)+"_"+str(cal[i][j]))
            number_days.append(day_number_btn)
        markup.add(*number_days)
        
    #Displaying the calendar in the Telegram bot
    return await bot.send_message(message, "Оберіть дату статистичних даних 📆", reply_markup=markup)