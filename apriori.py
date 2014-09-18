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

def sup_count(trans):
	"""
	returns a dictionary that is hashed by the item
	and whose value is the count of itemsets
	"""
	dic = {}
	for tup in trans:
		for e in tup:
			if e in dic:
				dic[e] = dic[e] + 1
			else:
				dic[e] = 1
	return dic

def frequent_1_itemset(dic, min_sup):
	"""
	takes the dictionary of 1-itemsets and return the 1-frequrnt 
	itemsets list
	"""
#	temp = {}
	l1 = []
	for e in sorted(dic.keys()):
		if dic[e] >= min_sup:
#			temp[e] = dic[e]
			l1.append([e,dic[e]])
	return l1
"""
def gen2c(l1):

	takes in 1-frequent ietmset list and returns 2-candidate itemset list
	i = 0
	j = 0
	c2 = []
	print "frequent"
#	print l1
	print "list"
	while i <= len(l1)-2:
		j = i + 1

		while  j < len(l1):
			index = j
			newList = []
			newList.append(l1[i])
			while index <= j :
				newList.append(l1[index])
				index = index + 1
			j = j + 1
			c2.append(newList)
		i = i + 1
	return c2
"""
def sup_count_ck(ck, trans):
	temp = []
	
	for l in ck:
		flag = 0
		count = 0
		for items in trans:
			flag = 0
			for e in l:
#				print items,
				if e not in items:
					flag = 1
			if flag == 0:
				count = count + 1 
		temp.append(count)
	return temp
#	apiori_gen(c2)	


def genkc(freqk_1,k):
	"""
	generates the kth candidate itemset 
	return a list of k-canddate itemset
	"""
	last_item = 0
	i = 0
	j = 1
	temp = []
	length = len(freqk_1)
	while i < length - 2:
		j = i + 1
		while j < length - 1:
			templist= []
			if freqk_1[i][:k-2] == freqk_1[j][:k-2]:
				last_item = freqk_1[j][k-2]
				for e in freqk_1[i]:
					templist.append(e)
				templist.append(last_item)
				temp.append(templist)
			j = j + 1
		i = i +1
	return temp

def prune(candidate,supp,min_sup):
	"""
	returns  a list of frequent itemset that satisfies the min_sup
	"""
	i = 0
	for e in supp:
		if e < min_sup:
			del(candidate[i])

		else:
			i = i + 1
	return candidate


def mining_association_rules(trans, patterns, supports, confidence):
	"""We will find a way out soon
	"""
	print "\n\n\n"
	for e in patterns:
		for element in e:
			 i = 0
			 while i < len(element):
				 j = i+1
				 while j<len(element):
					 print element[i], " -->", element[j]
					 j = j + 1
				 i = i + 1 ;
			
	

def main():
	"""give input as python apriori.py <inputfile> <support> <confidence>
	"""
	if len(sys.argv) <= 3:
		print "\n\ngive input as python apriori.py <inputfile> <support> <confidence>\n\n"
		exit(-1)

	min_sup = (float)(sys.argv[2])
	confidence = (float)(sys.argv[3])
	num_of_trans = 0
	trans, num_of_trans = readfile(sys.argv[1])
	min_sup = ((min_sup/100.0) * num_of_trans)
	k = 1
	dic = {}
	dic =  sup_count(trans)
	
	dic1 = []
	dic1 = frequent_1_itemset(dic, min_sup)
	
	l1 = []
	temp = []
	for e in dic1:
		temp = []
		temp.append(e[0])
		l1.append(temp)
	c2 = []
#	c2 = gen2c(l1)
	c2 =  genkc(l1,2)	
	supp = []
	supp = sup_count_ck(c2,trans)
	print "this is min sup ",min_sup,"\n\n"
	
	c2 = prune(c2,supp,min_sup)
	
	supp = sup_count_ck(c2,trans)	
	final_supports = []
	final_supports.append(supp)
	
	frequent_patterns = []
	frequent_patterns.append(c2)
	index = 0
	ck = []
	while frequent_patterns[index]:
		index = index + 1 
		ck = genkc(frequent_patterns[index-1],index + 2)
		supp = sup_count_ck(ck,trans)
		ck =  prune(ck, supp,min_sup)
		supp = sup_count_ck(ck,trans)
		final_supports.append(supp)
		frequent_patterns.append(ck)
#	print "this is it"
	frequent_patterns.pop()
	print "Here are the frequent patterns"
	print frequent_patterns
#	for e in frequent_patterns:
#		if len(e)>0:
#			print e
#	print "there should be some gap"
	final_supports.pop()
#	for e in final_supports:
#		if len(e)>0:
#       		print e
	print "\n\nThe Respective final supports"
	print final_supports
#	mining_association_rules(trans, frequent_patterns, final_supports,confidence)




if __name__ =='__main__':
	"""input of the form "python apriory.py filename min_sup"""
	main()


