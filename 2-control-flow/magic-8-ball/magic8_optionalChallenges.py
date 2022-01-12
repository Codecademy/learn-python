# Start by declaring all the variables needed
import random

name = "Joyce"
question = "Will I ever get to go to Egypt again?"
answer = ""
random_number = random.randint(1,20)
# run program several times to check
#print(random_number)

# Time to implement the core logic of our program!
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is certain."
elif random_number == 3:
  answer = "It is decidedly so."
elif random_number == 4:
  answer = "Without a doubt."
elif random_number == 5:
  answer = "You may rely on it."
elif random_number == 6:
  answer = "As I see it, yes."
elif random_number == 7:
  answer = "Most likely."
elif random_number == 8:
  answer = "Outlook good."
elif random_number == 9:
  answer = "Yes."
elif random_number == 10:
  answer = "Without a doubt."
elif random_number == 11:
  answer = "Reply hazy, try again."
elif random_number == 12:
  answer = "Ask again later."
elif random_number == 13:
  answer = "Better not tell you now."
elif random_number == 14:
  answer = "Cannot predict now."
elif random_number == 15:
  answer = "Concentrate and ask again."
elif random_number == 16:
  answer = "Don't count on it."
elif random_number == 17:
  answer = "My reply is 'No.'"
elif random_number == 18:
  answer = "My sources say no."
elif random_number == 19:
  answer = "Outlook not so good."
elif random_number == 20:
  answer = "Very doubtful."
else:
  answer = "Error."

# Now, let's see the program in action!
if name == "" and question == "":
  print("You provided neither a name nor a question. What are you even doing here?")
elif name == "":
  print(question)
  print("Magic 8-Ball's answer: " + answer)
elif question == "":
  print("You didn't ask a question.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)