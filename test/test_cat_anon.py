import unittest
import pycats
import pandas as pd

class TestCatAnon(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = pd.DataFrame({ 
            'a': [4,1,9,6,2,3,5,7,2,9],
            'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
        })

    def test_convert_to_anon(self):
        x_cat = self.x['b'].astype('category')
        anon_cats = pycats.cat_anon(x_cat)
        self.assertTrue(type(anon_cats.iloc[0].item()) is int)

    def test_ints_converted(self):
        x_cat = self.x['b'].astype('category')
        anon_cats = pycats.as_cat(self.x['a'])
        self.assertTrue(type(anon_cats.iloc[0].item()) is int)

if __name__ == '__main__':
    unittest.main()
