def swap(string1, string2):
	string3 = string1[:2] + string2[2:]
	string4 = string2[:2] + string1[2:]
	print string3,string4

def main():
	string1 = input ("Enter first string :")
	string2 = input ("Enter second string :")
	swap(string1, string2)
	
if __name__ == "__main__":
	main()