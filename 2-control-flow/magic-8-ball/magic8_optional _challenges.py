import random

name = "Abdelkarim"
question = "Am i having fun!!"

answer = ""

random_number = random.randint(1,12)

#print(random_number)
if random_number == 1:
  answer = "Yes - definitely."

elif random_number == 2:
  answer = "It is decidedly so"

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
  answer = "You should ask yourself that question."

elif random_number == 11:
  answer = "Hmm! i i mean... you you could ..."

elif random_number == 12:
  answer = "That's enough Magic 8-Ball for today."

else:
  answer = "Error"

if question != "" : 
  
  if name != "" :
    print( name , "asks:" , question )
  else:
    print("Question: %s" % question )
  
  print( "Magic 8-Ball's answer: " + answer )

else:
  print("No Questions, No Answers")