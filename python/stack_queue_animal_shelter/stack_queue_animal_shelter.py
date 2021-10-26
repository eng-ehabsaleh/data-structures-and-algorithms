class Node:
    def __init__(self, value, nxt=None):

        self.value = value
        self.nxt = nxt


class Queue:
    def __init__(self):

        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.nxt = node
            self.rear = node

    def dequeue(self):
        try:
            dequeue = self.front.value
            self.front = self.front.nxt
            return dequeue
        except:
            return ' empty Queue '


class Dog:

    def __init__(self, name):
        self.name = name
        self.kind = 'dog'


class Cat:

    def __init__(self, name):
        self.name = name
        self.kind = 'cat'


class Animal:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


class Animal_shelter:

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):

        if animal.kind == 'cat':
            self.cat.enqueue(animal)
            return ("the cat was added")

        elif animal.kind == 'dog':
            self.dog.enqueue(animal)
            return ("the dog was added")

        else:
            return 'the animal should be cat or dog'

    def dequeue(self, pref=None):

        if pref == 'cat':
            return self.cat.dequeue().name
        elif pref == 'dog':
            return self.dog.dequeue().name
        else:
            return None


if __name__ == "__main__":

    husky = Dog('husky')
    riex = Dog('riex')
    mishmish = Cat('mishmish')
    sinp = Cat('sinp')
    crocudaile = Animal('crocudaile', 'snake')
    ehab = Animal_shelter()
    ehab.enqueue(husky)
    ehab.enqueue(riex)
    ehab.enqueue(mishmish)
    print(ehab.enqueue(sinp))
    print(ehab.enqueue(crocudaile))
    print(ehab.dequeue('cat'))
