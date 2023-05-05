############################################
import random
name = "Uriah" # Enter name here or leave as a blank string
question = "Will learning Python 3 be easy?"
answer = ""
random_number = random.randint(1,13) 
#############################################
if random_number == 1:
  answer = "Yes, definitely."
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
  answer = "Not a chance in hell."
#################################################
#################################################
# This code will throw an "ERROR" message if the random number 
# generated is 11, 12, or 13. It will also check the name to see
# if it is a blank string or "Uriah"
# If the name is "Uriah" it will say that name in the terminal
# If the name is blank, it will say "Question: "
if random_number >= 11:
  print ("ERROR")
elif name == "":
    print ("Question: " + question)
    print ("Magic 8-Ball's answer: " + answer)
elif random_number <= 10:
  print (name + " asks: " + question) 
  print ("Magic 8-Ball's answer: " + answer)
################################################## 
