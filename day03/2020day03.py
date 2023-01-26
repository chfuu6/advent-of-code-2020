a = []


f = open('day03list.txt')
for line in f:
    a.append(list(line))

def checkTree(right,down,a):
    
    pointer = 0
    count = 0
    
    for i in range(down,len(a),down):
        
        pointer += right
        
        if a[i][pointer % 31] == '#':
            count += 1

    return count

print(checkTree(1, 1, a)*checkTree(3, 1, a)*checkTree(5, 1, a)*checkTree(7, 1, a)*checkTree(1, 2, a))
print(61*265*82*70*34)

'''
for i in range(1,len(a)):
    
    if pointer + 3 > 30:
        pointer = pointer - 30 + 2
    else:
        pointer += 3   
    
    if a[i][pointer] == '#':
        count += 1
'''






