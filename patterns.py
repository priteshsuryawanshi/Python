def pattern1():
	rows = input("Enter number of rows :")
	for i in range(1,rows+1):
		s=''
		for j in range(i):
			s=s+'*'
		print s
		
def pattern2():
	rows = input ("ENter number of rows :")
	for i in range(rows,0,-1):
		s=''
		for j in range(i):
			s=s+'*'
		print s
		
def pattern3():
	rows = input("Enter number of rows :")
	for i in range(1,rows+1):
		s=''
		for j in range(65,65+i):
			s=s+chr(j)
		print s
		
def main():
	pattern1()
	pattern2()
	pattern3()
	
if __name__ == "__main__":
	main()