from abc import ABC, abstractmethod

# abstract base class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    def name(self):
        pass
    def move(self):
        pass

class Monkey(Animal):
    def single(self):
        print('monkey is signing')

    def eat(self):
        print('eating banana')
layka = Monkey()
print(layka)