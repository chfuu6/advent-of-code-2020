f = open('day13list.txt')

data = f.read()
data = data.split(',')

new_data = []
for i in range(len(data)):
    if data[i] != 'x':
        temp = []
        temp.append(13)
        temp.append(i)
        temp.append(int(data[i]))
        new_data.append(temp)
        
new_data.pop(0)
print(new_data)

def check(new_data1, new_data2):

    if new_data1[0] > new_data2[0]:
        i = new_data1[0] 
        while True:           
            if (i - new_data2[0]) % new_data2[1] == 0:
                #print(i)
                return i
                break
            else:
                i += new_data1[1]
            
    else:
        i = new_data2[0]  
        while True:          
            if (i - new_data1[0]) % new_data1[1] == 0:
                #print(i)
                return i
                break
            else:
                i += new_data2[1]
  
def lcm(x, y):
 
   #  获取最大的数
   if x > y:
       greater = x
   else:
       greater = y
 
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
 
   return lcm

a = []

for i in range(0,len(new_data),2):
    x = 0
    temp = []
    while True:
        if ((new_data[i][0] * x) + new_data[i][1]) % new_data[i][2] == 0 and ((new_data[i+1][0] * x) + new_data[i+1][1]) % new_data[i+1][2] == 0:
            #print(x)
            temp.append(x)
            temp.append(lcm(new_data[i][2], new_data[i+1][2]))
            a.append(temp)
            break
        else:
            x += 1

print(a)



b = []
for i in range(0,len(a),2):
    temp = []
    temp.append(check(a[i], a[i+1]))
    temp.append(lcm(a[i][1], a[i+1][1]))
    b.append(temp)
    
print(b)

a = check(b[0], b[1])
print(a * 13)



'''
data = []
for line in f:
    for i in range (len(line.split(','))):
        if line.split(',')[i] != 'x':
            data.append(int(line.split(',')[i]))
           

time = 1000390
ans = 1000
for i in range(len(data)):
    
    if (data[i] * ((time // data[i]) + 1)) - time < ans:
        ans = (data[i] * ((time // data[i]) + 1)) - time
        print(data[i])
print(ans)
'''