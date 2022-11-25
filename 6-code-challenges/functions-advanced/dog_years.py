def dog_years(name, age):
    return "{name}, you are {age} years old in dog years".format(name = name, age = age * 7)


print(dog_years("Lola", 16))
print(dog_years("Baby", 0))
