import random

name = "Joe"
question = "Will I win the lottery?"
answer = ""

random_number = random.randint(1, 12)
# print(random_number)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
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
elif random_number == 10:
    answer = "Most likely definitely yes"
elif random_number == 11:
    answer = "Hard to say, hard to say"
elif random_number == 12:
    answer = "Nothing seems to indicate that"
else:
    answer = "Error"

if question == "":
  print("You are risking the fabric of reality!\nState your question!")
elif name == "":
  print("Question: " + question)
  print("Magic 8-Ball's answear: " + answer)
else:
  print(name + " asks: " + question)
  print("Magic 8 Ball's answer: " + answer)

# Wanted to test out doing a pull request, so I did! Woho!