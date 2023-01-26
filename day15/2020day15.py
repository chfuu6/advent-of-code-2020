data = [14,8,16,0,1,17]
num = (30000000-6)

space = {14:0, 8:1, 16:2, 0:3, 1:4}
pointer = 5
for i in range(num):

    if data[len(data) - 1] in space:
        data.append((len(data) - 1) - space[data[len(data) - 1]])
        space[data[len(data) - 2]] = pointer
        
    else:
        space[data[len(data) - 1]] = pointer
        data.append(0)
        
    pointer += 1
        
print(data[len(data) - 1])


        
