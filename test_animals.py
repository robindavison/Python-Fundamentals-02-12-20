import unittest
from unittest import TestCase
from session6_inheritance import Dog
from session6_inheritance import Snake
from session6_inheritance import Duck


class Test_Animals(TestCase):
    def test_if_dog_is_a_dog(self):
        dog = Dog()
        self.assertEqual(dog.name, "Dog")

    def test_if_snake_is_a_dog(self):
        snake = Snake()
        self.assertEqual(snake.name, "Snake")

    def test_if_duck_is_a_duck(self):
        duck = Duck()
        self.assertEqual(duck.name, "Duck")


    def test_if_animals_can_walk(self):
        dog = Dog()
        snake = Snake()
        duck = Duck()
        self.assertEqual(dog.walks(), "Dog starts walking")
        self.assertEqual(snake.walks(), "Snake starts slithering")
        self.assertEqual(duck.walks(), "Duck starts waddling")


    def test_if_animals_eat(self):
        dog = Dog()
        snake = Snake()
        duck = Duck()
        self.assertEqual(dog.eats("steak"), "Dog eats steak")
        self.assertEqual(dog.eats("pizza"), "Dog does not eat pizza")
        self.assertEqual(snake.eats("Cheese"), "Snake does not eat Cheese")
        self.assertEqual(snake.eats("rat"), "Snake eats rat")
        self.assertEqual(duck.eats("bread"), "Duck eats bread")
        self.assertEqual(duck.eats("cake"), "Duck does not eat cake")


#if __name__ == "__main__":
#    unittest.main()

#