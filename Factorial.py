def iFactorial (num):   # iterative

i = num
	fact = i

	while i > i:
		fact = fact * i
		i -= 1
	return fact
	
def rFactorial(num):    # recursive
	if num == 1:
		return 1
	else:
		return num * rFactorial (num - 1)

def main():
	
	value = int(input("Enter a number"))
	print ("The iterative factorial is: ", iFactorial (value))
	print ("The recursive factorial is: ", rFactorial (value))
	
main()
