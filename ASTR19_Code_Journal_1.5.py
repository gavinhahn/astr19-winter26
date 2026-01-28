# Code Journal 1.5

'''
Write a Python program that writes out a table of the function 
sin(x) vs. x, where x is tabulated between 0 and 2 with a 
thousand entries. Follow the basic Python program structure, 
including a main program function.
'''

import numpy as np
from tabulate import tabulate
from astropy.table import Table 

def main():
	min_x = 0
	max_x = 2*np.pi
	count = 1000

	x_col = make_array(min_x,max_x,count) # make x values
	y_col = np.sin(x_col)                 # make y values
 
	table_data = [(a, b) for a, b in zip(x_col,y_col)] # create x,y tuples
	table_headers = ["x","sin(x)"] # make headers

	table = tabulate(table_data, tablefmt="grid", headers=table_headers,
		floatfmt=".3f") # create tabulate table

	print(table) # print table

	'''
	astropy_table = Table()
	astropy_table["x"] = x_col
	astropy_table["y"] = y_col

	astropy_table["x"].format = "{:.3f}"
	astropy_table["y"].format = "{:.3f}"

	print(astropy_table)
	'''


def make_array(min,max,num):
	return np.linspace(min,max,num)


if __name__ == "__main__":
	main()



	