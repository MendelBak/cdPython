#Fun With Functions Assignment
#Odd and Evens Loop
def odd_even_loop():
  """Return a series of numbers from 1 to 200 and whether they are odd or even."""
  for i in range(1, 200):
      if i % 2 == 0:
          print "Number is %d. Number is even, just like me!" % i
      elif i % 2 != 0:
          print "Number is %d. Number is odd." % i
odd_even_loop() #function call

#Multiply List
def multiply_list(list_input):
    """Multiply each value by 5 and return a new list with multiplied values. Takes a variable or a value as an argument."""
    new_list = []
    for i in list_input:
        new_list.append(i * 5)
    print new_list
multiply_list([3,6,8,10,67]) #function call

#Hacker Challenge
# def layered_list(arr):
#     print arr
#     new_arr = []
#     for x in arr: 
#         val_arr = []
#         for i in range(0,x):
#             val_arr.append(1)
#         new_arr.append(val_arr)
#     return new_arr
# layered_list([1,2,3,4,5]) THIS CODE IS UNFINISHED! i DON'T KNOW HOW TO DO THIS CHALLENGE

