'''
i have a list
a = [1, 2, 3, 5, 2]

i need to group these list elements to where they are in groups that their sum `<= 5`

ie; this would produce
myNewList = [[1,2,2], [3], [5]]
'''
import scipy as sp 
a = [int(round(i * 5)) for i in sp.rand(30).tolist()]
#a = [1, 1, 4, 2, 3, 5, 2, 4, 3, 2, 1]
#a = [1, 1, 4, 2, 3, 5, 2]
#a = [1, 5, 2, 3]

a = sorted(a, reverse=True)
target = 5 #"target val"

res = []
temp = []
i = 0
while 1: #len(a) > 0:
    #curr item too large or at target: add it in its own list
    if a[i] >= target: 
        res.append([a[i]])
        a.__delitem__(i)
        i=0

    #over target: check further down in list
    elif(sum(temp + [a[i]] ) > target):
        i += 1

    #at target: move from temp to result list    
    elif(sum(temp + [a[i]] ) == target):
        res.append(temp + [a[i]])
        temp = []
        a.__delitem__(i)
        i=0

    #under target: move from big to temp list
    else:#(sum(temp + a[i]) < target):
        temp += [a[i]]
        a.__delitem__(i)
        i=0

    if len(a) == 0: 
        res.append(temp)
        break

    #reached the end of list: move temp to result. reset index
    if i == len(a): 
        res.append(temp)
        temp = []
        i = 0

print res
