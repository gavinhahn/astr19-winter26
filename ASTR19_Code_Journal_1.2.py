# Code Journal 1.2

'''
Write a Python program that prints the sum of two floating 
point numbers, the difference between two integers, and the 
product of a floating point number and an integer. In each 
case, have the program print out the data type of the 
resulting answer.
'''

# main function
def main():
	# sum of two floats
	e = 2.718
	pi = 3.141

	e_pi = e+pi 

	print(e_pi)
	print(type(e_pi))

	# diff of two ints
	a = 6
	b = 4

	c = 6-4

	print(c)
	print(type(c))

	# product of float and int
	x = e*a 

	print(x)
	print(type(x))

	

if __name__ == "__main__" :
	main()

