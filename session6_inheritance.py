# create a Class
class Animal:
    def __init__(self, name, animal_type):
 #       print("Animal", name, "of type", animal_type, "was created")

        self.name = name
        self.animal_type = animal_type

    def walks(self):
        return self.name + " does not walk"

    def eats(self, food):
        return self.name + " does not eat"

    def noise(self):
        return self.name + " does not make a noise"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "Dog", "Mammal")

    def walks(self):
        return self.name + " starts walking"

    def noise(self):
        return self.name + " says woof woof"

    def eats(self, food):
        if food == "steak":
            return self.name + " eats " + food
        else:
            return self.name + " does not eat " + food


class Duck(Animal):
    def __init__(self):
        Animal.__init__(self, "Duck", "Bird")

    def walks(self):
        return self.name + " starts waddling"

    def noise(self):
        return self.name + " says quack quack"

    def eats(self, food):
        if food == "bread":
            return self.name + " eats " + food
        else:
            return self.name + " does not eat " + food


class Snake(Animal):
    def __init__(self):
        Animal.__init__(self, "Snake", "Reptile")

    def walks(self):
        return self.name + " starts slithering"

    def noise(self):
        return self.name + " says sssssss"

    def eats(self, food):
        if food == "rat":
            return self.name + " eats " + food
        else:
            return self.name + " does not eat " + food


dog = Dog()
#print(dog.walks())
#print(dog.noise())
#print(dog.eats("steak"))
#print(dog.eats("cheese"))

duck = Duck()
#print(duck.walks())
#print(duck.noise())
#print(duck.eats("bread"))
#print(duck.eats("lemons"))

snake = Snake()
#print(snake.walks())
#print(snake.noise())
#print(snake.eats("rat"))
#print(snake.eats("lemons"))
