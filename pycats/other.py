def fct_other(f, keep, drop, other_level = "Other"):
	f = f.apply(lambda row: row if row in drop else other_level)
	return f
