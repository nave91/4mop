import sys
import random
list = [random.randint(0,30) for i in range(0,30) ]
print list
sum = 0
for i in list:
    sum = sum + int(i)
print sum,"initial sum"

def f(list,item,los):
    if list:
        item1 = list.pop(0)
        print item1
        if item + item1 > 30: 
            if item < 30:
                los.append(item)
                print los
                f(list,item1,los)
            else:
                los.append(item1)
                print los
                f(list,item,los)
        else:
            item2 = 0
            item+=item1
            for i in range(0,len(list)):
                if list[i]+item < 30:
                    item2 = list.pop(i)
                    print item2,"item2"
                    print los
                    item+=item2
                    break
            if item2 == 0: los.append(item)
            print los
            f(list,item,los)
    else:
        print los
        isum = 0
        for i in los:
            isum = isum + i
        print isum,"final sum"
        sys.exit()


f(list,0,[])
