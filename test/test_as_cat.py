import unittest
import pycats
import pandas as pd

class TestAsCat(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = pd.DataFrame({ 
            'a': [4,1,9,6,2,3,5,7,2,9],
            'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
        })

    def test_converts_to_cat(self):
        x_cat = pycats.as_cat(self.x['b'])
        self.assertTrue(x_cat.dtype.name == 'category')

    def test_cats_stay_cats(self):
        x_cat = pycats.as_cat(self.x['b'])
        x_cat = pycats.as_cat(x_cat)
        self.assertTrue(x_cat.dtype.name == 'category')

if __name__ == '__main__':
    unittest.main()
