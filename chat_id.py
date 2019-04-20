

import telebot
from time import sleep


bot = telebot.TeleBot('891630453:AAE7NaSUSbUTVjFImCKeZBMudgys0omiR3Y')
@bot.message_handler(commands=["start"])
def start(message):
    with open('id_list_text.txt') as f:
        id_list = list(map(int, f.read().split()))
        bot.send_message(message.chat.id, "Welcome to our iMotivateBot !!! Get Your daily motivation now!! \n"
                                          "/delete - write if You want to unsubscribe")
        print("chat.id=", message.chat.id)

    if id_list.count(message.chat.id) == 0:
        f = open('id_list_text.txt', 'a')
        f.write("\n"+str(message.chat.id))
        f.close()
        id_list.append(message.chat.id)

    print(id_list)
    return


@bot.message_handler(commands=["test"])
def test(message):

    bot.send_message(message.chat.id, "Some test")



@bot.message_handler(commands=["delete"])
def delete(message):
    bot.send_message(message.chat.id, "UNSUBSCRIBED")
    with open('id_list_text.txt', 'r+') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if (str(message.chat.id)) not in line:
                f.write(line)
        f.truncate()
        f.close()
    print("chat.id=", message.chat.id, 'deleted')

@bot.message_handler(commands=["help"])
def help(message):

    bot.send_message(message.chat.id, "You can choose next commands: \n "
                                      "/start - start motivate bot\n"
                                      "/test - test test\n"
                                      "/delete - Unsubscribe\n"
                                      "/other  - other other")



print("Lets start")



if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
        sleep(1)


    except Exception:
        print("Internet error!")
        sleep(1)
        bot.polling(none_stop=True)
    finally:
        bot.polling(none_stop=True)
        sleep(1)
