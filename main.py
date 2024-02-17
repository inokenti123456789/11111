import random


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.age = 0
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(5, 10)

    def sleep(self):
        self.energy += 2
        print(f"{self.name} is sleeping. Energy level increased to {self.energy}.")

    def play(self):
        if self.energy >= 3:
            self.energy -= 3
            self.hunger += 1
            print(f"{self.name} is playing. Energy decreased to {self.energy}. Hunger increased to {self.hunger}.")
        else:
            print(f"{self.name} is too tired to play.")

    def eat(self):
        if self.hunger >= 2:
            self.hunger -= 2
            print(f"{self.name} is eating. Hunger decreased to {self.hunger}.")
        else:
            print(f"{self.name} is not hungry.")

    def __str__(self):
        return f"{self.name} is a {self.species} with age {self.age}, hunger level {self.hunger}, and energy level {self.energy}."

    cat = Pet("Whiskers", "cat")

    dog = Pet("Buddy", "dog")

    print(cat)
    cat.sleep()
    cat.play()
    cat.eat()

    print(dog)
    dog.sleep()
    dog.play()
    dog.eat()