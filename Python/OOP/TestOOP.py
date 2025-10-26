class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I'm an animal")

class Dog(Animal):
    def test(self):
        print("Test a dog")
    def speak(self):
        print(f"{self.name} says Woof!")

# Test
dog.speak()  # Milo says Woof!
