def summation(ll, ul):
	sum = 0
	for i in range(ll, ul+1):
		if ( i % 2 != 0):
			sum = sum + i
	return sum
	
def main():
	ll = input("Enter the lower limit :")
	ul = input("Enter the upper limit :")
	print ("The sum of all odd numbers in the given range is %d"%(summation(ll, ul)))
	
if __name__ == "__main__":
	main()
