f = open('day11list.txt')

matrix = []
for line in f:
    temp = []
    for i in range(len(line) - 1):
        temp.append(line[i])
        
    matrix.append(temp)
    
matrix[len(matrix)-1].append('L')
#print(matrix)
#print('...')

#--------part1----------
def step1(matrix):
    new_data = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):  
    
            if matrix[i][j] == 'L' and i == 0 and j != 0 and j != len(matrix[i]) - 1:
                flag = True
                if matrix[i][j-1] != 'L' and matrix[i][j-1] != '.':
                    flag = False
                if matrix[i][j+1] != 'L' and matrix[i][j+1] != '.':
                    flag = False
                if matrix[i+1][j] != 'L' and matrix[i+1][j] != '.':
                    flag = False
                if matrix[i+1][j-1] != 'L' and matrix[i+1][j-1] != '.':
                    flag = False
                if matrix[i+1][j+1] != 'L' and matrix[i+1][j+1] != '.':
                    flag = False
                
                if flag == True:
                    temp.append('#')
                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == 'L' and i == 0 and j == 0:
                flag = True
                if matrix[i][j+1] != 'L' and matrix[i][j+1] != '.':
                    flag = False
                if matrix[i+1][j] != 'L' and matrix[i+1][j] != '.':
                    flag = False
                if matrix[i+1][j+1] != 'L' and matrix[i+1][j+1] != '.':
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i == 0 and j == len(matrix[i]) - 1:
                flag = True
                if matrix[i][j-1] != 'L' and matrix[i][j-1] != '.':
                    flag = False
                if matrix[i+1][j] != 'L' and matrix[i+1][j] != '.':
                    flag = False
                if matrix[i+1][j-1] != 'L' and matrix[i+1][j-1] != '.':
                    flag = False
                    
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i != 0 and j != 0 and i != len(matrix) - 1 and j != len(matrix[i]) - 1:
                flag = True
                if matrix[i][j-1] != 'L' and matrix[i][j-1] != '.':
                    flag = False
                if matrix[i][j+1] != 'L' and matrix[i][j+1] != '.':
                    flag = False
                if matrix[i+1][j] != 'L' and matrix[i+1][j] != '.':
                    flag = False
                if matrix[i+1][j-1] != 'L' and matrix[i+1][j-1] != '.':
                    flag = False
                if matrix[i+1][j+1] != 'L' and matrix[i+1][j+1] != '.':
                    flag = False
                if matrix[i-1][j] != 'L' and matrix[i-1][j] != '.':
                    flag = False
                if matrix[i-1][j-1] != 'L' and matrix[i-1][j-1] != '.':
                    flag = False
                if matrix[i-1][j+1] != 'L' and matrix[i-1][j+1] != '.':
                    flag = False
                
                if flag == True:
                    temp.append('#')
                
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i != 0 and j == 0 and i != len(matrix) - 1:
                flag = True
                if matrix[i][j+1] != 'L' and matrix[i][j+1] != '.':
                    flag = False
                if matrix[i+1][j] != 'L' and matrix[i+1][j] != '.':
                    flag = False
                if matrix[i-1][j] != 'L' and matrix[i-1][j] != '.':
                    flag = False
                if matrix[i+1][j+1] != 'L' and matrix[i+1][j+1] != '.':
                    flag = False
                if matrix[i-1][j+1] != 'L' and matrix[i-1][j+1] != '.':
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
    
            if matrix[i][j] == 'L' and i != 0 and j == len(matrix[i]) - 1 and i != len(matrix) - 1:
                flag = True
                if matrix[i][j-1] != 'L' and matrix[i][j-1] != '.':
                    flag = False
                if matrix[i+1][j] != 'L' and matrix[i+1][j] != '.':
                    flag = False
                if matrix[i-1][j] != 'L' and matrix[i-1][j] != '.':
                    flag = False
                if matrix[i+1][j-1] != 'L' and matrix[i+1][j-1] != '.':
                    flag = False
                if matrix[i-1][j-1] != 'L' and matrix[i-1][j-1] != '.':
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i == len(matrix) - 1 and j != 0 and j != len(matrix[i]) - 1:
                flag = True
                if matrix[i][j-1] != 'L' and matrix[i][j-1] != '.':
                    flag = False
                if matrix[i][j+1] != 'L' and matrix[i][j+1] != '.':
                    flag = False
                if matrix[i-1][j] != 'L' and matrix[i-1][j] != '.':
                    flag = False
                if matrix[i-1][j-1] != 'L' and matrix[i-1][j-1] != '.':
                    flag = False
                if matrix[i-1][j+1] != 'L' and matrix[i-1][j+1] != '.':
                    flag = False
                
                if flag == True:
                    temp.append('#')
                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == 'L' and i == len(matrix) - 1 and j == 0:
                flag = True
                if matrix[i][j+1] != 'L' and matrix[i][j+1] != '.':
                    flag = False
                if matrix[i-1][j] != 'L' and matrix[i-1][j] != '.':
                    flag = False
                if matrix[i-1][j+1] != 'L' and matrix[i-1][j+1] != '.':
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                flag = True
                if matrix[i][j-1] != 'L' and matrix[i][j-1] != '.':
                    flag = False
                if matrix[i-1][j] != 'L' and matrix[i-1][j] != '.':
                    flag = False
                if matrix[i-1][j-1] != 'L' and matrix[i-1][j-1] != '.':
                    flag = False
                    
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                                        
            if matrix[i][j] == '.':
                temp.append(matrix[i][j])
                
            if matrix[i][j] == '#':
                temp.append(matrix[i][j])
                           
        new_data.append(temp)
    
    return new_data

