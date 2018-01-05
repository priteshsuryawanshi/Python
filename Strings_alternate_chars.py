def first_last(string1):
	s = string1[0:2]+string1[:-3:-1][:-3:-1]
	print s
	
def alternate_chars(string1):
	s = string1[0::2]
	print s

def main():
	string1 = input ("Enter a string :")
	first_last(string1)
	alternate_chars(string1)
	
	
	
if __name__ == "__main__":
	main()