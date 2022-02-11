import random

#list of answers for program to output
answers = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

#set variables to empty strings to facilitate while loops
name = ""
question = ""

#ensure user input
while name == "":
    name = input("What is your name?   ")
while question == "":
    question = input("What is your question?   ")

#pick a random answer from list of answers above
answer = answers[random.randint(0,len(answers))]

#output it all
print(name, "asks:", question)
print("Magic 8-Ball's answer:", answer)
