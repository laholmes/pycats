# pycats
Tools for working with categorical variables in Pandas (port of features from R forcats package)

## installation
```
pip install pycats
```

## usage
```
import pandas as pd
from pycats import lump  

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

## api
lump.fct_lump  
port of forcats fct_lump - Lump together least/most common factor levels in a categorical variable into "other" (or any custom name)
