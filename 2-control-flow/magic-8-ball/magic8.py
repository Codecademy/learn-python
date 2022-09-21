import random
# create random number from 1 to 9
random_number = random.randint(1, 9)

# taking user name input and question
name = input("Whats your name? ")
question = input("Enter your question ...")
# variables will be used later in the if statement
answer = ""

if random_number == 1:
  answer = "Yes definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not to tell you now."
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

print(name, " asks: ", question)
print("Magic ball answers: ", answer)
