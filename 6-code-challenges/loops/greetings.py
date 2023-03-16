def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append('Hello, ' + name)
    return new_list


print(add_greetings(["Owen", "Max", "Sophie"]))
