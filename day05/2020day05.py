f = open('day05list.txt')
data = []
for line in f:
    data.append(line)


ans = []

for i in range(len(data)):
    row = ''
    column = ''
    for j in range(len(data[i])):

        if data[i][j] == 'F':
            row += '0'
        
        elif data[i][j] == 'B':
            row += '1'

        elif data[i][j] == 'L':
            column += '0'
            
        elif data[i][j] == 'R':
            column += '1'
    
    ans.append(int(row,2) * 8 + int(column,2))

print(max(ans))          


ans.sort()

for i in range(min(ans),max(ans)):    
    if i not in ans:
        print(i)



    