import pandas as pd

def cat_collapse(f, groups):
    for key in groups:
        print(key)
        f = f.apply(lambda row: key if row in groups[key] else row)
    return f
