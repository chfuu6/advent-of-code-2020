f = open('day16list.txt')

temp = []
data = []
for line in f:
    temp.append(line[:-1])
    if line == '\n':
        data.append(temp)
        temp = []
        
for i in range(len(data)):
    data[i].pop(len(data[i]) - 1)

info = {}
INFO = [] 

part2INFO = []   
for i in range(len(data[0])):
    temp = []
    num = len(data[0][i].split(' ')) - 1
    temp.append(data[0][i].split(' ')[num - 2])
    temp.append(data[0][i].split(' ')[num])
    
    part2INFO.append(temp)
    INFO.append(data[0][i].split(' ')[num - 2])
    INFO.append(data[0][i].split(' ')[num])

    
for i in range(len(part2INFO)):
    temp = []
    temp.append(int(part2INFO[i][0].split('-')[0]))
    temp.append(int(part2INFO[i][0].split('-')[1]))
    temp.append(int(part2INFO[i][1].split('-')[0]))
    temp.append(int(part2INFO[i][1].split('-')[1]))
    info[data[0][i].split(':')[0]] = temp
    
#print(info)
#print(INFO)

data[2].pop(0)

num_data = []
for i in range(len(data[2])):
    for j in range(len(data[2][i].split(','))):       
        num_data.append(data[2][i].split(',')[j])


ansans = 0
ans = {}
for i in range(len(num_data)):
    num = int(num_data[i])
    flag = False
    
    for j in range(len(INFO)):  
        if num >= int(INFO[j].split('-')[0]) and num <= int(INFO[j].split('-')[1]):
            flag = True
            
    if flag == False:
        ans[num] = True
        ansans += num

#print(ansans)
#print(ans)

tickets = []
test = 0
for i in range(len(data[2])):
    flag = True
    for j in range(20):
        if int(data[2][i].split(',')[j]) in ans.keys():
            flag = False
        
    if flag == True:
        tickets.append(data[2][i])
        

new_tickets = []        
for i in range(len(tickets)):
    temp = []
    for j in range(len(tickets[i].split(','))):       
        temp.append(int(tickets[i].split(',')[j]))
    new_tickets.append(temp)
    
#print(new_tickets)
xxx = [179,101,223,107,127,211,191,61,199,193,181,131,89,109,197,59,227,53,103,97] 
new_tickets.append(xxx)
#new_tickets.append(['11','12','13'])
#print(part2INFO)

INFO = []
for i in range(len(part2INFO)):
    temp = []
    temp.append(int(part2INFO[i][0].split('-')[0]))
    temp.append(int(part2INFO[i][0].split('-')[1]))
    temp.append(int(part2INFO[i][1].split('-')[0]))
    temp.append(int(part2INFO[i][1].split('-')[1]))
    INFO.append(temp)

def finalAns(INFO):
    for i in range(20):
        count = 0
        for x in range(len(INFO)):
            flag = True
            #print(INFO[x])
            
            for j in range(len(new_tickets)):
                num = new_tickets[j][i]
                #print(num)
                if (num < INFO[x][0]) or ((num > INFO[x][1]) and num < INFO[x][2]) or (num > INFO[x][3]):
                    flag = False
      
    
            if flag == True:
                keynum = x
                count += 1
                
        if count == 1:      
            #print(i, INFO[keynum])
            FINALANS[str(INFO[keynum])] = i
            INFO.remove(INFO[keynum])
            break

FINALANS = {}

for i in range(20):
    finalAns(INFO)
    
ans = 1
for key in info.keys():
    if 'departure' in key:
        ans = ans * xxx[FINALANS[str(info[key])]]
        
print(ans)
    







      
        