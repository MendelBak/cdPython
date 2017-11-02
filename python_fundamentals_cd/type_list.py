#Type List
def typeList(inputVar):
#This function only takes variables as an argument, not values.
	newString = ''
	sum = 0

	for value in inputVar:
		if isinstance(value, int) or isinstance(value, float):
			sum += value
		elif isinstance(value, str):
			newString += value

	if newString and sum:
		print "The input was of mixed type"
		print newString
		print sum

	elif new_string:
		print "The input was of string type"
		print new_string

	else: 
		print "The input was of number type"
		print sum