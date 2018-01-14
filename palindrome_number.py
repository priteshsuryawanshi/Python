def palindrome(num):
	rem = 0
	rev = 0
	num1 = num
	while num1:
		rem = num1 % 10
		rev = rev * 10 + rem
		num1 = num1 // 10
	if (num == rev):
		print ("Number is a palindrome")
	else:
		print ("Number is not a palindrome")

def method2(num):
	num = str(num)
	rev = num[::-1]
	if ( num == rev ):
		print ("Number is a palindrome")
	else:
		print ("Number is not a palindrome")
		
def main():
	num = eval(input("Enter a number :"))
	palindrome(num)
	method2(num)

if __name__ == "__main__":
	main()