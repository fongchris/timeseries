
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

# ================ simple ================


def simple_return(ts):
	new_ts = []
	last_x = -999999
	for x in ts:
		if last_x == -999999:
			last_x = x
		else:
			r = (x/last_x)-1
			new_ts.append(r)
			last_x = x
	#print(new_ts)
	#print(len(new_ts))
	return new_ts


# this one is useful

def simple_return_cap(ts,cap):
	new_ts = []
	last_x = -999999
	for x in ts:
		if last_x == -999999:
			last_x = x
		else:
			r = (x/last_x)-1
			if r > cap:
				r = cap
			if r < -cap:
				r = -cap
			new_ts.append(r)
			last_x = x
	print(new_ts)
	#print(len(new_ts))
	return new_ts


#simple_return_cap(extract(0),0.10000000000)




def calculate_return_band (raw_value, max_value, min_value, k):
	increment = (max_value-min_value)/k
	if raw_value == max_value:
		band = k
	else:
		band = int((raw_value-min_value)//increment+1)
	return band


print(calculate_return_band(-0.1,0.10000000000, -0.10000000000, 100))
print(calculate_return_band(0.1,0.10000000000, -0.10000000000, 100))
print(calculate_return_band(0.098,0.10000000000, -0.10000000000, 100))
print(calculate_return_band(0.097999,0.10000000000, -0.10000000000, 100))

# ================ log ================

def log_return(ts):
	new_ts = []
	last_x = -999999
	for x in ts:
		if last_x == -999999:
			last_x = x
		else:
			r = log(x/last_x)
			new_ts.append(r)
			last_x = x
	#print(new_ts)
	#print(len(new_ts))
	return new_ts

# =======================================



def test_simple_range():

	print ('*****  Simple Return: Extreme Count *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	

	for stock_id in stock_list:
		ts1 = simple_return(extract(stock_id))
		ts_aggregated = ts_aggregated + ts1
		print('.',end="",flush=True)

	positive_list = [abs(x) for x in ts_aggregated]

	list_5 = [x for x in positive_list if x>=0.05]
	list_7_5 = [x for x in positive_list if x>=0.075]
	list_10 = [x for x in positive_list if x>=0.1]
	list_20 = [x for x in positive_list if x>=0.2]
	list_25 = [x for x in positive_list if x>=0.25]
	list_30 = [x for x in positive_list if x>=0.30]



	print ("positive list")
	print (len(positive_list))
	print (mean(positive_list))

	print ("5")
	print (len(list_5))
	print (mean(list_5))

	print ("7.5")
	print (len(list_7_5))
	print (mean(list_7_5))

	print ("10")
	print (len(list_10))
	print (mean(list_10))


	print ("20")
	print (len(list_20))
	print (mean(list_20))

	print ("25")
	print (len(list_25))
	print (mean(list_25))

	print ("30")
	print (len(list_30))
	print (mean(list_30))



#test_simple_range()
'''
====simple=== 
positive list
2938688
0.016626893551965578
5
155053
0.07954510947594312
7.5
58378
0.1120532068614438
10
26602
0.14368097412282868
20
2760
0.2645918696209104
25
1141
0.32673422349620024
30
541

====log===
positive list
2938688
0.016623092067332246
5
155067
0.07949348847848868
7.5
58158
0.11207717031233178
10
26646
0.14343872871232718
20
2733
0.26656132479152533
25
1137
0.3311731208759927
30
533
0.3985296330517088
'''

def test_log_range():

	print ('*****  Log Return: Extreme Count *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	

	for stock_id in stock_list:
		ts1 = log_return(extract(stock_id))
		ts_aggregated = ts_aggregated + ts1
		print('.',end="",flush=True)

	positive_list = [abs(x) for x in ts_aggregated]
	list_5 = [x for x in positive_list if x>=0.05]
	list_7_5 = [x for x in positive_list if x>=0.075]
	list_10 = [x for x in positive_list if x>=0.1]
	list_20 = [x for x in positive_list if x>=0.2]
	list_25 = [x for x in positive_list if x>=0.25]
	list_30 = [x for x in positive_list if x>=0.30]



	print ("positive list")
	print (len(positive_list))
	print (mean(positive_list))

	print ("5")
	print (len(list_5))
	print (mean(list_5))

	print ("7.5")
	print (len(list_7_5))
	print (mean(list_7_5))

	print ("10")
	print (len(list_10))
	print (mean(list_10))


	print ("20")
	print (len(list_20))
	print (mean(list_20))

	print ("25")
	print (len(list_25))
	print (mean(list_25))

	print ("30")
	print (len(list_30))
	print (mean(list_30))

#test_log_range()







#================== obselete


def simple_return_m (ts,factor):
	merged_ts = []
	count=0
	while (count+factor) <= len(ts)-1:
		new_point = log(ts[count+factor]/ts[count])
		merged_ts.append(new_point)
		count = count+factor
	#print(merged_ts)
	#print(len(merged_ts))
	return merged_ts 
#[1,5,20,60,120,240] [day,week,month,quater,half,year]

#simple_return(extract(0))
#simple_return_m(extract(0),240)



def log_return_m (ts,factor):
	merged_ts = []
	count=0
	while (count+factor) <= len(ts)-1:
		new_point = log(ts[count+factor]/ts[count])
		merged_ts.append(new_point)
		count = count+factor
	#print(merged_ts)
	#print(len(merged_ts))
	return merged_ts 




def find_max_min():
	start = timeit.default_timer()
	print ('*****  Local Max Min Test  *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for stock_id in stock_list:
		ts1 = log_return(extract(stock_id)) # simple or log
		ts_aggregated = ts_aggregated + ts1

	stop  = timeit.default_timer()
	print(max(ts_aggregated))
	print(min(ts_aggregated))
	print('Running Time (s): %f' %time)
#find_max_min()
# simple 1.6490066225165565 -0.7266811279826464

def zero():
	print ('*****  Zero Test  *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for stock_id in stock_list:
		ts1 = simple_return(extract(stock_id))
		ts_aggregated = ts_aggregated + ts1
	print(ts_aggregated.count(0))

#zero()
#32200



def find_global_max_min():
	print ('*****  Global Test  *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for m in [1,5,20,60,120,240]:
		for stock_id in stock_list:
			ts1 = simple_return_m(extract(stock_id),m)
			ts_aggregated = ts_aggregated + ts1
	print(max(ts_aggregated))
	print(min(ts_aggregated))

#find_global_max_min()
# 11.8113207541698
# 0.960579128


def calculate_band_return (max_value,k,raw_value):
	increment = (max_value+1)/k
	if raw_value == max_value:
		band = k
	else:
		raw_value2 = raw_value+1
		band = int(raw_value2//increment+1)
	print(band)
	return band



