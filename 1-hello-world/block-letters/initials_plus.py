'''
Author:   Mischa Fubler
Purpose:  Brushing up on Python 3 fundamentals for
          Budget App project

This script takes a list of 1 or more characters
and writes it as 'ASCII art' as per codeCademy's 
requirements here: https://www.codecademy.com/courses/learn-python-3/projects/python-block-letters

TODO: create function to take user input.
  Should check that input exists in char_dict
TODO: create function to add char definition
  to char_dict if it doesn't already exist
TODO: Move char_dict to separate file
TODO: check if output_width is wider than terminal width
  warn user if so.
'''

'''
Each dictionary key refers to a list of lists.
Each list stored at an index of the parent list
indicates which 1-index column numbers should
have the key's character printed.
e.g. [1,5] specifies that the first row of the 
M character should have the 1st and 5th column print 
the M character.
This approach makes the printing more complex
Than storing each character of rows in a list
e.g. ['M',' ',' ',' ','M'] or [1,0,0,0,1]
I figured as the character list expands, the storage
required will be considerably less.
Can use print(letters.get('M')[0]) to get the
definition of which columns need M printed in them.
'''
char_dict = {
  
  'D' : [[1,2,3,4]
        ,[1,5]
        ,[1,5]
        ,[1,5]
        ,[1,5]
        ,[1,5]
        ,[1,2,3,4]],
  'F' : [[1,2,3,4,5]
        ,[1]
        ,[1]
        ,[1,2,3]
        ,[1]
        ,[1]
        ,[1]],
  'G' : [[2,3,4]
        ,[1,5]
        ,[1]
        ,[1,2,3,4,5]
        ,[1,5]
        ,[1,5]
        ,[2,3,4]],
  'M' : [[1,5]
        ,[1,2,4,5]
        ,[1,2,4,5]
        ,[1,3,5]
        ,[1,5]
        ,[1,5]
        ,[1,5]]
}

# Change character to print here
chars = ['M','G','F']
char_width = 5
char_height = 7
debug = False
nothing = ''
output_width = char_width * len(chars) + len(chars)-1
space = ' '

def write(chars): 
  # For storing the ASCII print definitions of the letters
  letters = []
  # load character row indexes into letters
  for i, c in enumerate(chars):
    letters.append(char_dict.get(c))
    if debug:
      print(f'First row of letters[{i}]:',letters[i][0])
  '''
  For each row, loop through the characters passed in chars. 
  For each char in chars iterate char_witdh times and
  if current column index + 1 is in current row
  print the char, otherwise print space.
  At the end of each character width, print a space
  At the end of each row move to new line
  '''
  for row in range(char_height): 
    for char_i in range(len(chars)):
      for column in range(char_width):
        if column+1 in letters[char_i][row]:
          print(chars[char_i],end=nothing)
        else: print(space,end=nothing)
      print(space,end=nothing)
    print()

if debug:
  print('Char height: ', char_height)
  print('output width: ',output_width)
write(chars)