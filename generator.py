def generate_5_100 ():
	alphabet =[]
	prob = 1/(100**5)
	for i in list(range(0,101)):#31
		for j in list(range(0,101)):
			for k in list(range(0,101)):
				for p in list(range(0,101)):
					for q in list(range(0,101)):
						a=((i,j,k,p,q),prob)
						alphabet.append(a)
						print('.',end="",flush=True)
	print(alphabet)

generate_5_100 ()

