
#import matplotlib.pyplot as plt

from statistics import mean
from math import log
import time
import csv
import timeit

# function 1 "extract" extracts the raw time series from the ticker
def extract(number):
	ts = []
	with open('csvsp1500.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			ts.append(row[number])
	del ts[0]
	ts=list(map(float, ts))
	return ts

# function 2 "convert" converts a time serie to "tuples" of bands number
def convert(ts,window_size,number_of_bands,max_value):

	increment = (max_value)/(number_of_bands)
	ts2 = [int ((x)//increment+1) for  x in ts]

	ts3=[]
	count = 0 + window_size
	while (count <= len(ts2)):
 			x = ts2[(count-window_size):count]
 			z = tuple(x)
 			ts3.append(z)
 			count = count +1
	return ts3

# function 3 
def calculate_prob (ts,prob_threshold):
	ul = [(x,round(ts.count(x)/len(ts),100)) for x in set(ts)]
	ul.sort()
	#fl = [tup for tup in ul if (tup[1]>prob_threshold)]
	#fl.sort()
	return ul

# function 4 
def calculate_entropy (letter_prob):
	prob_list=[x[1] for x in letter_prob]
	#print(prob_list)
	#print(sum(prob_list))

	entropy = 0
	for p in prob_list:
		entropy = entropy - p*log(p,2)
	return entropy

# function 5
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

# main function 
def main(stock_list,window_size, number_of_bands, max_value, probability_threshold):
	print ("\n ")
	#print ("************** START OF MAIN *******************")
	
	start_overall = timeit.default_timer()

	ts_aggregated = []

	start_convert = timeit.default_timer()
	for stock_id in stock_list:
		ts1 = extract(stock_id)
		ts2 = convert(ts1,window_size,number_of_bands,max_value)
		#print ("Stock ID: %d" % stock_id)
		#print (ts1)
		#print ("Letters and Probabilities:" )
		#print (calculate_prob2(ts2,probability_threshold))
		ts_aggregated = ts_aggregated + ts2
		#print('.',end="",flush=True)
	stop_convert  = timeit.default_timer()

	#print ('done aggregation\n ')

	start_prob = timeit.default_timer()
	letter_prob = calculate_prob (ts_aggregated,probability_threshold)
	stop_prob = timeit.default_timer()

	start_entropy = timeit.default_timer()
	entropy = calculate_entropy (letter_prob)
	stop_entropy = timeit.default_timer()

	stop_overall  = timeit.default_timer()


	time_overall = stop_overall - start_overall
	time_convert = stop_convert - start_convert
	time_prob = stop_prob - start_prob
	time_entropy = stop_entropy - start_entropy
	

	print ("=============== result ================")
	print('Input 1 - Window Size n = %d, Number of Bands k = %d' % (window_size, number_of_bands))
	#print('Input 2 -: ' )
	#print('Input 3 - Max: %d' %max_value)
	#print('Increment: %d' %increment)
	#print('Probability Threshold: %d' %probability_threshold)
	print('\n')
	#print ("Letters and Probabilities:")
	#print(letter_prob)
	
	print('Time (Overall:) %f' %time_overall)
	print('Time (Converting TS): %f' %time_convert)
	print('Time (Letter Probability): %f' %time_prob)
	print('Time (Entropy): %f' %time_entropy)
	print ("Entropy: %f" %entropy) 
	#print ("***************** END OF MAIN ******************")
	

#========= Parameters =============================
#k^n
#n window_size = 4 #n=3
#k number_of_bands = 100 # k=100
#max_value = 2000
#probability_threshold = 0
#increment = (max_value)/(number_of_bands)
#stock_list = list(range(0,1428)) #481 #378 #569 #1428
#============================================================

#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def test1():
	print ("***************************** TEST 1 (Fix K = 100) ********************************")
	max_value = 2000
	probability_threshold = 0
	number_of_bands = 100 
	stock_list = list(range(0,1428))    
	for window_size in [5,10,15,20,25,30,35,40]:
		main(stock_list,window_size, number_of_bands, max_value, probability_threshold)
#test1()

#[500,1000,1500,2000,2500,3000]

def test2():
	print ("****************************** TEST 2 (Fix n = 5)  ********************************")
	max_value = 2000
	probability_threshold = 0
	window_size = 5
	stock_list = list(range(0,1428))    
	for number_of_bands in [100,250,500,1000,1500,2000,2500,3000,3500]:
		main(stock_list,window_size, number_of_bands, max_value, probability_threshold)

#test2()


def test_threshold():
	max_value = 2000
	probability_threshold = 0
	number_of_bands = 500
	window_size = 3
	stock_list = list(range(0,1428))
	main(stock_list,window_size, number_of_bands, max_value, 0.001)
	main(stock_list,window_size, number_of_bands, max_value, 0)

#test_threshold()

def test_basic():
	print(convert(extract(1),5,1000,2000))

#test_basic()


def test_merge():
	ts = extract(1)
	ts2 = merge(ts,120) #5, 20, 60, 120, 240
	ts3 = convert(ts2,5,1000,2000)
	letter_prob = calculate_prob (ts3,0)
	entropy = calculate_entropy (letter_prob)
	print (ts2)
	print (ts3)
	print (letter_prob)
	print (entropy)



def main2(stock_list,window_size, number_of_bands, max_value, probability_threshold,factor):
	print ("\n ")
	#print ("************** START OF MAIN *******************")
	
	start_overall = timeit.default_timer()

	ts_aggregated = []

	for stock_id in stock_list:
		ts1 = extract(stock_id)
		ts_m = merge(ts1,factor)
		ts2 = convert(ts_m,window_size,number_of_bands,max_value)
		ts_aggregated = ts_aggregated + ts2
		print('.',end="",flush=True)

	letter_prob = calculate_prob (ts_aggregated,probability_threshold)
	entropy = calculate_entropy (letter_prob)

	print ("=============== result ================")
	print('Inputs - Window Size n = %d, Number of Bands k = %d, Max =%d' % (window_size, number_of_bands,max_value))
	#print('Input 2 -: ' )
	#print('Input 3 - Max: %d' %max_value)
	#print('Increment: %d' %increment)
	#print('Probability Threshold: %d' %probability_threshold)
	print ("Entropy: %f" %entropy) 

	filtered_lp = [tup for tup in letter_prob if (tup[1]>probability_threshold)]
	filtered_lp.sort()

	print ("Letters and Probabilities:")
	print(filtered_lp)

	
	#print ("***************** END OF MAIN ******************")


def test_resolution():
	max_value = 2000
	probability_threshold = 0
	number_of_bands = 500
	window_size = 5
	stock_list = list(range(0,1428))
	for factor in [1,5, 20, 60, 120, 240]:
		print('\n')
		print('--------------- merging factor %d ----------' %factor)
		main2(stock_list,window_size, number_of_bands, max_value, probability_threshold,factor)

test_resolution()

