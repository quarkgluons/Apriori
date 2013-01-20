#! /usr/bin/python

import sys

def readfile(filename):
        """reads the input file and gets the transactions in a 
        list named trans that too sorted"""
        f = open(filename,"rU")
        trans = []
        items = []
        num_of_trans = 0
        for line in f:
                num_of_trans = num_of_trans + 1
                temp = line.find(" ")
                line = line[temp+1:]
                items = line.split(", ")
                temp =  items.pop()
                index = temp.find("\n")
                items.append(temp[:index])
                index = 0
                for e in items:
                        items[index] = int(e)
                        index = index + 1
                items.sort()
                trans.append(items)
        return trans, num_of_trans

def read_file(trans):
#	f = open(filename,"rU")
	count  = 0
	for line in trans:
		if 0 in line and 1 in line and  2 in line:
			count = count + 1
	print count

def main():
	trans, num_trans  =readfile(sys.argv[1])
	read_file(trans)


if __name__ == "__main__":
	main()
