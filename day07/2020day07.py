f = open('day07list.txt')
temp = []
temp1 = []
for line in f:
    temp.append(line[:-2].split('contain')[0])
    temp1.append(line[:-2].split('contain')[1])
    
    
data1 = []
for i in range(len(temp)):
    #data[temp[i].split(' bags')[0]] = False
    data1.append(temp[i].split(' bags')[0])
    

info = []
for i in range(len(temp1)):
    info.append(temp1[i].split(','))


data = {}
for i in range(len(data1)):
    data[data1[i]] = info[i]


def findColor(color, data, howmany):
    #print('input ' + color)
    temp = {}
    count = 0
    num = 0
    flag = False
    
    for i in range(len(data[color])):
        newcolor = data[color][i].split(' ')[2] + ' ' + data[color][i].split(' ')[3]

        if 'other' not in newcolor:
            temp[newcolor] = data[color][i].split(' ')[1]
            #print(temp)
            num = findColor(newcolor, data, int(data[color][i].split(' ')[1]))
            
        else:
            flag = True
            
        count = count + num
        
    if flag == True:
        return howmany
    
    else:
        return count * howmany + howmany

            

temp = {}
final_ans = 0
# for i in range(len(data['shiny gold'])):
#     color = data['shiny gold'][i].split(' ')[2] + ' ' + data['shiny gold'][i].split(' ')[3]
#     temp[color] = data['shiny gold'][i].split(' ')[1]
#     numnum = int(data['shiny gold'][i].split(' ')[1])
#     #print(temp)
#     ans = findColor(color, data, numnum)
#     final_ans = final_ans + ans
    
#print(final_ans)
print(findColor('shiny gold', data, 1) - 1)
    





'''
data2 = []
for i in range(len(info)):
    for j in range(len(info[i])):
         if 'shiny gold bag' in info[i][j]:
             print(info[i])
             print(data1[i])
             data2.append(data1[i])
             data[data1[i]] = True


flag = False
while flag == False:
    flag1 = True
    for i in range(len(info)):
        for j in range(len(info[i])):
            for k in range(len(data2)):
                
                if data2[k] in info[i][j]:
                    
                    if data1[i] not in data2:
                        data2.append(data1[i])
                        print(info[i])
                        print(data1[i])
                        data[data1[i]] = True   
                        flag1 = False
                        
    if flag1 == True:
                flag = True


    
ans = 0                
for i in data.values():
    if i == True:
        ans += 1
        
print(ans)

'''
