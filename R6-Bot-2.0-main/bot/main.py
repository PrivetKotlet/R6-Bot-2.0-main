import telebot
import pyfiglet
import __pycache__
from colorama import *
from modules.Operatives import *
from modules.db_parss import *


'''/ __ \/ ___/ ___// /_____ ______/ /_______     / /_  ____  / /_
  / /_/ / __ \\__ \/ __/ __ `/ ___/ //_/ ___/    / __ \/ __ \/ __/
 / _, _/ /_/ /__/ / /_/ /_/ (__  ) ,< (__  )    / /_/ / /_/ / /_
/_/ |_|\____/____/\__/\__,_/____/_/|_/____/____/_.___/\____/\__/
                                         /_____/'''


token = '5165986680:AAEWLjg-Ahtmzdh0Gc-9rTBw6OUIgIxCBVw'


bot = telebot.TeleBot(token)
#Получение Токена для подключения

#Приветсвенное сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет. Я бот Степан я буду давать тебе задания на игру R6')


#Функия help навигация для пользователя
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,'''
/zadanie - Получить Задание 
/offers - Оставить отзыв''')



#Функция отвечающая за отзывы от пользовотеля 
@bot.message_handler(commands=['offers'])
def Offers_message(message):
    bot.send_message(message.chat.id, 'Напишите ваш отзыв или предложение')
    bot.register_next_step_handler(message, record_references_or_suggestions)


def record_references_or_suggestions(message):
    references = message.text
    f = open('Offers.txt' , 'w')
    f.write(references)
    f.close()
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв")


#Проверка на задание со звёздочкой
@bot.message_handler(commands=['zadanie'])
def Task_message(message):
    bot.send_message(message.chat.id, 'Хотите Задание со Звёздочкой ?')
    bot.register_next_step_handler(message, squad_selection)

#Функция которая выбирает отряд оперативников
def squad_selection(message):
    global msg
    msg = message.text.lower()
    global star_choice
    if msg == "да" or "da" or "lf" or "yes" :
        star_choice = 1
        bot.send_message(message.chat.id, 'Выбирите Защита или Атака ?')
        bot.register_next_step_handler(message, Operatives_choice)
    elif msg =="нет" or "net" or "ytn" or "no":
        star_choice = 2
        bot.send_message(message.chat.id, 'Выбирите Защита или Атака ?')
        bot.register_next_step_handler(message, Operatives_choice)
    else:
        bot.send_message(message.chat.id,"Я вас не понял")


#Функция которая выбирает оперативника
def Operatives_choice(message):
    Type_Operatives_choice = message.text.lower()
    if Type_Operatives_choice == "защита":
        bot.send_message(message.chat.id, 'Выбирите оперативника')
        bot.send_message(message.chat.id, protection)
        bot.register_next_step_handler(message, Operatives_choice_Protection)
    elif Type_Operatives_choice == "атака":
        bot.send_message(message.chat.id, 'Выбирите оперативника')
        bot.send_message(message.chat.id, attak)
        bot.register_next_step_handler(message, Operatives_choice_Attack)


