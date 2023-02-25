from telebot import types
import calendar

month_list = [' ', 'Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']

async def getDate(bot, message, year, month):

    cal = calendar.monthcalendar(year, month)
     
    markup = types.InlineKeyboardMarkup(row_width=7)
    first_btn = types.InlineKeyboardButton(("< "+str(month_list[month])+" - "+str(year)+" >"), callback_data = "Date_"+str(year)+"_"+str(month))
    
    pn_btn = types.InlineKeyboardButton("Пн", callback_data = " ")
    vt_btn = types.InlineKeyboardButton("Вт", callback_data = " ")
    sr_btn = types.InlineKeyboardButton("Ср", callback_data = " ")
    cht_btn = types.InlineKeyboardButton("Чт", callback_data = " ")
    pt_btn = types.InlineKeyboardButton("Пт", callback_data=" ")
    sb_btn = types.InlineKeyboardButton("Сб", callback_data = " ")
    nd_btn = types.InlineKeyboardButton("Нд", callback_data = " ")
    
    if cal[0][0] == 0:
        one_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        one_btn = types.InlineKeyboardButton(cal[0][0], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[0][0]))
    if cal[0][1] == 0:
        two_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        two_btn = types.InlineKeyboardButton(cal[0][1], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[0][1]))
    if cal[0][2] == 0:
        three_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        three_btn = types.InlineKeyboardButton(cal[0][2], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[0][2]))
    if cal[0][3] == 0:
        four_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        four_btn = types.InlineKeyboardButton(cal[0][3], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[0][3]))
    if cal[0][4] == 0:
        five_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        five_btn = types.InlineKeyboardButton(cal[0][4], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[0][4]))
    if cal[0][5] == 0:
        six_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        six_btn = types.InlineKeyboardButton(cal[0][5], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[0][5]))
    if cal[0][6] == 0:
        seven_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        seven_btn = types.InlineKeyboardButton(cal[0][6], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[0][6]))
    eight_btn = types.InlineKeyboardButton(cal[1][0], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[1][0]))
    nine_btn = types.InlineKeyboardButton(cal[1][1], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[1][1]))
    ten_btn = types.InlineKeyboardButton(cal[1][2], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[1][2]))
    eleven_btn = types.InlineKeyboardButton(cal[1][3], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[1][3]))
    twelve_btn = types.InlineKeyboardButton(cal[1][4], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[1][4]))
    thirteen_btn = types.InlineKeyboardButton(cal[1][5], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[1][5]))
    fourteen_btn = types.InlineKeyboardButton(cal[1][6], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[1][6]))
    fifteen_btn = types.InlineKeyboardButton(cal[2][0], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[2][0]))
    sixteen_btn = types.InlineKeyboardButton(cal[2][1], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[2][1]))
    seventeen_btn = types.InlineKeyboardButton(cal[2][2], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[2][2]))
    eighteen_btn = types.InlineKeyboardButton(cal[2][3], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[2][3]))
    nineteen_btn = types.InlineKeyboardButton(cal[2][4], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[2][4]))
    twenty_btn = types.InlineKeyboardButton(cal[2][5], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[2][5]))
    twenty_one_btn = types.InlineKeyboardButton(cal[2][6], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[2][6]))
    twenty_two_btn = types.InlineKeyboardButton(cal[3][0], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[3][0]))
    twenty_three_btn = types.InlineKeyboardButton(cal[3][1], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[3][1]))
    twenty_four_btn = types.InlineKeyboardButton(cal[3][2], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[3][2]))
    twenty_five_btn = types.InlineKeyboardButton(cal[3][3], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[3][3]))
    twenty_six_btn = types.InlineKeyboardButton(cal[3][4], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[3][4]))
    twenty_seven_btn = types.InlineKeyboardButton(cal[3][5], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[3][5]))
    twenty_eight_btn = types.InlineKeyboardButton(cal[3][6], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[3][6]))
    if cal[4][0] == 0:
        twenty_nine_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        twenty_nine_btn = types.InlineKeyboardButton(cal[4][0], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[4][0]))
    if cal[4][1] == 0:
        thirty_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        thirty_btn = types.InlineKeyboardButton(cal[4][1], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[4][1]))
    if cal[4][2] == 0:
        thirty_one_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        thirty_one_btn = types.InlineKeyboardButton(cal[4][2], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[4][2]))
    if cal[4][3] == 0:
        thirty_two_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else: 
        thirty_two_btn = types.InlineKeyboardButton(cal[4][3], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[4][3]))
    if cal[4][4] == 0:
        thirty_three_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        thirty_three_btn = types.InlineKeyboardButton(cal[4][4], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[4][4]))
    if cal[4][5] == 0:
        thirty_four_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        thirty_four_btn = types.InlineKeyboardButton(cal[4][5], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[4][5]))
    if cal[4][6] == 0:
        thirty_five_btn = types.InlineKeyboardButton(" ", callback_data = " ")
    else:
        thirty_five_btn = types.InlineKeyboardButton(cal[4][6], callback_data = "Choose_"+str(year)+"_"+str(month)+"_"+str(cal[4][6]))
        
    markup.add(first_btn)
    markup.add(pn_btn, vt_btn, sr_btn, cht_btn, pt_btn, sb_btn, nd_btn,
               one_btn, two_btn, three_btn, four_btn, five_btn, six_btn, seven_btn,
               eight_btn, nine_btn, ten_btn, eleven_btn, twelve_btn, thirteen_btn, fourteen_btn,
               fifteen_btn, sixteen_btn, seventeen_btn, eighteen_btn, nineteen_btn, twenty_btn, twenty_one_btn,
               twenty_two_btn, twenty_three_btn, twenty_four_btn, twenty_five_btn, twenty_six_btn, twenty_seven_btn, twenty_eight_btn,
               twenty_nine_btn, thirty_btn, thirty_one_btn, thirty_two_btn, thirty_three_btn, thirty_four_btn, thirty_five_btn)
     
    return await bot.send_message(message, "Оберіть дату статистичних даних 📆", reply_markup=markup)