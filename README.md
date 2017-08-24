# pycats :smiley_cat:
Tools for working with categorical variables in Pandas (port of features from R forcats package - https://cran.r-project.org/web/packages/forcats/index.html)

currently in development - pre-alpha. Current version 0.1.14

pypi package reference here https://pypi.python.org/pypi/pycats/0.1.14

## installation
```
pip install pycats
```

## dependencies
pandas, numpy

## usage
```
import pandas as pd
import pycats
```

## api

### as_cat(x)
convert a series (column in data frame) to a category  

#### arguments   
x - series to convert to a category  
  
#### returns  
the category representation of the provided series  

#### example  

```
x = pd.DataFrame({ 
  'a': [4,1,9,6,2,3,5,7,2,9], 
  'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = pycats.as_cat(x['b'])

```

### cat_lump(x, n, other_level='Other')  
port of forcats fct_lump - Lump together least/most common factor levels in a categorical variable into "other" (or any custom name)  

#### arguments  
x - category object to lump  
n - threshold number of occurrences below which to lump into other level. i.e. for n = 2, levels occurring <= 2 in x will be lumped together into 'other' level  
other_level - name for the 'other' level which factor levels are converted to  

#### returns  
the lumped version of the provided category object  

#### example  
```
x = pd.DataFrame({ 
  'a': [4,1,9,6,2,3,5,7,2,9], 
  'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = x['b'].astype('category')
x['b'] = pycats.cat_lump(x['b'], 2)
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

### cat_other(x, drop, other_level='Other')  
port of forcats fct_other - replace levels with other  

#### arguments  
x - category object   
drop - list of category levels to replace in x  
other_level - name for the 'other' level which dropped factor levels are converted to  

#### returns  
category object with dropped levels replaced by other_level

#### example  
```
x = pd.DataFrame({ 
  'a': [4,1,9,6,2,3,5,7,2,9],
  b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = pycats.cat_other(x['b'], ['foo', 'baz'], ['bar','baz2'])
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

### cat_anon(x)
port of forcats fct_anon - replace category level names with random integers. Maintains level groupings, does not preserve order or values of original categories

#### arguments  
x - category object  

#### returns  
category object, with each category level replaced by a random number in range [0,10000000]  

#### example  
```
x = pd.DataFrame({
  'a': [4,1,9,6,2,3,5,7,2,9],
  'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']
})
x['b'] = x['b'].astype('category')
x['b'] = pycats.cat_anon(x['b'])
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


### cat_collapse(x, groups)
port of forcats fct_collapse - Collapse factor levels into manually defined groups

#### arguments
x - category object
groups - dictionary, with each key a new category level to use, and each value the list of category levels that the new level should be replaced with. the values are collapsed to the key.

#### returns
category object, with levels matching the specification in groups.

#### example  
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
x['b'] = pycats.cat_collapse(x['b'], groups)
print(x['b'])
```

### cat_drop(x, in_place=False)
thin wrapper on pandas remove_unused_categories. TBD may replace later based on performance

##### arguments
x - category object
in_place - whether or not to drop unused categories inplace or return a copy of this categorical with unused categories dropped

##### returns
category object, with unused levels dropped

##### example
````
````

