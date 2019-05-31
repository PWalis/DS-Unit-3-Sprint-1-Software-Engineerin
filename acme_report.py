from acme import Product
import random 
from statistics import mean

adjectives = ['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved']

nouns = [' Anvil', ' Catapult' ' Disguise' ' Mousetrap', ' ???']

def generate_name():
    name_list = random.sample(adjectives, 1), random.sample(nouns, 1)
    name_tup = name_list[0][0],name_list[1][0]
    name = ''.join(name_tup)
    return name_list

def generate_products(number=30):
    number = number
    x=[]
    for i in range(0, number):
        name = generate_name()
        prod = Product(name, price=random.randint(5, 100), weight=random.randint(5, 100),
            flammability=random.uniform(0.0, 2.5))
        x.append(prod)
    return x

# prod_list = generate_products()

def inventory_report(products):
    unique_list=[]
    price_list=[]
    weight_list=[]
    flammability_list=[]
    for i in products:
        price_list.append(i.price)
        weight_list.append(i.weight)
        flammability_list.append(i.flammability)
        if i.name not in unique_list:
            unique_list.append(i.name)

    print('ACME CORPRATION OFFICIAL INVENTORY REPORT',
            '\nUnique Product Names:', len(unique_list),
            '\nAverage Price:', mean(price_list),
            '\nAverage Weight:', mean(weight_list),
            '\nAverage Flammability', mean(flammability_list))

# inventory_report(prod_list)

if __name__ == '__main__':
    inventory_report(generate_products())
    


# def inventory_report():
