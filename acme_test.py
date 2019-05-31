
from acme import Product, BoxingGlove
from acme_report import generate_products, adjectives, nouns
import unittest 


class product_tester(unittest.TestCase):

    def test_product(self):
        prod = Product('A Cool Toy')
        self.assertEqual(prod.name, 'A Cool Toy')
        self.assertEqual(prod.price, 10)
        prod.explode()
        prod.stealability()
    
    def test_stealability(self):
        prod = Product('A Cool Toy', price=500)
        prod.stealability()

    def test_explode(self):
        prod = Product('A Cool Toy', flammability=60)
        prod.explode()


    def test_BoxingGLove(self):
        glove = BoxingGlove('Punchy the third')
        self.assertEqual(glove.name, 'Punchy the third')
        self.assertEqual(glove.weight, 10)
        self.assertEqual(glove.price, 10)
        glove.explode()
        glove.punch()
    
class AcmeReportTest(unittest.TestCase):

    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        gen_list = generate_products()
        for i in gen_list:
            self.assertIn(i.name[0][0], adjectives)
            self.assertIn(i.name[1][0], nouns)


if __name__ == '__main__':
    unittest.main()
