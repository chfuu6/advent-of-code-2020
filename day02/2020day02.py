a = []
b = 0

f = open('day02list.txt')
for line in f:
    a.append(line)
f.close()


for i in range(len(a)):
    num = a[i].split(' ')[0]
    num1 = int(num.split('-')[0]) - 1
    num2 = int(num.split('-')[1]) - 1
    
    lead = a[i].split(' ')[1]
    lead = lead.split(':')[0]
    
    data = a[i].split(': ')[1]
    data = list(data)
    
    if (data[num1] == lead and data[num2] != lead) or (data[num1] != lead and data[num2] == lead):
        b += 1
        
print(b)
        

 
'''
    b = data.count(lead)
    
    if b <= num2 and b >= num1:
        ans += 1
'''
        
#print(ans)
        
    
