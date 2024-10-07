class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
# __eq__
print(h1 == h2)
# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)
# __iadd__
h1 += 10
print(h1)
# __radd__
h2 = 10 + h2
print(h2)
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__