def step2(matrix):
    
    new_data = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):  

            if matrix[i][j] == '#' and i == 0 and j != 0 and j != len(matrix[i]) - 1:
                count = 0
                if matrix[i][j-1] == '#':
                    count += 1
                if matrix[i][j+1] == '#':
                    count += 1
                if matrix[i+1][j] == '#':
                    count += 1
                if matrix[i+1][j-1] == '#':
                    count += 1
                if matrix[i+1][j+1] == '#':
                    count += 1
                
                if count >= 4:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == '#' and i == 0 and j == 0:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i == 0 and j == len(matrix[i]) - 1:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i != 0 and j != 0 and i != len(matrix) - 1 and j != len(matrix[i]) - 1:
                count = 0
                if matrix[i][j-1] == '#':
                    count += 1
                if matrix[i][j+1] == '#':
                    count += 1
                if matrix[i+1][j] == '#':
                    count += 1
                if matrix[i+1][j-1] == '#':
                    count += 1
                if matrix[i+1][j+1] == '#':
                    count += 1
                if matrix[i-1][j] == '#':
                    count += 1
                if matrix[i-1][j-1] == '#':
                    count += 1
                if matrix[i-1][j+1] == '#':
                    count += 1
                
                if count >= 4:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i != 0 and j == 0 and i != len(matrix) - 1:
                count = 0
                if matrix[i][j+1] == '#':
                    count += 1
                if matrix[i+1][j] == '#':
                    count += 1
                if matrix[i-1][j] == '#':
                    count += 1
                if matrix[i+1][j+1] == '#':
                    count += 1
                if matrix[i-1][j+1] == '#':
                    count += 1
                
                if count >= 4:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
    
            if matrix[i][j] == '#' and i != 0 and j == len(matrix[i]) - 1 and i != len(matrix) - 1:
                count = 0
                if matrix[i][j-1] == '#':
                    count += 1
                if matrix[i+1][j] == '#':
                    count += 1
                if matrix[i-1][j] == '#':
                    count += 1
                if matrix[i+1][j-1] == '#':
                    count += 1
                if matrix[i-1][j-1] == '#':
                    count += 1
                
                if count >= 4:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i == len(matrix) - 1 and j != 0 and j != len(matrix[i]) - 1:
                count = 0
                if matrix[i][j-1] == '#':
                    count += 1
                if matrix[i][j+1] == '#':
                    count += 1
                if matrix[i-1][j] == '#':
                    count += 1
                if matrix[i-1][j-1] == '#':
                    count += 1
                if matrix[i-1][j+1] == '#':
                    count += 1
                
                if count >= 4:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == '#' and i == len(matrix) - 1 and j == 0:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '.':
                temp.append(matrix[i][j])
                
            if matrix[i][j] == 'L':
                temp.append(matrix[i][j])
                           
                           
        new_data.append(temp)
    
    return new_data
#--------part2-----------

def up(matrix,i,j):
    flag = True
    while flag == True:

        i -= 1
        if matrix[i][j] == '#':
            flag == False
            return True
        
        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif i == 0:
            flag == False
            return False
            
