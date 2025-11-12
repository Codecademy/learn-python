import random
name = ("Leon")
question = ("Will I ever eat a hotdog again?")
answer = ""
random_number = random.randint(1, 12)

#Random number generators for empty string testing
rand_name = random.randint(1, 12)
rand_question = random.randint(1, 12)


#Set argument for name and question var to test empty string results: 
if rand_name == 1: name = ""
else:
  if rand_question == 1: question = ""
  

#Check Random number function
if random_number == 1: answer = 'Yes - definitely'
elif random_number == 2: answer = 'It is decidedly so'
elif random_number == 3: answer = 'Without a doubt'
elif random_number == 4: answer = 'Reply hazy, try again'
elif random_number == 5: answer = 'Ask again later'
elif random_number == 6: answer = 'Better not tell you now'
elif random_number == 7: answer = 'My sources say no'
elif random_number == 8: answer = 'Outlook not so good'
elif random_number == 9: answer = 'Very doubtful'
elif random_number == 10: answer = 'Its possible, maybe tomorrow'
elif random_number == 11: answer = 'It depends on the weather'
elif random_number == 12: answer = 'As long as your wife is not home'
else: answer = 'Error'

#Optional Challenges: tasks 12-14
if question == "": 
  print('You forgot to state your question so:')
  print('The universe is at risk of turning into a hotdog')
else: 
  if name == "": 
    print('No name entered. Only the question will print:')
    print(f'Question: {question}')

  else:
    print(f'{name} asks: {question}')
    print(f'''Magic 8-Ball's answer: {answer}''')



