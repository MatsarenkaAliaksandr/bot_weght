import telebot
from telebot import types

token = '5592597754:AAEpvGL_YLPDyPftW6042r1Kz-wtEfIiGU8'
bot = telebot.TeleBot(token)

value = ""
old_value = ""
value_1 = ''
value_2 = ''


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    calc_btn = types.InlineKeyboardButton(text="Показать результат", callback_data='=')
    n1_btn = types.InlineKeyboardButton(text="1", callback_data='1')
    n2_btn = types.InlineKeyboardButton(text="2", callback_data='2')
    n3_btn = types.InlineKeyboardButton(text="3", callback_data='3')
    n4_btn = types.InlineKeyboardButton(text="4", callback_data='4')
    n5_btn = types.InlineKeyboardButton(text="5", callback_data='5')
    n6_btn = types.InlineKeyboardButton(text="6", callback_data='6')
    n7_btn = types.InlineKeyboardButton(text="7", callback_data='7')
    n8_btn = types.InlineKeyboardButton(text="8", callback_data='8')
    n9_btn = types.InlineKeyboardButton(text="9", callback_data='9')
    n0_btn = types.InlineKeyboardButton(text="0", callback_data='0')
    T_btn = types.InlineKeyboardButton(text=",", callback_data='.')
    C_btn = types.InlineKeyboardButton(text="C", callback_data='C')
    w_btn = types.InlineKeyboardButton(text="Вес", callback_data='value_1')
    h_btn = types.InlineKeyboardButton(text="Рост", callback_data='value_2')
    keyboard.add(n1_btn, n2_btn, n3_btn)
    keyboard.add(n4_btn, n5_btn, n6_btn)
    keyboard.add(n7_btn, n8_btn, n9_btn)
    keyboard.add(n0_btn, C_btn, T_btn)
    keyboard.add(h_btn, w_btn)
    keyboard.add(calc_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, "Добрый день! Введите, вес(кг)/рост(м)")
    global value
    if value == "":
        bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    global value, value_1, value_2, old_value
    data = call.data
    if data == "C":
        value = ""
    elif data == "value_1":
        value_1 = value
        value = ''
    elif data == "value_2":
        value_2 = value
    elif data == "=":
        value = str(float(value_1) / float(value_2) ** 2)
        if float(value) <= 16:
            bot.send_message(call.message.chat.id, "У вас выраженный дефицит массы тела!")
        if float(value) > 16 and float(value) <= 18.5:
            bot.send_message(call.message.chat.id, "У вас недостаточная (дефицит) массы тела!")
        if float(value) > 18.5 and float(value) <= 24.99:
            bot.send_message(call.message.chat.id, "У вас норма!")
        if float(value) >= 25 and float(value) <= 30:
            bot.send_message(call.message.chat.id, "У вас избыточная масса тела(предожирение)!")
        if float(value) > 30 and float(value) <= 35:
            bot.send_message(call.message.chat.id, "У вас ожирение!")
        if float(value) > 35 and float(value) <= 40:
            bot.send_message(call.message.chat.id, "У вас ожирение резкое!")
        if float(value) > 40:
            bot.send_message(call.message.chat.id, "У вас очень резкое ожирение!")
        img = open('kalk.png', 'rb')
        bot.send_photo(chat_id=call.message.chat.id,photo=img)
        img.close()
    else:
        value += data
    if value != old_value:
        if value == "":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="0", reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=value, reply_markup=keyboard)
    old_value = value


if __name__ == "__main__":
    bot.polling(none_stop=True)
