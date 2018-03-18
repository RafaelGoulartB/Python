# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

falas = ['oi', 'olá','bom dia', 'opá','Como vai? ','estou bem']

bot.set_trainer(ListTrainer)
bot.train(falas)

while True:
    question = str(input("You: "))
    if question == "quit":
        break
    answer =  bot.get_response(question)
    if float(answer.confidence) > 0.5:
        print('Bot: ', answer)
    else:
        print("Bot:  Não entendi")

    if question == "quit":
        break