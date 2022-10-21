import random

name = ""
question = ""
answer = ""

random_number = random.randint(1, 11)
#print(random_number)
#to test randomness

#core logic w/ additional random answers
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Hmmmm, I am not so sure."
elif random_number == 11:
  answer = "You bet, haha!"
else:
  answer = "Error"

#personalizing the replies
if name == "" and question != "":
  print ("Question:",question)
  print ("Magic 8-Ball's answer:",answer)
elif name == "" and question == "":
  print ("You forgot to ask 8-Ball your question.")
elif name != "" and question == "":
  print ("You forgot to ask 8-Ball your question,", name+".")
else:
  print (name,"asks:",question)
  print ("Magic 8-Ball's answer:",answer)
