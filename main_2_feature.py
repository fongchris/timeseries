from statistics import mean, pstdev
from math import atan, degrees,log
import pickle
import sys

def entropy (prob_list):
	entropy = 0.0
	for p in prob_list:
		entropy = entropy - p*log(p,2)
	return entropy


def rebalance (falphabet):
	prob_sum = 0.0
	new_probs =[]
	new_falphabet = []
	for i in falphabet:
		#print(i[0])
		prob_sum = prob_sum+i[0]

	for i in falphabet:
		a = list(i)
		a[0] = a[0]/prob_sum
		b = tuple(a)
		new_falphabet.append(b)
	#print(prob_sum)
	#print(new_alphabet)
	return new_falphabet
'''
a = [(0.3,1,2,3),(0.3,3,4,5),(0.30,7,8,9)]
b= rebalance(a)
print(b)
'''



def conditional_entropy_list (falphabet,f_number):
	ce_list = []

	done = 0
	loop_size =50
	for v in list(range(1,51)):
		a=[]
		for x in falphabet:
			if x[f_number] == v:
				a.append(x)

		b=rebalance(a)
		prob_list = [x[0] for x in b]
		ce = entropy(prob_list)
		ce_list.append(ce)
		done = done+1
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done/loop_size))
		sys.stdout.flush()
	print('\n')
	return ce_list



def feature_jpdf(falphabet,f1,f2):
	jpdf = []


	comb = []
	for item in falphabet:
		a = (item[f1],item[f2])
		comb.append(a)

	unique_comb = set(comb)

	unique_size = len(unique_comb)
	done =0


	for j in unique_comb:
		prob = 0
		for k in falphabet:
			if j[0]==k[f1] and j[1]==k[f2]:
				prob = prob + k[0]
		jpdf.append((j,prob)) # [((1,2),0.5),((1,3),0.5)]
		done = done+1
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done/unique_size))
		sys.stdout.flush()

	print('\n')
	jpdf.sort()
	return jpdf

	print ("==== Feature: %d JPDF =======" %f1) 
	print ("==== Feature: %d JPDF =======" %f2) 
	print ("Unique Size: %d" %unique_size)

'''
with open('./data/falphabet2.pickle', 'rb') as handle:
  		falphabet = pickle.load(handle)
print(feature_jpdf(falphabet,2,3))
'''


def ce_2feature(falphabet,f1,f2,v1,v2):
	a=[]
	for x in falphabet:
		if x[f1] == v1 and x[f2]==v2:
			a.append(x)
	b=rebalance(a)
	prob_list = [x[0] for x in b]
	ce = entropy(prob_list)
	return ce


def ce_test_final(f1,f2):
	with open('./data/falphabet2.pickle', 'rb') as handle:
		falphabet = pickle.load(handle)


	jdf = feature_jpdf(falphabet,f1,f2)
	jdf_size = len(jdf)
	print('done jdf')

	accumulate = 0
	done=0
	for item in jdf:
		v1 = item[0][0]
		v2 = item[0][1]
		ce = ce_2feature(falphabet,f1,f2,v1,v2)

		a = ce*item[1]
		accumulate = accumulate +a
		done = done+1
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done/jdf_size))
		sys.stdout.flush()

	print('\n') 
	print ('====result=======')
	print((f1,f2))
	print(accumulate)
	print ('===============')

	final = ((f1,f2),accumulate)
	return final



master =[]
for i in list(range(1,11)):
	for j in list(range(i,11)):
		a = ce_test_final(i,j)
		master.append(a)

print(master)
	
'''
ce_test_final(3,1)

ce_test_final(4,1)
'''

