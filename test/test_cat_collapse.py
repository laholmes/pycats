import unittest
import pycats
import pandas as pd
import collections


class TestCatCollapse(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = pd.DataFrame({ 
        'a': [4,1,9,6,3,2,3,2,9],
        'b': ['foo', 'foo', 'foo', 'foo2', 'bar', 'bar', 'bar2', 'baz', 'baz2']
        })

        self.groups = {
            'collapse_bar': ['bar', 'bar2'],
            'collapse_foo': ['foo','foo2']
        }

    def test_collapse(self):
        x_cat = self.x['b'].astype('category')
        collapsed_cats = pycats.cat_collapse(x_cat, self.groups)
        remaining_cats = ['collapse_bar', 'collapse_foo', 'baz', 'baz2']
        self.assertTrue(collections.Counter(collapsed_cats.cat.categories) == collections.Counter(remaining_cats))

if __name__ == '__main__':
    unittest.main()
