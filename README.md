# pycats
Tools for working with categorical variables in Pandas (port of features from R forcats package)

## installation
```
pip install pycats
```

## usage
```
from pycats import lump
import pandas as pd
x = pd.DataFrame({ 'a': [4,6,2,3], 'b': ['foo', 'foo', 'bar', 'baz']})
x['b'] = x['b'].astype('category')
x['b'] = lump.fct_lump(x['b'], 2)
x['b']

0    NaN
1    NaN
2    bar
3    baz
```

## api
lump.fct_lump
port of forcats fct_lump - Lump together least/most common factor levels in a categorical variable into "other" (or any custom name)
