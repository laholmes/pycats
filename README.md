# pycats :smiley_cat:
Tools for working with categorical variables in Pandas (port of features from R forcats package - https://cran.r-project.org/web/packages/forcats/index.html)

currently in development - pre-alpha. Current version 0.1.6

pypi package reference here https://pypi.python.org/pypi/pycats/0.1.6

## installation
```
pip install pycats
```

## dependencies
pandas, numpy

## usage
```
import pandas as pd
from pycats import lump, other    
```

## api

### lump.cat_lump  
port of forcats fct_lump - Lump together least/most common factor levels in a categorical variable into "other" (or any custom name)

```
x = pd.DataFrame({ 
  'a': [4,1,9,6,2,3,5,7,2,9], 
  'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = x['b'].astype('category')
x['b'] = lump.cat_lump(x['b'], 2)
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
8      Other  
9      Other  

### other.cat_other
port of forcats fct_other - replace levels with other

```
x = pd.DataFrame({ 
  'a': [4,1,9,6,2,3,5,7,2,9],
  b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = other.cat_other(x['b'], ['foo', 'baz'], ['bar','baz2'])
print(x['b'])
```
0      Other   
1      Other  
2      Other  
3      Other  
4      Other  
5      bar  
6      bar  
7      bar  
8      Other  
9      baz2  

### anon.cat_anon
port of forcats fct_anon - replace category level names with random integers. Maintains level groupings, does not preserve order or values of original categories

```
x = pd.DataFrame({
  'a': [4,1,9,6,2,3,5,7,2,9],
  'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = x['b'].astype('category')
x['b'] = cat_anon(x['b'])
print(x['b'])
```
0    1223194  
1    1223194  
2    1223194  
3    1223194  
4    1223194  
5    6220873   
6    6220873  
7    6220873  
8    2811679  
9     582436 


### cat_collapse
port of forcats fct_collapse - Collapse factor levels into manually defined groups


```
x = pd.DataFrame({
  'a': [4,1,9,6,2,3,5,7,2,9],
  'b': ['foo', 'foo', 'foo', 'foo2', 'foo3', 'bar', 'bar', 'bar2', 'baz', 'baz2']
})

groups = {
	'other': ['bar2', 'baz'],
	'cool': ['foo','foo2']
}

x['b'] = x['b'].astype('category')
x['b'] = cat_collapse(x['b'], groups)
print(x['b'])
```
