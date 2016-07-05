a=[((1, 1, 1), 0.9900957270078161), ((2, 2, 2), 0.006860889457773905), ((3, 3, 3), 0.0016861161796345215), ((4, 4, 4), 0.0004333587515999891), ((6, 6, 6), 0.00021889212669190338)]





def convert_main(a):
	new_list = []
	for z in a:
		if dummy_elim(z[0]) == True:
	 		new_list.append(z)
	print(new_list)







def dummy_elim (z):
	if (z == (1,1,1)):
		return False
	else:
		return True

convert_main(a)