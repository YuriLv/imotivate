
from time import sleep
import requests
import random
import datetime
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


with open('id_list_text.txt') as inp:
    id_list = list(map(int, inp.read().split()))


def get_quote():
    with open('motivation.txt', encoding='UTF8') as fname:
        line = fname.read().splitlines()
        print(random.choice(line))
        return random.choice(line)



def send_api_request(quote_text):
    with open('id_list_text.txt') as inp:
        id_list = list(map(int, inp.read().split()))
    for i in range(len(id_list)):

        url ="https://api.telegram.org/bot891630453:AAE7NaSUSbUTVjFImCKeZBMudgys0omiR3Y/sendMessage?chat_id=%d&text=%s" % (id_list[i],quote_text)
        r = requests.get(url)
        if (r.status_code != 200):
            print ("Send failed, status code: %s, error: %s" % (r.status_code, r.content))
            return False
    print(id_list)
    return True


time_start = datetime.time(0,00,00)
time_end = datetime.time(23,50,00)
time_current = datetime.datetime.now().time()

def main():
    while True:
        # os.system('python chat_id.py')

        if time_start < time_current < time_end:

            quote = get_quote()
            send_api_request(quote)
            sleep(20)
            print()
        else:
            print('waiting. Working time 09-20, Now is ', time_current)
            sleep(300)

if __name__ == '__main__':

    main()




