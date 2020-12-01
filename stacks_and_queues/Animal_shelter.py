
class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    pass
class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.cats, self.dogs = [], []

    def enqueue(self,animal):
        if isinstance(animal, Cat):
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0: return None
        cat = self.cats.pop(0)
        return cat 

    def dequeueDog(self):
        if len(self.dogs) == 0: return None
        dog = self.dogs.pop(0)
        return dog 

    def dequeueAny(self):
        if len(self.cats): return self.dequeueCat()
        return self.dequeueDog()

        




        
