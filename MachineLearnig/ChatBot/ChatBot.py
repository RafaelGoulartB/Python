from chatterbot.filters import RepetitiveResponseFilter
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('Alfredo',filters=["chatterbot.filters.RepetitiveResponseFilter"])

words = [
    'Hello','How are you?',"I'm fine, and you", "I'm doing great!","What's your name? "
]

chatbot.set_trainer(ListTrainer)
chatbot.train(words)

while True:
    question = str(input("You: "))
    if question == 'quit':
        break
    
    response = chatbot.get_response(question)
    print('Bot:',response)
