#you know what final testin
#from lab
#testing 123
#import matplotlib.pyplot as plt

from statistics import mean
from math import log
import time
import csv
import timeit





def extract(number):
	ts = []
	with open('1500comma.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			ts.append(row[number])
	del ts[0]
	ts=list(map(float, ts))
	return ts




def calculate_band (raw_value, max_value, k):
	increment = max_value/k
	if raw_value == max_value:
		band = k
	else:
		band = int(raw_value//increment+1)
	return band



def find_data_size():
	lst = []
	for i in list(range(0,1168)):
		ts = extract(i)
		lst.append(len(ts))
	print('number of stocks')
	print(lst)
	print('number of data point')
	print(len(lst))

#find_data_size()
# 1168*2517****

def find_max_min():
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for stock_id in stock_list:
		ts1 = extract(stock_id)
		ts_aggregated = ts_aggregated + ts1
	print(max(ts_aggregated))
	print(min(ts_aggregated))
#find_max_min()
#1799.23  new 1469.56

def convert(ts,window_size,number_of_bands,max_value):

	#increment = (max_value)/(number_of_bands)
	#ts2 = [int ((x)//increment+1) for  x in ts]
	ts2 =[calculate_band(x,max_value,number_of_bands) for x in ts]
	ts3=[]
	count = 0 + window_size
	while (count <= len(ts2)):
 			x = ts2[(count-window_size):count]
 			z = tuple(x)
 			ts3.append(z)
 			count = count +1
	return ts3

def calculate_prob (ts):
	ul = [(x,(ts.count(x)/len(ts))) for x in set(ts)]
	ul.sort()
	#fl = [tup for tup in ul if (tup[1]>prob_threshold)]
	#fl.sort()
	return ul

def calculate_entropy (letter_prob):
	prob_list=[x[1] for x in letter_prob]
	#print(prob_list)
	#print(sum(prob_list))

	entropy = 0
	for p in prob_list:
		entropy = entropy - p*log(p,2)
	return entropy

def merge (ts,factor):
	merged_ts = []
	count=0
	while (count+factor-1) <= len(ts)-1:
		new_point = mean(ts[count:(count+factor)])
		merged_ts.append(new_point)
		count = count+factor
	#print(merged_ts)
	return merged_ts 
#merge ([1,2,3,4,5,6],6)


def normalise(ts):
	ts_max = max(ts)
	ts_min = min(ts)
	ts_normalised = []
	for a in ts:
		if a==ts_max:
			b = 100
			ts_normalised.append(b)
		else:
			b = 100*(a-ts_min)/(ts_max-ts_min)
			ts_normalised.append(b)
	return ts_normalised




#ts = extract(0)
#print (normalise (ts))


# main function 
def main(stock_list,window_size, number_of_bands, max_value, norm, merge_factor):
	print ("\n ")
	#print ("************** START OF MAIN *******************")
	
	start = timeit.default_timer()

	increment = (max_value)/(number_of_bands)
	letter_list_agg = []

	for stock_id in stock_list:
		ts = extract(stock_id)
		
		if norm != 0:
			ts=normalise(ts)

		#if merge_factor != 0:
		#	ts=merge(ts,merge_factor)

		ls = convert(ts,window_size,number_of_bands,max_value)
		#print ("Stock ID: %d" % stock_id)
		#print (ts)
		#print ("Letters and Probabilities:" )
		#print (calculate_prob2(ts2,probability_threshold))
		letter_list_agg = letter_list_agg + ls
		print('.',end="",flush=True)


	#print (letter_list_agg)
	data_size = len(letter_list_agg)

	letter_prob = calculate_prob (letter_list_agg)

	number_of_letters = len(letter_prob)

	entropy = calculate_entropy (letter_prob)

	ordered_letter_prob = sorted(letter_prob, key=lambda tup: tup[1], reverse=True)
	#ordered_letter_prob = letter_prob.sort(key=lambda tup: tup[1], reverse=True)

	stop  = timeit.default_timer()
	time = (stop - start)
	
	print('\n')
	if norm != 0:
		print ('*****  The data is normalised  *****')

	if merge_factor != 0:
		print ('*****  Merging factor: %d  *****' %merge_factor)

	print('-----------  n = %d, k = %d, Max = %d, Increment = %f -------------' % (window_size, number_of_bands, max_value, increment))
	#print('Increment: %d' %increment)
	#print('Probability Threshold: %d' %probability_threshold)
	print('\n')
	#print ("Letters and Probabilities:")
	#print(letter_prob)
	#print(ordered_letter_prob)
	print('Running Time (s): %f' %time)
	print ("Entropy: %f" %entropy) 
	print('Number of Letters: %d' %(int(number_of_bands**window_size)))
	print ('Number of Possible Letters : %d' %number_of_letters)
	print ('Sample size: %d' %data_size)
	#print ("***************** END OF MAIN ******************")
	print('Top 5:')
	print(ordered_letter_prob[0:5])
	print('Alphabet:')
	print(letter_prob)

#========= test =============================
#k^n

def test1():
	print ('*****  Test 1  *****')
	for n in [7]: #n=3 5 7
		for k in [1000]: # k=10 100 1000
			window_size = n #n=3 5 7
			number_of_bands = k # k=10 100 1000
			max_value = 1500
			stock_list = list(range(0,1168)) #481 #378 #569 #1428
			main(stock_list,window_size, number_of_bands, max_value,0,0)

#test1()
#============================================================
def test2():
	print ('*****  Test 2  *****')
	for n in [3]: #n=3 5 7
		for k in [10]: # k=10 100 1000
			window_size = n #n=3 5 7
			number_of_bands = k # k=10 100 1000
			max_value = 1001
			stock_list = list(range(0,10)) #1168
			main(stock_list,window_size, number_of_bands, max_value,1,0)

#test2()


def test3():
	print ('*****  Test 3  *****')
	for m in [20, 60, 120, 240]:  # [0,5,20,60,120,240]
			window_size = 5 #n=3 5 7
			number_of_bands = 100 # k=10 100 1000
			max_value = 2000
			stock_list = list(range(0,1168)) #481 #378 #569 #1428
			main(stock_list,window_size, number_of_bands, max_value,0,m)



#============== NOW RUNNING ================

# this is for normalise 5*100
def test4():
	print ('*****  Test 4  *****')
	for n in [5]: #n=3 5 7
		for k in [10]: # k=10 100 1000
			window_size = n #n=3 5 7
			number_of_bands = k # k=10 100 1000
			max_value = 100
			stock_list = list(range(0,1168)) #1168
			main(stock_list,window_size, number_of_bands, max_value,1,0)


test4()


def test_normalise_band():
	agg_ts =[]
	stock_list = list(range(0,1168)) #1168
	for i in stock_list:
		ts = normalise(extract(i))
		ts2 =[calculate_band(x,100,100) for x in ts]
		agg_ts=agg_ts+ts2
		print('.',end="",flush=True)

	print(agg_ts)
	print(len(agg_ts))
	print(max(agg_ts))
	print(min(agg_ts))

#ok
