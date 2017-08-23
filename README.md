# pycats :smiley_cat:
Tools for working with categorical variables in Pandas (port of features from R forcats package - https://cran.r-project.org/web/packages/forcats/index.html)

currently in development.

pypi package reference here https://pypi.python.org/pypi/pycats/0.1.4

## installation
```
pip install pycats
```

## usage
```
import pandas as pd
from pycats import lump  
```

```
x = pd.DataFrame({ 
  'a': [4,1,9,6,2,3,5,7,2,9], 
  'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = x['b'].astype('category')
x['b'] = lump.fct_lump(x['b'], 2)
print(x['b'])
```
0      foo  
1      foo  
2      foo  
3      foo  
4      foo  
5      bar  
6      bar  
7      bar  
8    Other  
9    Other  

```
x = pd.DataFrame({ 
  'a': [4,1,9,6,2,3,5,7,2,9],
  b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = fct_other(x['b'], ['foo', 'baz'], ['bar','baz2'])
print(x['b'])
```
0    Other   
1    Other 
2    Other  
3    Other  
4    Other  
5      bar  
6      bar  
7      bar  
8    Other  
9     baz2  


## api

### lump.fct_lump  
port of forcats fct_lump - Lump together least/most common factor levels in a categorical variable into "other" (or any custom name)

### other.fct_other
port of forcats fct_other - replace levels with other
