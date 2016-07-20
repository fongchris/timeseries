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



#========================= SAME AS Before ==================




def simple_return_cap(ts,max_value,min_value):
	new_ts = []
	last_x = -999999
	for x in ts:
		if last_x == -999999:
			last_x = x
		else:
			r = (x/last_x)-1
			if r > max_value:
				r = max_value
			if r < min_value:
				r = min_value
			new_ts.append(r)
			last_x = x
	#print(new_ts)
	#print(len(new_ts))
	return new_ts



def calculate_return_band (raw_value, max_value, min_value, k):
	increment = (max_value-min_value)/k
	if raw_value == max_value:
		band = k
	else:
		band = int((raw_value-min_value)//increment+1)
	return band


def convert(ts,window_size,number_of_bands,max_value,min_value):
	ts2 =[calculate_return_band(x,max_value,min_value,number_of_bands) for x in ts]
	ts3=[]
	count = 0 + window_size
	while (count <= len(ts2)):
 			x = ts2[(count-window_size):count]
 			z = tuple(x)
 			ts3.append(z)
 			count = count +1
	return ts3




def main(stock_list,window_size, number_of_bands, max_value, min_value):
	print ("\n ")

	#print ("************** START OF MAIN *******************")	
	start = timeit.default_timer()
	increment = (max_value)/(number_of_bands)
	letter_list_agg = []

	for stock_id in stock_list:
		ts = extract(stock_id)
		ts2 = simple_return_cap(ts,max_value,min_value)

		ls = convert(ts2,window_size,number_of_bands,max_value,
			min_value)
		letter_list_agg = letter_list_agg + ls
		print('.',end="",flush=True)
		
	#print(letter_list_agg)


	data_size = len(letter_list_agg)

	letter_prob = calculate_prob (letter_list_agg)

	number_of_letters = len(letter_prob)

	entropy = calculate_entropy (letter_prob)

	ordered_letter_prob = sorted(letter_prob, key=lambda tup: tup[1], reverse=True)
	#ordered_letter_prob = letter_prob.sort(key=lambda tup: tup[1], reverse=True)

	stop  = timeit.default_timer()
	time = (stop - start)
	
	print('\n')

	print ('*****  Simple Return  *****')

	print('-----------  n = %d, k = %d, Max = %d, Increment = %f -------------' % (window_size, number_of_bands, max_value, increment))
	
	print('\n')
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
	






   
	
print ('*****  Beta Return Test 1  *****')
window_size = 5 #n=3 5 7
number_of_bands = 100 # k=10 100 1000
max_value = 0.10
min_value = -0.10
stock_list = list(range(0,1168)) #1168
main(stock_list,window_size, number_of_bands, max_value,min_value)



		