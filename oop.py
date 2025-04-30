# Base Class
class Animal:
    def move(self):
        pass  # Placeholder for polymorphism

# Derived Classes
class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Bird(Animal):
    def move(self):
        return "Flying 🐦"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

# Using Polymorphism
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(animal.move())
