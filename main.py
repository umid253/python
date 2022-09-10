import telebot
from telebot import types
bot= telebot.TeleBot ('5479614388:AAFplRML2MPxj4Hs5mY7PGxe4TTq8krCibM')
storage = {}
   
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("👋 ПОКАЗАТЬ ТАБЛИЦУ ИМТ(BMI)")

    btn2 = types.KeyboardButton("НАЗАД🔙")

    btn3 = types.KeyboardButton("НАЧАТЬ✌️")
    btn4 = types.KeyboardButton("💻📞ПОДДЕРЖКА 📨✅")
    markup.add(btn1, btn2 , btn3 , btn4)

    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я ВЫЧИСЛЮ ВАШ ИМТ(BMI)".format(message.from_user), reply_markup=markup)
    init_storage(message.from_user.id)
    bot.reply_to(message, "ВЫ ХОТИТЕ ВЫЧИСЛИТЬ СВОЙ ИМТ(BMI)?\nЕСЛИ ХОТИТЕ ВВЕДИТЕ (НАЧАТЬ✌️): ")
    bot.register_next_step_handler(message, plus)

@bot.message_handler(content_types=['text'])

def func(message):

    if(message.text == "👋 ПОКАЗАТЬ ТАБЛИЦУ ИМТ(BMI)"):

        bot.send_message(message.chat.id, text= "16 И МЕНЕЕ | ВЫРАЖЕННЫЙ ДЕФИЦИТ МАССЫ ТЕЛА  \n16 - 18,5 | НЕДОСТАТОЧНАЯ МАССА ТЕЛА (ДЕФИЦИТ)  \n18,5-25 | НОРМА  \n25-30 | ИЗБЫТОЧНАЯ МАССА ТЕЛА (ПРЕДОЖИРЕНИЕ  \n30-35 | ОЖИРЕНИЕ ПЕРВОЙ СТЕПЕНИ  \n35-40 | ОЖИРЕНИЕ ВТОРОЙ СТЕПЕНИ  \n40 и более | ОЖИРЕНИЕ ТРЕТЬЕЙ СТЕПЕНИ (МОРБИДНОЕ))\n\nБЕРЕГИТЕ СЕБЯ И СЛЕДИТЕ ЗА СВОИМ ЗДОРОВЬЕМ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")

    elif(message.text == "НАЗАД🔙"):

        bot.send_message(message.chat.id, text="ЕСЛИ ХОТИТЕ НАЧАТЬ ЗАНОВО\n НАЖМИТЕ  /start 😎")

    elif(message.text == "💻📞ПОДДЕРЖКА 📨✅"):

        bot.send_message(message.chat.id, text="НАПИШИТЕ НАМ НА ПОЧТУ📧 yumid255@gmail.com ИЛИ НА ПОЧТУ📧  yumid253@gmail.com И МЫ РАССМОТРИМ ВАШУ ЗАЯВКУ📄 И ОТВЕТИМ В ТЕЧЕНИИ 48 ЧАСОВ⌚️\n ИЗВИНИТЕ🙏😘 ЗА ПРИЧИНЁННЫЕ НЕУДОБСТВА👌✅\n\n\n\nПОЖАЛУЙСТА 🙏ПИШИТЕ ✍️ТОЛЬКО ПО ДЕЛУ  , ЕСЛИ ВЫ НАШЛИ  КАКОЙ-ЛИБО БАГ,  ОШИБКУ В ПЕРЕВОДЕ  ЛИБО БОТ🤖 ПО КАКИМ-ТО ПРИЧИНАМ НЕ РАБОТАЕТ;  СРАЗУ  СООБЩАЙТЕ ОБ ЭТОМ В ПОДДЕРЖКУ!!!")

    elif(message.text == "НАЧАТЬ✌️"):

        bot.send_message(message.chat.id, text="/start")
    else:

        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")




def init_storage(user_id):
  storage[user_id] = dict(first_number=None, second_number=None)

def store_number(user_id, key, value):
  storage[user_id][key] = dict(value=value)

def get_number(user_id, key):
  return storage[user_id][key].get('value')



def plus(message):
      if message.text == "НАЧАТЬ✌️":
         bot.reply_to(message,"ВВЕДИТЕ СВОЮ МАССУ ТЕЛА⚖️: ")
         bot.register_next_step_handler(message, plus_one)
      
def plus_one(message):
        first_number = message.text

        if not first_number.isdigit():
            msg = bot.reply_to(message, 'Enter only digits!')
            bot.register_next_step_handler(message, plus_one)
            return

        store_number(message.from_user.id, "first_number", first_number)
        bot.reply_to(message, "ВВЕДИТЕ СВОЙ РОСТ📈,\n НАПРИМЕР(1.70): ")
        bot.register_next_step_handler(message, plus_two)

def plus_two(message):
       second_number = message.text

       if  second_number.isdigit():
            msg = bot.reply_to(message, 'Enter only digits!')
            bot.register_next_step_handler(message, plus_two)
            return

       store_number(message.from_user.id, "second_number", second_number)

       number_1 = get_number(message.from_user.id, "first_number")
       number_2 = get_number(message.from_user.id, "second_number")

       c = int(number_1) / float(number_2) ** 2
       bot.reply_to(message, f"ВОТ ВАШ ИМТ(BMI)✅:" + str( round(c) ) )

bot.polling(none_stop=True, interval=0)

bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True, interval=0)
    bot.infinity_polling()