f = open('day08list.txt')

data = []
numdata = []
for line in f:
    data.append(line.split(' ')[0])
    numdata.append(line.split(' ')[1][:-1])

#print(len(data))
#print(data)
#print(numdata)

def findCount(data):
    ans = 0
    i = 0
    check = []
    while True:     
        
        check.append(i)
        #print(check)
        if data[i] == 'acc':
            
            if numdata[i][0] == '+':
                #print(numdata[i][1:])
                ans = ans + int(numdata[i][1:])
                
            elif numdata[i][0] == '-':
                #print(numdata[i][1:])
                ans = ans - int(numdata[i][1:])
            
            i = i + 1
                
        elif data[i] == 'jmp':
            
            if numdata[i][0] == '+':
                #print(numdata[i][1:])
                i = i + int(numdata[i][1:])
    
                
            elif numdata[i][0] == '-':
                #print(numdata[i][1:])
                i = i - int(numdata[i][1:])
    
                
        elif data[i] == 'nop':
               
            i = i + 1

        if i == len(data) - 1:
            print(ans)
            return i
            break
        
        if i in check:
            check.append(i)
            return i
            break


i = 0
while i >= 0:
    #print(i)
    if data[i] == 'nop':
        data[i] = 'jmp'
        
        #print(data)
        
        if findCount(data) != len(data) - 1:
            data[i] = 'nop'
            
        else:
            break

            
    elif data[i] == 'jmp':
        data[i] = 'nop'
        
        #print(data)

        if findCount(data) != len(data) - 1:
            data[i] = 'jmp'   
            
        else:
            break
        
    i += 1