#Функция которая скидывает задание оперативников защиты
def Operatives_choice_Protection(message):
    operative = message.text.lower()
    if operative == 'smoke':
        bot.send_message(message.chat.id, Operatives.Protection.Smoke(star_choice))
    elif operative == 'mute':
        bot.send_message(message.chat.id, Operatives.Protection.MUTE(star_choice))
    elif operative == 'castle':
        bot.send_message(message.chat.id, Operatives.Protection.CASTLE(star_choice))
    elif operative == 'pulse':
        bot.send_message(message.chat.id, Operatives.Protection.PULSE(star_choice))
    elif operative == 'jager':
        bot.send_message(message.chat.id, Operatives.Protection.JAGER(star_choice))
    elif operative == 'bandit':
        bot.send_message(message.chat.id, Operatives.Protection.BANDIT(star_choice))
    elif operative == 'doc':
        bot.send_message(message.chat.id, Operatives.Protection.DOC(star_choice))
    elif operative == 'rook':
        bot.send_message(message.chat.id, Operatives.Protection.ROOK(star_choice))
    elif operative == 'tachanka':
        bot.send_message(message.chat.id, Operatives.Protection.TACHANKA(star_choice))
    elif operative == 'kapkan':
        bot.send_message(message.chat.id, Operatives.Protection.KAPKAN(star_choice))
    elif operative == 'frost':
        bot.send_message(message.chat.id, Operatives.Protection.FROST(star_choice))
    elif operative == 'caveira':
        bot.send_message(message.chat.id, Operatives.Protection.CAVEIRA(star_choice))
    elif operative == 'echo':
        bot.send_message(message.chat.id, Operatives.Protection.ECHO(star_choice))
    elif operative == 'mira':
        bot.send_message(message.chat.id, Operatives.Protection.MIRA(star_choice))
    elif operative == 'lesion':
        bot.send_message(message.chat.id, Operatives.Protection.LESION(star_choice))
    elif operative == 'ela':
        bot.send_message(message.chat.id, Operatives.Protection.ELA(star_choice))
    elif operative == 'vigil':
        bot.send_message(message.chat.id, Operatives.Protection.VIGIL(star_choice))
    elif operative == 'maesteo':
        bot.send_message(message.chat.id, Operatives.Protection.MAESTRO(star_choice))
    elif operative == 'clash':
        bot.send_message(message.chat.id, Operatives.Protection.CLASH(star_choice))
    elif operative == 'kaid':
        bot.send_message(message.chat.id, Operatives.Protection.KAID(star_choice))
    elif operative == 'mozzie':
        bot.send_message(message.chat.id, Operatives.Protection.MOZZIE(star_choice))
    elif operative == 'warden':
        bot.send_message(message.chat.id, Operatives.Protection.WARDEN(star_choice))
    elif operative == 'goyo':
        bot.send_message(message.chat.id, Operatives.Protection.GOYO(star_choice))
    elif operative == 'wamai':
        bot.send_message(message.chat.id, Operatives.Protection.WAMAI(star_choice))
    elif operative == 'oryx':
        bot.send_message(message.chat.id, Operatives.Protection.ORYX(star_choice))
    elif operative == 'melusi':
        bot.send_message(message.chat.id, Operatives.Protection.MELUSI(star_choice))
    elif operative == 'aruni':
        bot.send_message(message.chat.id, Operatives.Protection.ARUNI(star_choice))
    elif operative == 'thunderbird':
        bot.send_message(message.chat.id, Operatives.Protection.THUNDERBIRD(star_choice))
    elif operative == 'thorn':
        bot.send_message(message.chat.id, Operatives.Protection.THORN(star_choice))
    elif operative == 'azami':
        bot.send_message(message.chat.id, Operatives.Protection.AZAMI(star_choice))
    else:
        bot.send_message(message.chat.id, "Такого оперативника нету в этом спецотряде напишите /zadanie чтобы получить задания")



