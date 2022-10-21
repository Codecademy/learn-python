# Josh A
# I need to learn Python!

j_line1="JJJJJ"
j_line2="  J  "
j_line3="  J  "
j_line4="  J  "
j_line5="J J  "
j_line6="J J  "
j_line7=" JJ  "

a_line1="  A  "
a_line2=" A A "
a_line3="A   A"
a_line4="AAAAA"
a_line5="A   A"
a_line6="A   A"
a_line7="A   A"

first_letter = "j"
second_letter = "a"

# %s is replaced with 'first_letter' and 'second_letter'
# %s_line1 turns into ${first_letter}_line1 which == j_line1

print( globals()[ '%s_line1' % first_letter] + "  " + globals()[ '%s_line1' % second_letter] )
print( globals()[ '%s_line2' % first_letter] + "  " +  globals()[ '%s_line2' % second_letter] )
print( globals()[ '%s_line3' % first_letter] + "  " +  globals()[ '%s_line3' % second_letter] )
print( globals()[ '%s_line4' % first_letter] + "  " +  globals()[ '%s_line4' % second_letter] )
print( globals()[ '%s_line5' % first_letter] + "  " +  globals()[ '%s_line5' % second_letter] )
print( globals()[ '%s_line6' % first_letter] + "  " +  globals()[ '%s_line6' % second_letter] )
print( globals()[ '%s_line7' % first_letter] + "  " +  globals()[ '%s_line7' % second_letter] )
