#Integer
x = 10
if type(x) is int:
	if x >= 100:
		print "That's a big number"
	elif x < 100:
		print "That's a teeny number"

#String
x = "Hello World"
x
'Hello World'
if type(x) is str:
	if len(x) >= 50:
		print "That's a long sentence"
	elif len(x) < 50:
		print "That's a normal length sentence"

#List
x = [1,2,3,4,5]
if type(x) is list:
	if len(x) >= 10:
		print "Large List!"
	elif len(x) < 10:
		print "Small List"