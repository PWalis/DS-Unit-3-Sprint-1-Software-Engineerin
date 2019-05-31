from acme import Product
import random 


adjectives = ['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved']

nouns = [' Anvil', ' Catapult' ' Disguise' ' Mousetrap', ' ???']

def generate_name():
    name_list = random.sample(adjectives, 1), random.sample(nouns, 1)
    name_tup = name_list[0][0],name_list[1][0]
    name = ''.join(name_tup)
    return name

def generate_products(number=30):
    x=[]
    for i in range(0, number):
        name = generate_name()
        prod = Product(name, price=random.randint(5, 100), weight=random.randint(5, 100),
            flammability=random.uniform(0.0, 2.5))
        x.append(prod)
    return x

# print(generate_products(2))

def inventory_report():
    

    


# def inventory_report():
