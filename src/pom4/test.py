import random

list = [random.randint(0,30) for i in range(0,30)]


print list
out = [list.pop(0)]
print out,list

print 30 - (int)(sum(out))
sumi = sum(out)
iter = 0
outing = []
while sumi < 30:
    breakit = False
    for i,j in enumerate(list):
        if (30 - ((int)(sum(out))+j)) >= 0:
            out.append(j)
            list.pop(i)
            break
        elif i == len(list)-1:
            breakit = True
    sumi = sum(out)
    if breakit:
        break
    print out,list,outing
    print len(out),len(list)
print outing        
        
