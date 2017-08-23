import pandas as pd
# Lump together least/most common factor levels into "other"
#
# @param f A factor.
#
# @param n
#   `n` preserves the most common `n` values.
#       default n = None
#   It there are ties, you will get at least `abs(n)` values.
#
# @param other_level Value of level used for "other" values. Always
#   placed at end of levels.
#
# @param ties_method A character string specifying how ties are
#   treated.
#   supported options = ["min", "average", "first"]
#   default = "first"


# TODO: add support for ties method
def fct_lump(f, n=None, other_level='Other', ties_method='first'):
    ties_methods = ['min', 'average', 'first', 'last', 'random']
    if ties_method not in ties_methods:
        raise ValueError('''ties_method not supported. Supported ties_methods are
                         ["min", "average", "first']''')

    levels = f.cat.categories
    counts = f.value_counts()

    if n is not None and n > 0:
        lump_cutoff = counts[n]
        f = f.apply(lambda row: row if not in_smallest(row, counts.to_dict(), lump_cutoff) else other_level)
    return f

# Given vector of counts, returns logical vector if in
# smallest groups
def in_smallest(level, counts, cutoff):
    return counts[level] <= cutoff
