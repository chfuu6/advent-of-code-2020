f = open('day10list.txt')

data = []
for line in f:
    data.append(int(line))
    

pointer = 0
count = []
new_data = []

while pointer != max(data):
    new_data.append(pointer)
    for i in range(1,4):

        pointer += 1
        if pointer in data:
            count.append(i)
            break
        
#print(new_data)
count.append(3)

howmany = []
temp = 1
for i in range(len(count)):

    if count[i] == 1:
        temp += 1
    
    else:
        howmany.append(temp)
        temp = 1
        
print(howmany)
ans = 1

for i in range(len(howmany)):
    if howmany[i] == 5:
        ans = ans * 7
        
    elif howmany[i] == 4:
        ans = ans * 4
        
    elif howmany[i] == 3:
        ans = ans * 2

print(ans)


'''
one = 0
second = 0
third = 0

for i in range(len(count)):
    if count[i] == 1:
        one += 1
        
    elif count[i] == 2:
        second += 1
        
    else:
        third += 1
        
print(one * (third + 1))  
'''     
