import unittest
import pycats
import pandas as pd
import collections

class TestCatLump(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = pd.DataFrame({ 
            'a': [4,1,9,6,2,3,5,7,2,9], 
            'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
        })

    def test_lump(self):
        as_cat = self.x['b'].astype('category')
        lump_cats = pycats.cat_lump(as_cat, 2)
        remaining_cats = ['foo', 'bar', 'Other']
        self.assertTrue(collections.Counter(lump_cats.cat.categories) == collections.Counter(remaining_cats))


if __name__ == '__main__':
    unittest.main()
