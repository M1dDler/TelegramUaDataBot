from telebot import types

async def changeMonth(bot, query, year, month):  
    
    #Names of months in Ukrainian language
    month_list = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
    
    #Creating a container with month buttons       
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    #Accept current month    
    continue_btn = types.InlineKeyboardButton("Залишити поточний місяць", callback_data="ChangeYear_"+str(year)+"_"+str(month))
    markup.add(continue_btn)
    
    #Display month names for user selection    
    list_buttons = []
    for month_name in month_list:
        month_btn = types.InlineKeyboardButton(month_name, callback_data="ChangeYear_"+str(year)+"_"+str(month_list.index(month_name)+1))
        list_buttons.append(month_btn)
    markup.add(*list_buttons)
    
    #Deleting a calendar with an old date
    await bot.delete_message(query.message.chat.id, query.message.id)
    
    #Sending a Telegram bot message about the possibility of the user choosing a month
    await bot.send_message(query.message.chat.id, "Вкажіть бажаний місяць року: ", reply_markup=markup)