from acme import Product, BoxingGlove
import unittest 


class product_tester(unittest.TestCase):

    def test_product(self):
        prod = Product('A Cool Toy')
        self.assertEqual(prod.name, 'A Cool Toy')
        self.assertEqual(prod.price, 10)
        prod.explode()
        prod.stealability()
        

    def test_BoxingGLove(self):
        glove = BoxingGlove('Punchy the third')
        self.assertEqual(glove.name, 'Punchy the third')
        self.assertEqual(glove.weight, 10)
        self.assertEqual(glove.price, 10)
        glove.explode()
        glove.punch()
    
    

if __name__ == '__main__':
    unittest.main()
