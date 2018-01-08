def string_count(string1, string2):
	count = 0
	string1 = string1.lower()
	for i in string1:
		if (string2 == i):
			count = count + 1
	print ("Number of times the given string occured is %d"%(count))
	


def main():
	string1 = input("Enter a string :")
	string2 = input("Enter the string to be searched :")
	string_count(string1, string2)
	
if __name__ == "__main__":
	main()