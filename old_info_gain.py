
#exec(open("./data_alphabet.py").read())

#exec(open("./main_info_gain.py").read())

from statistics import mean, pstdev
from math import log
import time
import csv
import timeit

#exec(open("./naive1.py")
def check_prob(a):
	prob_sum = 0 
	for i in a:
		prob_sum = prob_sum + i[1]
	print (prob_sum)
#OK 


def calculate_entropy (letter_prob):
	prob_list=[x[1] for x in letter_prob]
	#print(prob_list)
	#print(sum(prob_list))
	entropy = 0
	for p in prob_list:
		entropy = entropy - p*log(p,2)
	return entropy


def rebalance (alphabet):
	prob_sum = 0
	new_alphabet =[]
	for i in alphabet:
		prob_sum = prob_sum+i[1]

	for i in alphabet:
		a = (i[0],i[1]/prob_sum)
		new_alphabet.append(a)
	#print(prob_sum)
	#print(new_alphabet)
	return new_alphabet




# x1<= C <= x2
# y1<=C <=y2
#http://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
def intersect (x1, x2, y1, y2):
	if x1<=y2 and y1<=x2:
		return True
	else:
		return False


def eliminate_high(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		max_band = max(i[0])
		if max_band == v:
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)

#eliminate_max(a,5)


def eliminate_low(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		min_band = min(i[0])
		if min_band == v:
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)
#eliminate_min(a,5)


def eliminate_open(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		min_band = i[0][0]
		if min_band == v:
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)


def eliminate_close(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		min_band = i[0][4]
		if min_band == v:
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)


# ==================== maximum ============


def loop_simple(alphabet):
	count = 0
	#letters_number_list = []
	entropy_list = []
	probability_reduction_list = []
	for i in list(range(1,101)):
		new_alphabet = eliminate_close(alphabet,i)
		#letters_number = len(new_alphabet)
		#letters_number_list.append(letters_number)

		probability_reduction = sum([i[1] for i in new_alphabet])

		probability_reduction_list.append (probability_reduction)
		balanced_alphabet = rebalance(new_alphabet) 
		entropy = calculate_entropy(balanced_alphabet)
		entropy_list.append(entropy)
		count = count+1
		print(count/100)
		
	#print (letters_number_list)
	print (entropy_list)
	print (probability_reduction_list)


# ========================== minimum ===================







def loop_min2(alphabet):
	count = 0
	letters_number_list = []
	entropy_list = []
	for i in list(range(1,101)):
		new_alphabet = eliminate_min(alphabet,i)
		letters_number = len(new_alphabet)
		letters_number_list.append(letters_number)

		balanced_alphabet = rebalance(new_alphabet) 
		entropy = calculate_entropy(balanced_alphabet)
		entropy_list.append(entropy)
		count = count+1
		print(count/100)

	print (letters_number_list)
	print (entropy_list)








def eliminate_mean(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		mean_max = mean(i[0])
		mean_min = mean_max-1
		if intersect(v*0.5-0.5,v*0.5,mean_min,mean_max):
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)


def loop_mean2(alphabet):
	count = 0
	letters_number_list = []
	entropy_list = []
	for i in list(range(1,201)):
		new_alphabet = eliminate_mean(alphabet,i)
		letters_number = len(new_alphabet)
		letters_number_list.append(letters_number)

		balanced_alphabet = rebalance(new_alphabet) 
		entropy = calculate_entropy(balanced_alphabet)
		entropy_list.append(entropy)
		count = count+1
		print(count/100)

	print (letters_number_list)
	print (entropy_list)



def eliminate_sd(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		sd_min = pstdev(i[0])-0.5
		sd_max = pstdev(i[0])+0.5
		#if intersect(v-1,v,sd_min,sd_max):
		if intersect(v*0.5-0.5,v*0.5,sd_min,sd_max):
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)


def loop_sd2(alphabet):
	print("========= sd test ==========")
	start = timeit.default_timer()
	count = 0
	letters_number_list = []
	entropy_list = []
	for i in list(range(1,101)):
		new_alphabet = eliminate_sd(alphabet,i)
		letters_number = len(new_alphabet)
		letters_number_list.append(letters_number)

		balanced_alphabet = rebalance(new_alphabet) 
		entropy = calculate_entropy(balanced_alphabet)
		entropy_list.append(entropy)
		count = count+1
		print(count)

	stop  = timeit.default_timer()
	time = (stop - start)
	print (letters_number_list)
	print (entropy_list)
	print("========= sd test ==========")
	print('Running Time (s): %f' %time)




#=================== doubles ==============================



def loop_min_max(alphabet):
	print("========== min max test==========")
	count = 0
	letters_number_list = []
	entropy_list = []

	for i in list(range(1,101)): # this i min
		alphabet1 = eliminate_min(alphabet,i)
		for j in list(range(1,101)): # this is max
			alphabet2 = eliminate_max(alphabet1,j)

			letters_number = len(alphabet2)
			letters_number_list.append((i,j,letters_number))

			balanced_alphabet = rebalance(alphabet2) 
			entropy = calculate_entropy(balanced_alphabet)
			entropy_list.append((i,j,entropy))

			count = count+1
			print(count)
	print("========== min max test==========")
	print (letters_number_list)
	print (entropy_list)


#loop_min_max(a)



def loop_sd_mean(alphabet):
	print("======== sd-mean test===========")
	start = timeit.default_timer()
	count = 0
	letters_number_list = []
	entropy_list = []

	for i in list(range(1,101)): # this is  sd 
		alphabet1 = eliminate_sd(alphabet,i)
		for j in list(range(1,101)): # this is mean
			alphabet2 = eliminate_mean(alphabet1,j)
			letters_number = len(alphabet2)
			letters_number_list.append((i,j,letters_number))

			balanced_alphabet = rebalance(alphabet2) 
			entropy = calculate_entropy(balanced_alphabet)
			entropy_list.append((i,j,entropy))

			count = count+1
			print(count)


	stop  = timeit.default_timer()
	time = (stop - start)
	print (letters_number_list)
	print (entropy_list)
	print("======== sd-mean test===========")
	print('Running Time (s): %f' %time)










