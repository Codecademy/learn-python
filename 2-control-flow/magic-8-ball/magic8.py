import random

name = input("What is your first name? ")
question = input("Ask the Mighty 8-Ball, and she will tell your destiny! ")
random_number = random.randint(1, 9)
answer = ""

if random_number == 1:
  answer += "Yes - definitely."
elif random_number == 2:
  answer += "It is decidedly so."
elif random_number == 3:
  answer += "Without a doubt."
elif random_number == 4:
  answer += "Reply hazy, try again."
elif random_number == 5:
  answer += "Ask again later."
elif random_number == 6:
  answer += "Better not tell you now."
elif random_number == 7:
  answer += "My sources say no."
elif random_number == 8:
  answer += "Outlook not so good."
elif random_number == 9:
  answer += "Very doubtful."
else:
  print("Error! Try again!")

print(name, "asks:", question + "\nMagic 8-Ball's answer:", answer)
