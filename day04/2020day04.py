import re

f = open('day04list.txt')
w = f.readlines()

data = []
temp = ''
for i in range(len(w)):
    temp = temp + w[i][:-1] + ' '
    if w[i] == '\n':
        data.append(temp)
        temp = ''

new_data = []
fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']

for i in range(len(data)):
    checkdata = 0
    for j in range(len(fields)):
        if fields[j] in data[i]:
            checkdata += 1
    
    if checkdata == 7:
        new_data.append(data[i])

            
values = []    
for i in range(len(new_data)):
    values.append((new_data[i].split(' ')))

ans = 0
for i in range(len(values)):
    checkvalues = 0
    for j in range(len(values[i]) - 2):
        field = values[i][j].split(':')[0]
        #print(field)
        
        
        if field == 'byr':
            if int(values[i][j].split(':')[1]) >= 1920 and int(values[i][j].split(':')[1]) <= 2002:
                #print(int(values[i][j].split(':')[1]))
                checkvalues += 1
        
        elif field == 'iyr':
            if int(values[i][j].split(':')[1]) >= 2010 and int(values[i][j].split(':')[1]) <= 2020:
                #print(int(values[i][j].split(':')[1]))
                checkvalues += 1
        
        elif field == 'eyr':
            if int(values[i][j].split(':')[1]) >= 2020 and int(values[i][j].split(':')[1]) <= 2030:
                #print(int(values[i][j].split(':')[1]))
                checkvalues += 1            
        
        elif field == 'hgt':
            if values[i][j].split(':')[1][-2:] == 'cm':
                if int(values[i][j].split(':')[1][:-2]) >= 150 and int(values[i][j].split(':')[1][:-2]) <= 193:
                    checkvalues += 1
                    
            elif values[i][j].split(':')[1][-2:] == 'in':
                if int(values[i][j].split(':')[1][:-2]) >= 59 and int(values[i][j].split(':')[1][:-2]) <= 76:
                    checkvalues += 1
        
        
        elif field == 'hcl':
            str = values[i][j].split(':')[1]
            key = re.search('^#{1}[0-9a-f]{6}$', str)
            if key:
                checkvalues += 1


        elif field == 'ecl':
            ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            for x in range(len(ecl)):
                if values[i][j].split(':')[1] == ecl[x]:
                    checkvalues += 1
        
                    
        elif field == 'pid':
            if len(values[i][j].split(':')[1]) == 9:
                checkvalues += 1
    
    if checkvalues == 7:
        ans += 1
                
                
print(ans)
        

        

        
        
