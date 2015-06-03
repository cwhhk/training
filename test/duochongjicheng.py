__author__ = 'chenwei'
#coding:utf-8

class Animal(object):
    pass

class Mammal(Animal):
    pass
class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print "Running..."
class Flyable(object):
    def fly(self)
        print "Flying..."

class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird,Flyable):
    pass
class Ostrich(Bird,Runnable):
    pass




