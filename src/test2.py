import sys
import random
list = [random.randint(0,30) for i in range(0,30) ]
print list
sum = 0
for i in list:
    sum = sum + int(i)
print sum,"initial sum"

def f(list,sum,los):
    if list:
        item = list.pop(0)
        if sum+item < 30:
            sum += item
        else:
            los.append(sum)
        for i in range(0,len(list)):
            if list[i]+item < 30:
                sum += list[i]
                f(list,sum)
