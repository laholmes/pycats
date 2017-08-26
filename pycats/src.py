__all__ = ['cat_anon', 'cat_lump', 'as_cat', 'cat_collapse',
           'cat_other']

import pandas as pd
import numpy as np


def cat_lump(f, n=None, other_level='Other'):
    levels = f.cat.categories
    counts = f.value_counts()
    
    if n is not None and 0 < n < len(counts):
        lump_cutoff = counts.iloc[n]

        # checking for ties
        if len(counts[counts == lump_cutoff]) > 1:
            select_from_tied = n - len(counts[counts > lump_cutoff])
            random_tie_cats = counts[counts == lump_cutoff].sample(select_from_tied).index.values
            print(random_tie_cats)
            f = f.apply(lambda row: row if not in_smallest(row, counts.to_dict(), lump_cutoff)
                or row in random_tie_cats else other_level)
        else:
            f = f.apply(lambda row: row if not in_smallest(row, counts.to_dict(), lump_cutoff) else other_level)
    elif n is not None and (-1*len(counts)) < n < 0:
        lump_cutoff = counts.iloc[n]
        # checking for ties        
        if len(counts[counts == lump_cutoff]) > 1:
            select_from_tied = (-1*n) - len(counts[counts < lump_cutoff])
            random_tie_cats = counts[counts == lump_cutoff].sample(select_from_tied).index.values
            f = f.apply(lambda row: row if not in_largest(row, counts.to_dict(), lump_cutoff)
                or row in random_tie_cats else other_level)
        else:
            f = f.apply(lambda row: row if not in_largest(row, counts.to_dict(), lump_cutoff) else other_level)
    return f.astype('category')


def in_smallest(level, counts, cutoff):
    return counts[level] <= cutoff


def in_largest(level, counts, cutoff):
    return counts[level] >= cutoff


def cat_collapse(f, groups):
    for key in groups:
        f = f.apply(lambda row: key if row in groups[key] else row)
    return f.astype('category')


def as_cat(x):
    return x.astype('category')


def cat_anon(f):
    category_count = len(f.cat.categories)
    anon_levels = np.random.choice(10000000, category_count, replace=False)
    return f.cat.rename_categories(anon_levels)


def cat_other(f, drop, other_level = 'Other'):
    f = f.apply(lambda row: row if row not in drop else other_level)
    return f.astype('category')

def cat_drop(f, in_place=False):
    return f.cat.remove_unused_categories(in_place)
