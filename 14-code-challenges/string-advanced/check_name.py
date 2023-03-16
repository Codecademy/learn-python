def check_for_name(sentence, name):
    return name.lower() in sentence.lower()
print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is JAMIE", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))
