def armstrong(num):
	x=0
	temp = num
	while num:
		r = num % 10
		x = x + r*r*r
		print (x)
		num = num // 10
	if temp == x:
		print ("The given number is ARMSTRONG")
	else:
		print ("The given number is not ARMSTRONG")
		
def main():
	num = eval(input("Enter a number:"))
	armstrong(num)
	
if __name__ == "__main__":
	main()