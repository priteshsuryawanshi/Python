import sys
import shutil
import argparse

def appendfile(src_file, dest_file):
	src_fd = open(src_file,"a")
	dest_fd = open(dest_file)
	
	line = dest_fd.readline()
	while line != "":
		src_fd.write(line)
		line = dest_fd.readline()
	src_fd.flush()
	
	src_fd.close()
	dest_fd.close()
    
def main():
	print(sys.argv)
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", type=str, help="Input/Source File Name")
	parser.add_argument("-a", type=str, help="File to be appended")
	args = parser.parse_args()
	appendfile(args.i, args.a)
    
if __name__ == "__main__":
	main()
