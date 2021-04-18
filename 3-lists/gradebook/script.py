last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

print(gradebook)

computer_science = ['computer science', 100]
gradebook.append(computer_science)

#print(gradebook)

visual_arts = ['visual arts', 93]
gradebook.append(visual_arts)

#print(gradebook)

gradebook[-1][-1] += 5

#print(gradebook)

gradebook[2].remove(85)
gradebook[2].append('Pass')

#print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)