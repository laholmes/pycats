import unittest
import pycats
import pandas as pd
import collections

class TestCatOther(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = pd.DataFrame({ 
            'a': [4,1,9,6,2,3,5,7,2,9], 
            'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
        })

    def test_other(self):
        other_cats = pycats.cat_other(self.x['b'], ['foo', 'baz'])
        remaining_cats = ['bar', 'baz2', 'Other']
        self.assertTrue(collections.Counter(other_cats.cat.categories) == collections.Counter(remaining_cats))


if __name__ == '__main__':
    unittest.main()
