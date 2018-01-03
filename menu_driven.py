def add():
	num1 = input ("Enter first number : ")
	num2 = input ("Enter second number : ")
	return num1 + num2

def sub():
	num1 = input ("Enter first number : ")
	num2 = input ("Enter second number : ")
	return num1 - num2

def mul():
	num1 = input ("Enter first number : ")
	num2 = input ("Enter second number : ")
	return num1 * num2
	
def div():
	num1 = input ("Enter Dividend : ")
	num2 = input ("Enter divisor : ")
	return num1 / num2

def main():
	while True:
		choice = input (" Enter your choice : \n1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE\n5. EXIT\n ")
		if choice == 1:
			print ("The sum is %d"%(add()))
		elif choice == 2:
			print ("The difference is %d"%(sub()))
		elif choice == 3:
			print ("The product is %d"%(mul()))
		elif choice == 4:
			print ("The division is %d"%(div()))
		else:
			break

if __name__ == "__main__":
	main()