'''
i have a list
a = [1, 2, 3, 5, 2]

i need to group these list elements to where they are in groups that their sum `<= 5`

ie; this would produce
myNewList = [[1,2,2], [3], [5]]
'''
a = [1, 1, 2, 3, 5, 2]

a = sorted(a, reverse=True)
target = 5 #"target val"

result = []
f=lambda x: x<=target
t = []
for i in a:
    if f(sum(t+[i])): t += [i]
    else: 
        result.append(t)
        t = [i]
result.append(t
print result
