

import telebot
from time import sleep


bot = telebot.TeleBot('891630453:AAE7NaSUSbUTVjFImCKeZBMudgys0omiR3Y')
@bot.message_handler(commands=["start"])
def start(message):
    with open('id_list_text.txt') as data_file:
        id_list = list(map(int, data_file.read().split()))
    bot.send_message(message.chat.id, "Welcome to our iMotivateBot !!! Get Your daily motivation now!!")

    if id_list.count(message.chat.id) == 0:
        f = open('id_list_text.txt', 'a')
        f.write("\n"+str(message.chat.id))
        f.close()
        id_list.append(message.chat.id)

    print(id_list)
    return

print("Lets start")


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
        sleep(1)


    except Exception:
        print("Internet error!")
        sleep(1)