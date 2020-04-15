def generating_random_number():

  # declaring the range to be between 1-100
  
	rn = set(map(str,range(1,101))).pop()	# Using sets because sets are unordered in python

	# the rn returned above is in string format
  
	rn = int(rn)							# Converting the rn in integer format

	return rn



print(generating_random_number())
