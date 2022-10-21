'''For each character in a string, look up the character definition 
  and render it row by row -- think dot matrix printer... :) '''

# Matt Stone
# Dad, Cyclist, Cook


#TODO: add the other letters
alphabet = {
  "M": [
    "M   M",
    "MM MM",
    "MM MM",
    "M M M",
    "M   M",
    "M   M",
    "M   M"
  ],
  "S": [
    " SSS ",
    "S   S",
    "S    ",
    " SSS ",
    "    S",
    "S   S",
    " SSS ",
  ]
}

def render_by_row(initials):
  '''take list of letters, 
  render as ascii art'''
  first_initial = initials[0]
  for i in range(0,len(alphabet[first_initial])):
    row = ""
    for l in initials:
      row = row + (alphabet[l][i]) + " "
    print(row)
 
# run it
my_initials = "MS"
render_by_row(my_initials)