#Функция которая скидывает задание оперативников атаки
def Operatives_choice_Attack(message):
    operative = message.text.upper()
    if operative == 'SLEDGE':
        bot.send_message(message.chat.id, Operatives.Attack.SLEDGE(star_choice))
    elif operative == 'ASH':
        bot.send_message(message.chat.id, Operatives.Attack.ASH(star_choice))
    elif operative == 'THATCHER':
        bot.send_message(message.chat.id, Operatives.Attack.THATCHER(star_choice))
    elif operative == 'ASH':
        bot.send_message(message.chat.id, Operatives.Attack.ASH(star_choice))
    elif operative == 'THERMITE':
        bot.send_message(message.chat.id, Operatives.Attack.THERMITE(star_choice))
    elif operative == 'TWITCH':
        bot.send_message(message.chat.id, Operatives.Attack.TWITCH(star_choice))
    elif operative == 'IQ':
        bot.send_message(message.chat.id, Operatives.Attack.IQ(star_choice))
    elif operative == 'MONTAGNE':
        bot.send_message(message.chat.id, Operatives.Attack.MONTAGNE(star_choice))
    elif operative == 'GLAZ':
        bot.send_message(message.chat.id, Operatives.Attack.GLAZ(star_choice))
    elif operative == 'FUZE':
        bot.send_message(message.chat.id, Operatives.Attack.FUZE(star_choice))
    elif operative == 'BLITZ':
        bot.send_message(message.chat.id, Operatives.Attack.BLITZ(star_choice))
    elif operative == 'BUCK':
        bot.send_message(message.chat.id, Operatives.Attack.BUCK(star_choice))
    elif operative == 'BLACKBEARD':
        bot.send_message(message.chat.id, Operatives.Attack.BLACKBEARD(star_choice))
    elif operative == 'CAPITAO':
        bot.send_message(message.chat.id, Operatives.Attack.CAPITAO(star_choice))
    elif operative == 'HIBANA':
        bot.send_message(message.chat.id, Operatives.Attack.HIBANA(star_choice))
    elif operative == 'JACKAL':
        bot.send_message(message.chat.id, Operatives.Attack.JACKAL(star_choice))
    elif operative == 'YING':
        bot.send_message(message.chat.id, Operatives.Attack.YING(star_choice))
    elif operative == 'ZOFIA':
        bot.send_message(message.chat.id, Operatives.Attack.ZOFIA(star_choice))
    elif operative == 'DOKKAEBI':
        bot.send_message(message.chat.id, Operatives.Attack.DOKKAEBI(star_choice))
    elif operative == 'FINKA':
        bot.send_message(message.chat.id, Operatives.Attack.FINKA(star_choice))
    elif operative == 'LION':
        bot.send_message(message.chat.id, Operatives.Attack.LION(star_choice))
    elif operative == 'MAVERICK':
        bot.send_message(message.chat.id, Operatives.Attack.MAVERICK(star_choice))
    elif operative == 'NOMAD':
        bot.send_message(message.chat.id, Operatives.Attack.NOMAD(star_choice))
    elif operative == 'GRIDLOCK':
        bot.send_message(message.chat.id, Operatives.Attack.GRIDLOCK(star_choice))
    elif operative == 'NOKK':
        bot.send_message(message.chat.id, Operatives.Attack.NOKK(star_choice))
    elif operative == 'AMARU':
        bot.send_message(message.chat.id, Operatives.Attack.AMARU(star_choice))
    elif operative == 'KALI':
        bot.send_message(message.chat.id, Operatives.Attack.KALI(star_choice))
    elif operative == 'IANA':
        bot.send_message(message.chat.id, Operatives.Attack.IANA(star_choice))
    elif operative == 'ACE':
        bot.send_message(message.chat.id, Operatives.Attack.ACE(star_choice))
    elif operative == 'ZERO':
        bot.send_message(message.chat.id, Operatives.Attack.ZERO(star_choice))
    elif operative == 'FLORES':
        bot.send_message(message.chat.id, Operatives.Attack.FLORES(star_choice))
    elif operative == 'OSA':
        bot.send_message(message.chat.id, Operatives.Attack.OSA(star_choice))
    else:
        bot.send_message(message.chat.id, "Такого оперативника нету в этом спецотряде напишите /zadanie чтобы получить задания")


#Ответы на различный текст 
@bot.message_handler(content_types=['text'])
def start_message(message):
    texts = message.text.lower()
    if texts == "привет":
        bot.send_message(message.chat.id, 'Привет. Я бот Степан я буду давать тебе задания на игру R6')
    else:
        bot.send_message(message.chat.id, 'Я вас не понял напишите /help для навигации')


#Получение данных из базы. Данная функция сделанна воизбежания проблем с потоками
def parss_from_db_parss():
    global attak 
    global protection
    attak = Attack_parss()
    protection = Protection_parss()

#Функция для запуска бота
def main():
    print(pyfiglet.figlet_format("R6Stasks_bot", font="slant"))
    print(Fore.RED + 'Connection successful')
    a = str(input())
    a = a.lower()
    if a =="off":
        bot.stop_polling()
    elif a =="on":
        bot.polling()
    else:
        print(Fore.RED + "Connection unsuccessful")

    input()


if __name__ == "__main__":
    parss_from_db_parss()
    main()
