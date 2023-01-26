'''
f = open('day06list.txt')
w = f.readlines()

temp = ''
data = []
for i in range(len(w)):
    temp = temp + w[i][:-1]
    if w[i] == '\n':
        data.append(temp)
        temp = ''



ans = 0
for i in range(len(data)):
    count = 1
    for j in range(len(data[i]) - 1):
        
        if sorted(data[i])[j] != sorted(data[i])[j + 1]:
            count += 1
        
    
    ans = ans + count

print(ans)
'''
f = open('day06list.txt')
w = f.readlines()

temp = ''
data = []
times = []
count = 0
for i in range(len(w)):
    temp = temp + w[i][:-1] + ' '
    count += 1
    
    if w[i] == '\n':
        data.append(temp)
        times.append(count - 1)
        count = 0
        temp = ''
        

ans = 0
for i in range(len(data)):
    
    setdata = []
    
    temp = ''
    for j in range(times[i]):
        temp = temp + data[i].split(' ')[j]
        
    
    if times[i] == 1:
        #print(len(data[i]) - 2)
        ans = ans + len(data[i]) - 2
        
        
    if times[i] > 1:
        
        count1 = 0
        for x in range(len(temp)):
            count = 0
            
            for y in range(len(temp)):
                if temp[x] == temp[y]:
                    count += 1
                    
            if count == times[i]:
                count1 += 1
        
        #print(count1//times[i])
        ans = ans + (count1//times[i])

print(ans)

    
    
    





