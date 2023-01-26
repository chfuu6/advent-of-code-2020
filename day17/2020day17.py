f = open('day17list.txt')

Pos = []
for i in range(4,-5,-1):
    for j in range(-4,5,1):
        Pos.append([j, i, 0, 0])

data = {}
temp = []
for line in f:
    for i in range(9):
        temp.append(line[i])
        
for i in range(len(Pos)):
    data[str(Pos[i])] = temp[i]


    
def center(x,y,z):
    
    return [[x-1, y+1, z+1], [x  , y+1, z+1], [x+1, y+1, z+1],
            [x-1, y+1, z  ], [x  , y+1, z  ], [x+1, y+1, z  ],
            [x-1, y+1, z-1], [x  , y+1, z-1], [x+1, y+1, z-1],
    
            [x-1, y  , z+1], [x  , y  , z+1], [x+1, y  , z+1],   
            [x-1, y  , z  ], [x  , y  , z  ], [x+1, y  , z  ],  
            [x-1, y  , z-1], [x  , y  , z-1], [x+1, y  , z-1],
    
            [x-1, y-1, z+1], [x  , y-1, z+1], [x+1, y-1, z+1],   
            [x-1, y-1, z  ], [x  , y-1, z  ], [x+1, y-1, z  ],   
            [x-1, y-1, z-1], [x  , y-1, z-1], [x+1, y-1, z-1]]  




def newCenter(x,y,z,w):
    checklist = []
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    checklist.append([x+i, y+j, z+k, w+l])
    
    checklist.remove([x,y,z,w])
    return checklist

def count(checklist, data):   
    count = 0       
    for i in range(len(checklist)):
        if str(checklist[i]) in data.keys() and data[str(checklist[i])] == '#':
            count += 1
            
    return count

     

i = 11
j = 3


for step in range(6):
    new_data = {}

    for w in range(-(j//2), (j//2) + 1, 1):
        for z in range(-(j//2), (j//2) + 1, 1):
            for y in range((i//2), -(i//2) - 1, -1):
                for x in range(-(i//2), (i//2) + 1, 1):
                    
                    
                    '''
                    checklist = center(x,y,z) 
                    '''
                    
                    checklist = newCenter(x, y, z, w)
                    num = count(checklist, data)

                    if str([x,y,z,w]) in data.keys() and data[str([x,y,z,w])] == '#':
                        if num == 2 or num == 3:
                            new_data[str([x,y,z,w])] = '#'
                            
                        else:
                            new_data[str([x,y,z,w])] = '.'
                    
                    else:
                        if num == 3:
                            new_data[str([x,y,z,w])] = '#'
                            
                        else:
                            new_data[str([x,y,z,w])] = '.'
    
                        
    data = new_data
                        
    i += 2
    j += 2

  
count = 0
for a in new_data.values():
    if a == '#':
        count += 1
        
print(count)

                     
            
