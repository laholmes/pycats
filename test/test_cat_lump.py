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

    def test_negative_lump(self):
        as_cat = self.x['b'].astype('category')
        lump_cats = pycats.cat_lump(as_cat, -2)
        remaining_cats = ['baz', 'baz2', 'Other']
        self.assertTrue(collections.Counter(lump_cats.cat.categories) == collections.Counter(remaining_cats))

    def test_positive_ties(self):
        x = pd.DataFrame({ 
            'a': [4,1,9,6,2,3,5,7,2,4,6,7,4,8,9], 
            'b': ['foo', 'foo', 'foo', 'foo','bar','bar','bar','brr2','brr2','brr2','test1','test1','test2','test2', 'lol']
        })

        x_cat = x['b'].astype('category')
        lump_cats = pycats.cat_lump(x_cat, 2)
        remaining_cats = ['foo', 'bar', 'Other']
        remaining_cats_alt = ['foo', 'brr2', 'Other']

        self.assertTrue(collections.Counter(lump_cats.cat.categories) == collections.Counter(remaining_cats)
            or collections.Counter(lump_cats.cat.categories) == collections.Counter(remaining_cats_alt))

    def test_negative_ties(self):
        x = pd.DataFrame({ 
            'a': [4,1,9,6,2,3,5,7,2,4,6,7,4,8,9], 
            'b': ['foo', 'foo', 'foo', 'foo','bar','bar','bar','brr2','brr2','brr2','test1','test1','test2','test2', 'lol']
        })

        x_cat = x['b'].astype('category')
        lump_cats = pycats.cat_lump(x_cat, -2)
        remaining_cats = ['lol', 'test1', 'Other']
        remaining_cats_alt = ['lol', 'test2', 'Other']

        self.assertTrue(collections.Counter(lump_cats.cat.categories) == collections.Counter(remaining_cats)
            or collections.Counter(lump_cats.cat.categories) == collections.Counter(remaining_cats_alt))

if __name__ == '__main__':
    unittest.main()
