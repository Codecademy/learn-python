def username_generator(first_name, last_name):
    username = first_name[0:3] + last_name[0:4]
    return username


def password_generator(username):
    password = ""
    for temp in range(0, len(username)):
        password += username[temp - 1]
    return password


username = username_generator("Abe", "Simpson")
print(username)
print(password_generator(username))
