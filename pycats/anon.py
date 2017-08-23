import pandas as pd
import numpy as np

def cat_anon(f):
    category_count = len(f.cat.categories)
    anon_levels = np.random.choice(10000000,len(category_count),replace=False)
    return f.cat.rename_categories(anon_levels)
