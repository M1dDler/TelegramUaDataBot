from telebot import types

async def changeYear(bot, query, year, month):
    
    #Creating a container with year buttons
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    #Accept current year    
    continue_btn = types.InlineKeyboardButton("Залишити поточний рік", callback_data="EndChangeDate_"+str(year)+"_"+str(month))
    markup.add(continue_btn)
    
    #Displaying buttons with years for user selection
    twenty_two_btn = types.InlineKeyboardButton("2022", callback_data="EndChangeDate_2022_"+str(month))
    twenty_three_btn = types.InlineKeyboardButton("2023", callback_data="EndChangeDate_2023_"+str(month))
    markup.add(twenty_two_btn, twenty_three_btn)
    
    #Removing the month selection form
    await bot.delete_message(query.message.chat.id, query.message.id)
    
    #Sending a Telegram bot message about the possibility of choosing a year by the user
    await bot.send_message(query.message.chat.id, "Оберіть бажаний рік", reply_markup=markup)