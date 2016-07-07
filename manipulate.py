
#exec(open("./alphabet_old.py").read())

#exec(open("./manipulate.py").read())

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


# x1<= C <= x2
# y1<=C <=y2
#http://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
def intersect (x1, x2, y1, y2):
	if x1<=y2 and y1<=x2:
		return True
	else:
		return False


def eliminate_max(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		max_band = max(i[0])
		if max_band <= v:
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)

#eliminate_max(a,5)


def loop_max(alphabet):
	letters_number_list = []
	for i in list(range(1,101)):
		new_alphabet = eliminate_max(alphabet,i)
		letters_number = len(new_alphabet)
		letters_number_list.append(letters_number)
	print (letters_number_list)



def eliminate_min(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		min_band = min(i[0])
		if min_band >= v:
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)
#eliminate_min(a,5)



def loop_min(alphabet):
	letters_number_list = []
	for i in list(range(1,101)):
		new_alphabet = eliminate_min(alphabet,i)
		letters_number = len(new_alphabet)
		letters_number_list.append(letters_number)
	print (letters_number_list)



def eliminate_mean(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		mean_max = mean(i[0])
		mean_min = mean_max-1
		if intersect(v-1,v,mean_min,mean_max):
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)



def loop_mean(alphabet):
	letters_number_list = []
	for i in list(range(1,101)):
		new_alphabet = eliminate_mean(alphabet,i)
		letters_number = len(new_alphabet)
		letters_number_list.append(letters_number)
		print('.',end="",flush=True)
	print (letters_number_list)



def eliminate_sd(alphabet,v):
	new_alphabet = []
	for i in alphabet:
		sd_min = pstdev(i[0])-0.5
		sd_max = pstdev(i[0])+0.5
		if intersect(v-1,v,sd_min,sd_max):
			new_alphabet.append(i)
	#print(new_alphabet)
	return (new_alphabet)



def loop_sd(alphabet):
	letters_number_list = []
	for i in list(range(1,101)):
		new_alphabet = eliminate_sd(alphabet,i)
		letters_number = len(new_alphabet)
		letters_number_list.append(letters_number)
		print('.',end="",flush=True)
	print (letters_number_list)

#loop_sd(a)