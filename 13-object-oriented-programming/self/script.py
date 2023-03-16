class SearchEngineEntry:
    secure_prefix = ""

    def __init__(self, url):
        self.url = url


codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.com")

print(codecademy.url)
print(wikipedia.url)


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.radius)
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
