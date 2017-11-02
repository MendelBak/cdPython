>>> words = ("It's a Thanksgiving Day. It's my birthday too!")
>>> words
"It's a Thanksgiving Day. It's my birthday too!"
>>> words.find('day')
38
>>> words.replace("day", "month")
"It's a Thanksgiving Day. It's my birthmonth too!"
>>> x = ["hello",2,54,-2,7,12,98,"world"]
>>> x
['hello', 2, 54, -2, 7, 12, 98, 'world']
>>> y = [2,54,-2,7,12,98]
>>> y
[2, 54, -2, 7, 12, 98]
>>> y.max()
>>> max(y)
98
>>> min(y)
-2
>>> print x[0]
hello
>>> print x[0, 1]
>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]
>>> x
[19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
>>> x.sort()
>>> x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> x.len()
>>> len(x)
11
>>> x1 = x[len(x)/2]
>>> x1
10
>>> x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> x1 = x[:len(x)/2]
>>> x1
[-3, -2, 2, 6, 7]
>>> x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> x2 = x[len(x)/2]
>>> x2
10
>>> x2 = x[len(x)/2:]
>>> x2
[10, 12, 19, 32, 54, 98]
>>> x2.insert(0, x1)
>>> x2
[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
>>> 