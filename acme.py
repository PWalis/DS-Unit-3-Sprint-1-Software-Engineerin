import random
import unittest

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
            identifier=None):
            self.name = name
            self.price = price 
            self.weight = weight
            self.flammability = flammability
            self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        '''
        calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        '''
        calc = self.price/self.weight
        if calc < 0.5:
            print('Not so stealable')
        if (calc >= 0.5)&(calc<1.0) :
            print('Kinda stealable')
        if calc>=1.0:
            print('Very stealable!')


    def explode(self):
        '''
        calculates the flammability times the weight, and then
        returns a message: if the product is less than 10 return "...fizzle.", if it is
        greater or equal to 10 but less than 50 return "...boom!", and otherwise
        return "...BABOOM!!"
        '''
        pop = self.flammability*self.weight
        if pop<10:
            print('...fizzle.')
        if (pop>=10)&(pop<50):
            print('...boom!')
        if pop>=50:
            print('...KABOOM!!')


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
            identifier=None):
        super().__init__(name=name, price=price, weight=weight, flammability=flammability,
             identifier=identifier)

    def explode(self):
        print("it's a glove...")

    def punch(self):
        '''
        punch method returns "That tickles." if the weight is below 5,
        "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
        "OUCH!" otherwise
        '''
        power = self.weight
        if power<5:
            print('That Tickles')
        if (power>=5)&(power<15):
            print('Hey that hurt!')
        if power >= 15:
            print('OUCH!')
        
        