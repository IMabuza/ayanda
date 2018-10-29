# This file runs Ayanda
#A chatbot that helps with frequenty asked questions for IOHA

#imports

import random

#Templates

user_template = "You: {}"
bot_template = "Ayanda: {}"


def respond(message):
    #dictionary with questions as keys and lists of appropriate responses as values

    responses = {
        "what are ARVs":["HIV drugs are called antiretrovirals (ARVs) because HIV is a type of virus called a retrovirus. Would you like to ask me another question?", "Antiretrovirals, here is a link to learn more: https://en.wikipedia.org/wiki/Management_of_HIV/AIDS . Would you like to ask me another question?"]
    } 

    if message in responses:
        response = random.choice(responses[message])
        return response
    else:
        return "I don not understand your question, please rephrase it."

def send_message(message):

    if message == "bye":
        print(bot_template.format("Thanks for chatting, have a great one"))
    else:
        #print out bot reponse
        print(bot_template.format(respond(message)))

        #ask for more questions
        message = input("You: ")
        send_message(message)

message = input("You: ")
send_message(message)
