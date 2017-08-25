import unittest
import pycats
import pandas as pd

class TestCatCollapse(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = pd.DataFrame({ 
        'a': [4,1,9,6,2,3,5,7,2,9],
        'b': ['foo', 'foo', 'foo', 'foo2', 'foo3', 'bar', 'bar', 'bar2', 'baz', 'baz2']
        })

        self.groups = {
            'other': ['bar2', 'baz'],
            'cool': ['foo','foo2']
        }

    def test_collapse(self):
        self.x['b'] = self.x['b'].astype('category')
        collapsed_cats = pycats.cat_collapse(self.x['b'], self.groups)
        remaining_cats = ['other', 'cool', 'bar', 'baz2']
        self.assertEqual(collapsed_cats.cat.categories, remaining_cats)

if __name__ == '__main__':
    unittest.main()
