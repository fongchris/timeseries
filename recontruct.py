from statistics import mean, pstdev
import itertools
import timeit

#print(pstdev([100, 120, 140, 135, 169, 300]))

def calculate_band (raw_value, max_value, k):
	increment = max_value/k
	if raw_value == max_value:
		band = k
	else:
		band = int(raw_value//increment+1)
	return band

#print(calculate_band (19, 1000, 100))


def check_max (ts_max, max_value, k, letter):
	increment = (max_value)/(k)
	ts_max_band = int ((ts_max)//increment+1) 
	if max(letter) == ts_max_band:
		return True
	else:	
		return False

#print (check_max (70, 1000, 100, (1,2,8)))




def check_min (ts_min, max_value, k, letter):
	increment = (max_value)/(k)
	ts_min_band = int ((ts_min)//increment+1) 
	if min(letter) == ts_min_band:
		return True
	else:	
		return False

#print (check_min (9, 1000, 100, (1,2,8)))



# average something in that band = average something in average? 
# average something higher and average something lower?

def band_to_limits (band,max_value, k):
	increment = (max_value)/(k) 
	return ((band-1)*increment,band*increment-0.00000000000001)

#print (band_to_limits (1,1000, 100))
	
def check_mean (mean_input, max_value, k, letter):
	

	extreme_list = [] 
	for i in list(range(0,len(letter))):
		extreme = band_to_limits (letter [i], max_value, k)
		extreme_list.append(extreme)
	
	#print (extreme_list)
	combination_list = [list(i) for i in itertools.product([0, 1], repeat=len(letter))]
	#print (combination_list)
	actual_combination_list = []
	for combination in combination_list:
		 lst = [a[b] for a,b in zip(extreme_list,combination)]
		 actual_combination_list.append(lst)
	#print(actual_combination_list)

	mean_list = [mean(i) for i in actual_combination_list]

	#print(mean_list)

	if max(mean_list)>=mean_input and min(mean_list)<=mean_input:
		#print('true')
		return True
	else:
		#print('false')
		return False 

#check_mean (20,1000,100,(3,4,2))


def generate3(N):
	list1 = []
	for i in list(range(1,N+1)):
		for j in list(range(1,N+1)):
			for k in list(range(1,N+1)):
				list1.append((i,j,k))
	return list1
#print (generate3(100))




def check_std (std_input, max_value, k, letter):
	

	extreme_list = [] 
	for i in list(range(0,len(letter))):
		extreme = band_to_limits (letter [i], max_value, k)
		extreme_list.append(extreme)
	
	#print (extreme_list)
	combination_list = [list(i) for i in itertools.product([0, 1], repeat=len(letter))]
	#print (combination_list)
	actual_combination_list = []
	for combination in combination_list:
		 lst = [a[b] for a,b in zip(extreme_list,combination)]
		 actual_combination_list.append(lst)
	#print(actual_combination_list)

	std_list = [pstdev(i) for i in actual_combination_list]
	#print(std_list)
	if max(std_list)>=std_input and min(std_list)<=std_input:
		#print('true')
		return True
	else:
		#print('false')
		return False 


#============== testing ========





def test_mean(mean_input):
	start = timeit.default_timer()
	max_value = 1000
	k = 100
	mean_band = calculate_band (mean_input, max_value, k)

	print('Mean Value: %f' %mean_input)
	print('Mean Band: %d' %mean_band)

	letter_list = generate3(100)
	qualified_list = []
	for i in letter_list:
		a = check_mean (mean_input,max_value,k,i)
		if a == True:
			qualified_list.append(i)
	stop  = timeit.default_timer()
	time = (stop - start)/60
	
	print('Running Time: %f' %time)
	print('Number of qualified letters: %d' %len(qualified_list))
	print(qualified_list)


#test_mean(15) 
#test_mean(25)
#test_mean(50) 
#test_mean(75)





def test_std(std_input):
	
	start = timeit.default_timer()

	max_value = 1000
	k = 100

	std_band = calculate_band (std_input, max_value, k)

	print('S.D. Value: %f' %std_input)
	print('S.D. in terms of band distiance: %d' %std_band)

	letter_list = generate3(100)
	qualified_list = []
	for i in letter_list:
		a = check_std (std_input,max_value,k,i)
		if a == True:
			qualified_list.append(i)


	stop  = timeit.default_timer()
	time = (stop - start)/60
	
	print('Running Time: %f' %time)
	print('Number of qualified letters: %d' %len(qualified_list))
	print(qualified_list)
	
#test_std(5)
#test_std(15)
#test_std(35)
#test_std(75)


def test_mean_std(mean_input,std_input):
	
	start = timeit.default_timer()

	max_value = 1000
	k = 100

	mean_band = calculate_band (mean_input, max_value, k)


	std_band = calculate_band (std_input, max_value, k)
	print('Mean Value: %f' %mean_input)
	print('S.D. Value: %f' %std_input)
	print('Mean Band: %d' %mean_band)
	print('S.D. in terms of band distiance: %d' %std_band)

	max_value = 1000
	k = 100

	letter_list = generate3(100)
	qualified_list = []
	for i in letter_list:
		a = check_mean (mean_input,max_value,k,i)
		b = check_std (std_input,max_value,k,i)
		if a == True and b == True:
			qualified_list.append(i)

	stop  = timeit.default_timer()
	time = (stop - start)/60
	
	print('Running Time: %f' %time)
	print('Number of qualified letters: %d' %len(qualified_list))
	print(qualified_list)


#test_mean_std(40,5)
#test_mean_std(40,10)
#test_mean_std(40,25)