def down(matrix,i,j):
    flag = True
    while flag == True:
        
        i += 1
        if matrix[i][j] == '#':
            flag == False
            return True
        
        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif i == len(matrix) - 1:
            flag == False
            return False
        
def left(matrix,i,j):
    flag = True
    while flag == True:
        
        j -= 1
        if matrix[i][j] == '#':
            flag == False
            return True

        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif j == 0:
            flag == False
            return False

def right(matrix,i,j):
    flag = True
    while flag == True:
        
        j += 1
        if matrix[i][j] == '#':
            flag == False
            return True
        
        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif j == len(matrix[i]) - 1:
            flag == False
            return False
        
def upRight(matrix,i,j):
    flag = True
    while flag == True:
        
        j += 1
        i -= 1
        
        if matrix[i][j] == '#':
            flag == False
            return True
        
        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif j == len(matrix[i]) - 1 or i == 0:
            flag == False
            return False
        
def upLeft(matrix,i,j):
    flag = True
    while flag == True:
        
        j -= 1
        i -= 1
        
        if matrix[i][j] == '#':
            flag == False
            return True
        
        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif j == 0 or i == 0:
            flag == False
            return False
        
def downLeft(matrix,i,j):
    flag = True
    while flag == True:
        
        j -= 1
        i += 1
        
        if matrix[i][j] == '#':
            flag == False
            return True
        
        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif j == 0 or i == len(matrix) - 1:
            flag == False
            return False

def downRight(matrix,i,j):
    flag = True
    while flag == True:
        
        j += 1
        i += 1
        
        if matrix[i][j] == '#':
            flag == False
            return True
        
        elif matrix[i][j] == 'L':
            flag == False
            return False
        
        elif j == len(matrix[i]) - 1 or i == len(matrix) - 1:
            flag == False
            return False

def part2step1(matrix):
    new_data = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):  
    
            if matrix[i][j] == 'L' and i == 0 and j != 0 and j != len(matrix[i]) - 1:
                flag = True
                if down(matrix, i, j):
                    flag = False
                if left(matrix, i, j):
                    flag = False
                if right(matrix, i, j):
                    flag = False
                if downLeft(matrix, i, j):
                    flag = False
                if downRight(matrix, i, j):
                    flag = False
                
                if flag == True:
                    temp.append('#')
                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == 'L' and i == 0 and j == 0:
                flag = True
                if down(matrix, i, j):
                    flag = False
                if right(matrix, i, j):
                    flag = False
                if downRight(matrix, i, j):
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i == 0 and j == len(matrix[i]) - 1:
                flag = True
                if down(matrix, i, j):
                    flag = False
                if left(matrix, i, j):
                    flag = False
                if downLeft(matrix, i, j):
                    flag = False
                    
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i != 0 and j != 0 and i != len(matrix) - 1 and j != len(matrix[i]) - 1:
                flag = True
                if up(matrix, i, j):
                    flag = False
                if down(matrix, i, j):
                    flag = False
                if left(matrix, i, j):
                    flag = False
                if right(matrix, i, j):
                    flag = False
                if upRight(matrix, i, j):
                    flag = False
                if upLeft(matrix, i, j):
                    flag = False
                if downLeft(matrix, i, j):
                    flag = False
                if downRight(matrix, i, j):
                    flag = False
                
                if flag == True:
                    temp.append('#')
                
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i != 0 and j == 0 and i != len(matrix) - 1:
                flag = True
                if up(matrix, i, j):
                    flag = False
                if down(matrix, i, j):
                    flag = False
                if right(matrix, i, j):
                    flag = False
                if upRight(matrix, i, j):
                    flag = False
                if downRight(matrix, i, j):
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
    
            if matrix[i][j] == 'L' and i != 0 and j == len(matrix[i]) - 1 and i != len(matrix) - 1:
                flag = True
                if up(matrix, i, j):
                    flag = False
                if down(matrix, i, j):
                    flag = False
                if left(matrix, i, j):
                    flag = False
                if upLeft(matrix, i, j):
                    flag = False
                if downLeft(matrix, i, j):
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i == len(matrix) - 1 and j != 0 and j != len(matrix[i]) - 1:
                flag = True
                if up(matrix, i, j):
                    flag = False
                if left(matrix, i, j):
                    flag = False
                if right(matrix, i, j):
                    flag = False
                if upLeft(matrix, i, j):
                    flag = False
                if upRight(matrix, i, j):
                    flag = False
                
                if flag == True:
                    temp.append('#')
                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == 'L' and i == len(matrix) - 1 and j == 0:
                flag = True
                if up(matrix, i, j):
                    flag = False
                if right(matrix, i, j):
                    flag = False
                if upRight(matrix, i, j):
                    flag = False
                
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == 'L' and i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                flag = True
                if up(matrix, i, j):
                    flag = False
                if left(matrix, i, j):
                    flag = False
                if upLeft(matrix, i, j):
                    flag = False
                    
                if flag == True:
                    temp.append('#')
                else:
                    temp.append(matrix[i][j])
                                        
            if matrix[i][j] == '.':
                temp.append(matrix[i][j])
                
            if matrix[i][j] == '#':
                temp.append(matrix[i][j])
                           
        new_data.append(temp)
    
    return new_data

