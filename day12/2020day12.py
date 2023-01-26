f = open('day12list.txt')

direction = []
distant = []
for line in f:
    direction.append(line[:1])
    distant.append(int(line[1:]))

vertical = 1
level = 10

x = 0
y = 0
rotate = 'E'

for i in range(len(direction)):
    
    if direction[i] == 'N':
        vertical += distant[i]
        
    elif direction[i] == 'S':
        vertical -= distant[i]
        
    elif direction[i] == 'W':
        level -= distant[i]
        
    elif direction[i] == 'E':
        level += distant[i]
        
    elif direction[i] == 'F':
        
        x += distant[i] * level
        y += distant[i] * vertical
        
        '''
        if rotate == 'N':
            vertical += distant[i]
            
        elif rotate == 'S':
            vertical -= distant[i]
            
        elif rotate == 'W':
            level -= distant[i]
            
        elif rotate == 'E':
            level += distant[i]
        '''
            
    elif direction[i] == 'L':
        
        
        if distant[i] // 90 == 1:
            
            temp = level
            level = -vertical
            vertical = temp

            
            '''
            if rotate == 'E':
                rotate = 'N'
            elif rotate == 'N':
                rotate = 'W'
            elif rotate == 'W':
                rotate = 'S'
            elif rotate == 'S':
                rotate = 'E'
            '''
        
        elif distant[i] // 90 == 2:
            
            vertical = -vertical
            level = -level
            
            '''
            if rotate == 'E':
                rotate = 'W'
            elif rotate == 'N':
                rotate = 'S'
            elif rotate == 'W':
                rotate = 'E'
            elif rotate == 'S':
                rotate = 'N'
            '''
                
        elif distant[i] // 90 == 3:
            
            temp = level
            level = vertical
            vertical = -temp
            
            '''
            if rotate == 'E':
                rotate = 'S'
            elif rotate == 'N':
                rotate = 'E'
            elif rotate == 'W':
                rotate = 'N'
            elif rotate == 'S':
                rotate = 'W'
            '''
            
    elif direction[i] == 'R':
            
        if distant[i] // 90 == 1:
            
            temp = level
            level = vertical
            vertical = -temp
           
            '''
            if rotate == 'E':
                rotate = 'S'
            elif rotate == 'S':
                rotate = 'W'
            elif rotate == 'W':
                rotate = 'N'
            elif rotate == 'N':
                rotate = 'E'
            '''
        
        elif distant[i] // 90 == 2:
            
            vertical = -vertical
            level = -level
            
            '''
            if rotate == 'E':
                rotate = 'W'
            elif rotate == 'N':
                rotate = 'S'
            elif rotate == 'W':
                rotate = 'E'
            elif rotate == 'S':
                rotate = 'N'
            '''
                
        elif distant[i] // 90 == 3:
            
            temp = level
            level = -vertical
            vertical = temp
            
            '''
            if rotate == 'E':
                rotate = 'N'
            elif rotate == 'N':
                rotate = 'W'
            elif rotate == 'W':
                rotate = 'S'
            elif rotate == 'S':
                rotate = 'E'
            '''
            

print(abs(x) + abs(y))
            
            
            
            
            
            