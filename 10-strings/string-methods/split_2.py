greatest_guitarist = "santana"

print(greatest_guitarist.split("n"))
print(greatest_guitarist.split("a"))

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")

print(author_names)

author_last_names = []
for author_name in author_names:
    author_last_names.append(author_name.split()[-1])

print(author_last_names)
