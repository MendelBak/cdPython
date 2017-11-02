#Compare Lists
def compareLists(list1, list2):
  '''Compare two lists when given two arguments. Arguments must be variables, not lists.'''
  if cmp(list1, list2) == 0:
  	print "The lists are identical"
  else:
  	print "The lists are not identical"
compareLists([1,2,3,4,5], [1,2,3,4,5]) #premade arguments. Please change these to use the function