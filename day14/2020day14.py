f = open('day14list.txt')

mask = []
mem = []
temp = []
for line in f:
    if 'mask' in line:
        mask.append(line.split(' ')[2][:-1])
        mem.append(temp)
        temp = []
        
    else:
        temp.append(line[:-1])
        
mem.pop(0)
mask.pop(len(mask) - 1)

data = {}


for i in range(len(mask)):
    for j in range(len(mem[i])):
        
        key = mem[i][j].split('[')[1]
        key = key.split(']')[0]
        key = (36 - len(bin(int(key, 10))[2:])) * '0' + bin(int(key, 10))[2:]
        key = list(key)
    
        value = mem[i][j].split(' ')[2]
        #print(value)
        

        for x in range(len(key)):
            if mask[i][x] == 'X':
                key[x] = 'X'
                
            elif mask[i][x] == '1':
                key[x] = '1'

        
        count = 0
        for x in range(len(key)):
            if key[x] == 'X':
                count += 1
                
        pow_num = pow(2, count) 

        zeros = []
        for x in range(pow_num):
            zeros.append((count - len(bin(x)[2:])) * '0' + str(bin(x)[2:]))



        
        for x in range(len(zeros)):
            countcount = 0
            
            temp = key.copy()

            for y in range(len(temp)):
                if temp[y] == 'X':
                    temp[y] = zeros[x][countcount]
                    countcount += 1
            
            temp = ''.join(temp)
            data[temp] = value

                    
ans = 0
for values in data.values():
    ans = ans + int(values)
    
print(ans)
'''
#part1

data = {}

for i in range(len(mask)):
    for j in range(len(mem[i])):
        value = (36 - len(bin(int(mem[i][j].split(' ')[2], 10))[2:])) * '0' + bin(int(mem[i][j].split(' ')[2], 10))[2:]
        key = mem[i][j].split('[')[1]
        key = key.split(']')[0]
        
        value = list(value)
        for x in range(len(value)):
            if mask[i][x] != 'X':
                value[x] = mask[i][x]

        value = "".join(value)  
        data[key] = value
        
#print(data)
ans = 0
for values in data.values():
    ans = ans + int(values, 2)
    
print(ans)
'''




