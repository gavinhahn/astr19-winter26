# ASTR 19 Code Journal 1.3

# f(x) function
def f(x):
	return x**3+8 

# main function
def main():
	numIn = 9
	numOut = f(numIn)
	print(numOut)

	# prints "YAY!" if numOut > 27
	if numOut > 27 :
		print("Yay!")

if __name__ == "__main__" :
	main()