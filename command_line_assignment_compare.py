import filecmp
import sys
import shutil
import argparse

def comparefile(src_file, dest_file):
	
	
	src_fd = open(src_file)
	dest_fd = open(dest_file)
	
	
	if filecmp.cmp(src_file, dest_file):
		print ("Files are equal")
	else:
		print ("Files are unequal")
	src_fd.close()
	dest_fd.close()
    
def main():
	print(sys.argv)
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", type=str, help="Input/Source File Name")
	parser.add_argument("-o", type=str, help="Destination File Name")
	args = parser.parse_args()
	comparefile(args.i, args.o)
    
if __name__ == "__main__":
	main()
