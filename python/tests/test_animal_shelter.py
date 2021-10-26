from stack_queue_animal_shelter.stack_queue_animal_shelter import Dog, Cat, Animal_shelter


def test_cat_shelter_enqueue():
    animal = Animal_shelter()
    cat = Cat("mishmish")
    expected = "the cat was added"
    actual = animal.enqueue(cat)
    assert expected == actual


def test_dog_shelter_enqueue():
    animal = Animal_shelter()
    dog = Dog("mishmish")
    expected = "the dog was added"
    actual = animal.enqueue(dog)
    assert expected == actual


def test_cat_shelter_dequeue():
    animal = Animal_shelter()
    cat1 = Cat("mishmish")
    cat2 = Cat("sammora")
    animal.enqueue(cat1)
    animal.enqueue(cat2)
    expected = "sammora"
    actual = animal.dequeue('cat')
    assert expected == actual


def test_dog_shelter_dequeue():
    animal = Animal_shelter()
    dog1 = Dog("wolf")
    dog2 = Dog("husky")
    animal.enqueue(dog1)
    animal.enqueue(dog2)
    expected = "husky"
    actual = animal.dequeue('dog')
    assert expected == actual
