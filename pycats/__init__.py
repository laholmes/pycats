def fct_other(f, keep, drop, other_level = "Other"):
	f = f.apply(lambda row: row if row in drop else other_level)

import pandas as pd
x = pd.DataFrame({ 'a': [4,1,9,6,2,3,5,7,2,9], 'b': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'baz', 'baz2']})
x['b'] = fct_other(x['b'], ['foo', 'baz'], ['bar','baz2'])
print(x['b'])