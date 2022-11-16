import random

def get_answer(): 
    answer = ""   
    random_number = random.randint(1,9)
    print(random_number)
    if random_number == 1:
        answer = "yes"
    elif random_number == 2:
        answer = "it is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    else:
        answer = "Error"
    print(name + " asks: " + question )
    print(answer)


name = input("enter your name:")
if name == "":
    print("please enter your name")
    name = input("enter your name:")
else:
    print("hello " + name)

question = input("enter a yes or no question: ")
if question == "":
    print("try again")
    question = input("enter a yes or no question: ")
else:
    get_answer()

