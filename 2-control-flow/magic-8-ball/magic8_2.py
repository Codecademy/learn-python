import random

random_number = random.randint(1, 11)

name = "Leo"
question = "Are our cats cute?"
answer = ""

# print(random_number)

if (random_number == 1):
    answer = "Yes - definitely."
elif (random_number == 2):
    answer = "It is decidedly so."
elif (random_number == 3):
    answer = "Without a doubt."
elif (random_number == 4):
    answer = "Reply hazy, try again."
elif (random_number == 5):
    answer = "Ask again later."
elif (random_number == 6):
    answer = "Better not tell you now."
elif (random_number == 7):
    answer = "My sources say no."
elif (random_number == 8):
    answer = "Outlook not so good."
elif (random_number == 9):
    answer = "Very doubtful."
elif (random_number == 10):
    answer = "Interesting question."
elif (random_number == 11):
    answer = "I don't understand."
else:
    answer = "Error"

if (not len(name) == 0) and (not len(question) == 0):
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
elif (len(name) == 0) and (not len(question) == 0):
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
elif (question == ""):
    print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
