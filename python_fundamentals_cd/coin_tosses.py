from random import random
sum_head = 0
sum_tail = 0
for i in range(1, 5001):
    result = random() >= 0.5 
    if result == True:
        result = "Heads"
        sum_head += 1
    else:
        result = "Tails"
        sum_tail += 1
    print "Attempt #{}: Tossing a coin.. You tossed {}!... You've gotten {} {} so far and {} {} so far".format(i, result, sum_head, result, sum_tail, result)
print "I'm ending the program now. Thanks for playing!"