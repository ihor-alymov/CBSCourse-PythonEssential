from warnings import catch_warnings


class Animal:
    """Proto fo Animal"""

    count_animals = 0

    def __init__(self, name, age, weight, color, voice):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.voice_animal = voice
        Animal.count_animals += 1

    def voice(self):
        print(f"{self.voice_animal}")

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Weight: {self.weight}, Color: {self.color}, Voice: {self.voice_animal}"


dog = Animal("Spike", 4, 5, "Brown", "Woof")
dog.voice()
cat = Animal("Tom", 3, 3, "Black", "Meow")
cat.voice()
zebra = Animal("Marty", 10, 500, "Black and White", "Roar")
zebra.voice()

print(dog)
print(cat)
print(zebra)

print(f"Total number of animals: {Animal.count_animals}")
