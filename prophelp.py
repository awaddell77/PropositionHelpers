import itertools


def truth_table(*args):
	prop_names= [str(props) for props in args]
	prop_vals = [[0,1] for props in prop_names]
	print(prop_vals)
	for prop_name in prop_names: print(prop_name, end= '   ')
	print()
	for elements in itertools.product(*prop_vals): print(elements)
