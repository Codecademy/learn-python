# class Cat:
#     def __init__(self, input_name, input_age = 0, input_vaccination = True):
#         self.name = input_name
#         self.age = input_age
#         self.is_vaccinated = input_vaccination

# cat_one = Cat("Sparky", 2)
# cat_two = Cat("Cinnamon", 1.5, False)  # type: ignore
# print(cat_two.is_vaccinated)

# You can start with the Cat class or erase this and use your own!
class Cat:
    def __init__(self, input_name, input_breed, input_age = 0, input_friendliness = True):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_cuddly = True
        self.is_friendly = input_friendliness
        self.communicating = False

    # Create method where two
    # pets interact.
    # Ex: def name(self, pet):
    def start_communicate(self, other_cat):
        if (other_cat.is_friendly):
            self.communicating = True
            other_cat.communicating = True
            print("{name} start communicating with {other_name}!".format(name = self.name, other_name = other_cat.name))
        else:
            print("{other_name} did not want to communcaite with {name}!".format(name = self.name, other_name = other_cat.name))

# Create two pets.
cat_one = Cat("Alex", "Tabby", 1)
cat_two = Cat("Jack", "Siamese cat", 2)
# Call your method below.

cat_one.start_communicate(cat_two)