def part2step2(matrix):
    
    new_data = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):  

            if matrix[i][j] == '#' and i == 0 and j != 0 and j != len(matrix[i]) - 1:
                count = 0
                if down(matrix, i, j):
                    count += 1
                if left(matrix, i, j):
                    count += 1
                if right(matrix, i, j):
                    count += 1
                if downLeft(matrix, i, j):
                    count += 1
                if downRight(matrix, i, j):
                    count += 1
                
                if count >= 5:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == '#' and i == 0 and j == 0:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i == 0 and j == len(matrix[i]) - 1:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i != 0 and j != 0 and i != len(matrix) - 1 and j != len(matrix[i]) - 1:
                count = 0
                if up(matrix, i, j):
                    count += 1
                if down(matrix, i, j):
                    count += 1
                if left(matrix, i, j):
                    count += 1
                if right(matrix, i, j):
                    count += 1
                if upRight(matrix, i, j):
                    count += 1
                if upLeft(matrix, i, j):
                    count += 1
                if downLeft(matrix, i, j):
                    count += 1
                if downRight(matrix, i, j):
                    count += 1
                    
                if count >= 5:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i != 0 and j == 0 and i != len(matrix) - 1:
                count = 0
                if up(matrix, i, j):
                    count += 1
                if down(matrix, i, j):
                    count += 1
                if right(matrix, i, j):
                    count += 1
                if upRight(matrix, i, j):
                    count += 1
                if downRight(matrix, i, j):
                    count += 1
                
                if count >= 5:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
    
            if matrix[i][j] == '#' and i != 0 and j == len(matrix[i]) - 1 and i != len(matrix) - 1:
                count = 0
                if up(matrix, i, j):
                    count += 1
                if down(matrix, i, j):
                    count += 1
                if left(matrix, i, j):
                    count += 1
                if upLeft(matrix, i, j):
                    count += 1
                if downLeft(matrix, i, j):
                    count += 1
                
                if count >= 5:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i == len(matrix) - 1 and j != 0 and j != len(matrix[i]) - 1:
                count = 0
                if up(matrix, i, j):
                    count += 1
                if left(matrix, i, j):
                    count += 1
                if right(matrix, i, j):
                    count += 1
                if upLeft(matrix, i, j):
                    count += 1
                if upRight(matrix, i, j):
                    count += 1
                
                if count >= 5:
                    temp.append('L')                
                else:
                    temp.append(matrix[i][j])
                    
    
            if matrix[i][j] == '#' and i == len(matrix) - 1 and j == 0:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '#' and i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                temp.append(matrix[i][j])
                    
            if matrix[i][j] == '.':
                temp.append(matrix[i][j])
                
            if matrix[i][j] == 'L':
                temp.append(matrix[i][j])
                           
                           
        new_data.append(temp)
    
    return new_data
#-------------------------


flag = True
temp = []
ans = matrix
while flag == True:
    
    ans = step1(ans)
    if ans == temp:
        #print(ans)
        flag = False
    else:
        temp = ans
        
        ans = step2(ans)
        if ans == temp:
            #print(ans)
            flag = False
        else:
            temp = ans

finalAns = 0            
for i in range(len(ans)):
    for j in range(len(ans[i])):
        if '#' == ans[i][j]:
            finalAns += 1
            
print(finalAns)




    
    