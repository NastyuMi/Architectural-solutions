#Відмова від спадкування

class Animal:
    def speak(self):
        pass

    def move(self):
        pass

class Dog:
    def __init__(self):
        self.animal = Animal()

    def speak(self):
        self.animal.speak()

    def move(self):
        self.animal.move()

# Приклад використання
dog = Dog()
dog.speak()
dog.move()
