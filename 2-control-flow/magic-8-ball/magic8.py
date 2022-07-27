name = "Kirti"
question = "Tomorrow will rain?"
answer = ""
import random
random_number = random.randint(1,9)
a = random_number

if a == 1:
  answer = "Yes - definitely."
elif a == 2:
  answer = "It is decidedly so."
elif a == 3:
  answer = "Without a doubt."
elif a == 4:
  answer = "Reply hazy, try again."
elif a == 5:
  answer = "Ask again later."
elif a == 6:
  answer = "Better not tell you now."
elif a == 7:
  answer = "My sources say no."
elif a == 8:
  answer = "Outlook not so good."
elif a == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

if name == "":
  print("Question: ", question)
elif question == "":
  print("Ask something or fuck off!")
else:
  print(name ," asks: ", question)
  print("Magic 8-Ball's answer: ", answer)
