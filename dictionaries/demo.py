my_dictionary = {
    "song": "Estranged",
    "artist": "Guns N' Roses"
}
print(my_dictionary)
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"
print(my_dictionary)

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key: value for key, value in zip(names, heights)}

dictionary = {
    1: "Hello",
    "two": True,
    "3": [1, 2, 3],
    "Four": {"fun": "addition"},
    5.0: 5.5
}
print(dictionary)
