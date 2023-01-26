f = open('day09list.txt')

data = []
numToPlus = []
'''
i = 0
for line in f:
    i += 1

    if i > 25:
        data.append(int(line))
    else:
        numToPlus.append(int(line))
'''

for line in f:
    data.append(int(line))

'''

check = 0
for i in range(len(data)):
    space = {}
    for j in range(len(numToPlus)):

        
        if data[i] - numToPlus[j] in space:
            numToPlus.append(data[i])
            numToPlus.remove(numToPlus[0])

            break
        else:
            space[numToPlus[j]] = True
           
        
    if len(space) == 25:
        print(data[i])
        break
'''

            
ans = 15353384
#ans = 277
flag = False

while flag == False:
    key = 0
    anslist = []
    for i in range(len(data)):
        key = key + data[i]
        if key > ans:
            data.remove(data[0])
            break
        
        elif key == ans:
            print('success')
            flag = True
            break
        
        else:
            anslist.append(data[i])
    
            
print(max(anslist) + min(anslist))














