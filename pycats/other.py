def cat_other(f, keep, drop, other_level = 'Other'):
	return f.apply(lambda row: row if row in drop else other_level)
