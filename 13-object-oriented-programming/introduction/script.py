a_string = "Cool String"
an_int = 12

print(type(a_string))
print(type(an_int))
print(type(5))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))


class Facade:
    pass


facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
