'''
a = []
ans = 2020

f = open('day01list.txt')
for line in f:
    a.append(int(line))
f.close()



for i in range(len(a)):
    #print(a[i])
    for j in range(len(a)):
        for k in range(len(a)):
            if ans == a[i] + a[j] + a[k]:
                print(a[i] * a[j] * a[k])
'''
a = []
space = {}

f = open('day01list.txt')
for line in f:
    a.append(int(line))
f.close()

for i in range(len(a)):
    if (2020 - a[i]) in space:
        print(a[i] * (2020 - a[i]))
    else:
        space[a[i]] = True
    

