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

	


def run_ce():

	master_ce_list = []
	with open('./data/falphabet2.pickle', 'rb') as handle:
  		falphabet = pickle.load(handle)

	for i in list(range(1,11)):
		print('feature %d:' %i)
		ce_list = conditional_entropy_list(falphabet,i)
		master_ce_list.append(ce_list)
		print(ce_list)

	with open('./data/master_ce2.pickle', 'wb') as handle:
  		pickle.dump(master_ce_list, handle)


#run_ce()




def feature_pdf(falphabet,f):
	prob_list = []
	done = 0
	for i in list(range(1,51)):
		prob = 0
		for item in falphabet:
			if item[f] == i:
				prob = prob + item[0]
		prob_list.append(prob)
		done = done +1
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done/100))
		sys.stdout.flush()

	print ('\n')
	print ("==== Feature: %d PDF =======" %f) 
	#print (prob_list)
	return prob_list






def run_pdf():
	master_pdf=[]
	with open('./data/falphabet2.pickle', 'rb') as handle:
  		falphabet = pickle.load(handle)

	for i in list(range(1,11)):
		a=feature_pdf(falphabet,i)
		master_pdf.append(a)
		print(a)

	with open('./data/master_pdf2.pickle', 'wb') as handle:
  		pickle.dump(master_pdf, handle)


def dot(list1,list2):
	result = sum([i*j for (i, j) in zip(list1, list2)])
	return result


def run_final():
	with open('./data/master_ce2.pickle', 'rb') as handle:
  		master_ce = pickle.load(handle)

	with open('./data/master_pdf2.pickle', 'rb') as handle2:
		master_pdf = pickle.load(handle2)

	for i in list(range(0,10)):
		a=dot(master_ce[i],master_pdf[i])
		print(a)

run_final()

#feature_jpdf(falphabet,1,2)



#run_falphabet()
#run_single_pdf()
#run_jpdf()
