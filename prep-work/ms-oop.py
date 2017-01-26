import sys

class Animal(object):

  population = 0


  @classmethod
  def populationCount(cls):
    return cls.population

  def __init__(self, name, fav_food):
    self.name = name
    self.favoriteFood = fav_food
    Animal.population += 1

  def sleep(self):
        print self.name + ' sleeps for 8 hours'

  def eat(self, food):
      print self.name + ' eats ' + food
      if food == self.favoriteFood:
        print 'YUM! ' + self.name + ' wants more ' + food

class Tiger(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        Animal.__init__(self, name, 'meat')

class Bear(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        Animal.__init__(self, name, 'fish')

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print self.name + ' hibernates for 4 months'

class Unicorn(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        Animal.__init__(self, name, 'marshmallows')

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print self.name + ' sleeps in a cloud'

class Giraffe(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        Animal.__init__(self, name, 'leaves')

    def eat(self, food):
      print self.name + ' eats ' + food
      if food == self.favoriteFood:
        print 'YUM! ' + self.name + ' wants more ' + food
      else:
        print 'YUCK! ' + self.name + ' spits out ' + food

class Bee(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        Animal.__init__(self, name, 'pollen')

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print self.name + ' never sleeps'

    def eat(self, food):
      print self.name + ' eats ' + food
      if food == self.favoriteFood:
        print 'YUM! ' + self.name + ' wants more ' + food
      else:
        print 'YUCK! ' + self.name + ' spits out ' + food

class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print self.name + ' is feeding ' + food + ' to ' + str(len(animals)) + ' of ' + str(Animal.populationCount()) + ' total animals'
        for animal in animals:
          animal.eat(food)
          animal.sleep()