def count(text):
	vowel_count = 0
	consonant_count = 0
	text=text.lower()
	for i in text:
		if ( i == "a" or i == "e" or i == "i" or i == "o" or i == "u" ):
			vowel_count=vowel_count+1
		else:
			consonant_count=consonant_count+1
	print ("Number of vowels and consonants in the given string %s are %d and %d respectively")%(text, vowel_count, consonant_count) 
	



def main():
	text = input("Enter a string : ")
	count(text)
	
if __name__ == "__main__":
	main()