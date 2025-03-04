class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

def play_sound(animal: Animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog)  
play_sound(cat)  
play_sound(cow)
