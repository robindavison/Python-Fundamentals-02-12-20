# create a Class
class Animal:
    def __init__(self, name, animal_type):
        print("Animal", name, "of type", animal_type, "was created")

        self.name = name
        self.animal_type = animal_type

    def noise(self):
        if self.name == "snake":
            return "sssssssssss"
        elif self.name == "dog":
            return "Woof Woof"
        elif self.name == "duck":
            return "Quack Quack"
        else:
            return "No noise"

    def walk(self):
        if self.name == "snake":
            return self.name + " does not walk"
        elif self.name == "dog":
            return self.name + " starts walking"
        elif self.name == "duck":
            return self.name + " starts waddling"
        else:
            return self.name + " does nothing"

    def eat(self, food):
        if (self.name == "snake" and food == "rat") or \
                (self.name == "dog" and food == "steak") or \
                (self.name == "duck" and food == "bread"):
            return self.name + " eats the " + food
        else:
            return self.name + " does not eat " + food

# ####end of Class: Animal


dog = Animal("dog", "Mammal")
snake = Animal("snake", "Reptile")
duck = Animal("duck", "Bird")

print("Dog says", dog.noise())
print("Snake says", snake.noise())
print("Duck says", duck.noise())

print(dog.walk())
print(snake.walk())
print(duck.walk())

print((snake.eat("rat")))
print(snake.eat("pasta"))
print(dog.eat("rat"))
print(dog.eat("steak"))
print(duck.eat("steak"))
print(duck.eat("bread"))
