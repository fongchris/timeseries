from statistics import mean, pstdev

def sd_extreme (a,b,c,d,e):

	max_sd = 0
	val1 = 0
	val2 = 0
	val3 = 0
	val4 = 0
	val5 = 0
	for i in list(range(0,11)):#31
		for j in list(range(0,11)):
			for k in list(range(0,11)):
				for p in list(range(0,11)):
					for q in list(range(0,11)):
						val1 = a - i*0.1
						val2 = b - j*0.1
						val3 = c - k*0.1
						val4 = d - p*0.1
						val5 = e - q*0.1
				

						sd = pstdev([val1,val2,val3,val4,val5])
						if (sd>=max_sd):
							max_sd = sd
							print(max_sd)
							print(val1)
							print(val2)
							print(val3)
							print(val4)
							print(val5)

#sd_extreme(3,5,6,8,9)





def sd_extreme2 (a,b,c,d,e):

	max_sd = 1000000
	val1 = 0
	val2 = 0
	val3 = 0
	val4 = 0
	val5 = 0
	for i in list(range(0,2)):#31
		for j in list(range(0,2)):
			for k in list(range(0,2)):
				for p in list(range(0,2)):
					for q in list(range(0,2)):
						val1 = a - i*1
						val2 = b - j*1
						val3 = c - k*1
						val4 = d - p*1
						val5 = e - q*1
				

						sd = pstdev([val1,val2,val3,val4,val5])
						if (sd<=max_sd):
							max_sd = sd
							print(max_sd)
							print(val1)
							print(val2)
							print(val3)
							print(val4)
							print(val5)

#sd_extreme2(3,5,6,8,9)





def sd_extreme3 (a,b,c,d,e):

	max_sd = 0

	min_sd = 10000000
	
	for i in list(range(0,101)):#31
						val1 = a - i*0.01
						sd = pstdev([val1,b,c,d,e])
						if (sd>=max_sd):
							max_sd = sd
						if (sd<=min_sd):
							min_sd = sd
	print(max_sd)
	print(min_sd)

	print(max_sd-min_sd)


sd_extreme3(100,101,999,999,999)

