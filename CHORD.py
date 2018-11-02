import random

bCheck = False
nCheck = False

## input b value; this determines what value is added to the node values
## when the maximum node value is exceeded

while bCheck == False:
    b = int(input("B value: "))
    if 5 <= b <= 10:
        bCheck = True
    else:
        print("B value must be between 5 and 10. Please enter another value.")

## input number of nodes

while nCheck == False:
    
    n = int(input("Number of nodes: "))
    if 5 <= n <= 15:
        nCheck = True
    else:
        print("Number of nodes must be between 5 and 15. Please enter another value.")

## limit is the value added to the node values when the maximum node value
## is exceeded

limit = 2 ** b

nodes = random.sample(range(0, limit), n)

nodes = sorted(nodes, key=int)

print(" ")
print("Nodes: ", nodes, "\n")

fingerTables = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for i in range(len(nodes)):
    for j in range(b):
        entry = nodes[i] + 2**j
        
        if i == 0:
            fingerTables[i].append(entry)
        elif i == 1:
            fingerTables[i].append(entry)
        elif i == 2:
            fingerTables[i].append(entry)
        elif i == 3:
            fingerTables[i].append(entry)
        elif i == 4:
            fingerTables[i].append(entry)
        elif i == 5:
            fingerTables[i].append(entry)
        elif i == 6:
            fingerTables[i].append(entry)
        elif i == 7:
            fingerTables[i].append(entry)
        elif i == 8:
            fingerTables[i].append(entry)
        elif i == 9:
            fingerTables[i].append(entry)
        elif i == 10:
            fingerTables[i].append(entry)
        elif i == 11:
            fingerTables[i].append(entry)
        elif i == 12:
            fingerTables[i].append(entry)
        elif i == 13:
            fingerTables[i].append(entry)
        elif i == 14:
            fingerTables[i].append(entry)

kWorks = False
k = random.randint(0,limit)

while(not kWorks):
    for table in fingerTables:
        #print(table)
        for number in table:
            if k == number:
                kWorks = True
                break
        if(not kWorks):
            k = random.randint(0,limit)

## Starting node

nStart = nodes[1]
print("\nStarting Node: ", nStart)
print("Key ID: ", k)

currentNode = nStart
currentFT = fingerTables[1]
visits = []
visitsFT = []
found = False

#search for the k value
while(not found):
    visits.append(currentNode)
    visitsFT.append(currentFT)
    #for loop searches the finger table of current node for k
    tempk = k
    closestFtValue = None
    closestNode = None
    for value in currentFT:
        if value == tempk:
            found = True
            break
        elif value < k+limit:
            closestFtValue = value
    #k value was not in current node's fingertable
    if closestFtValue == None:
        tempk += limit
        for value in currentFT:
            if value == k+limit:
                found = True
                break
            elif value < k+limit:
                closestFtValue = value
        #closestFtValue found
        for node in nodes:
            if node >= closestFtValue:
                currentNode = node
                currentFT = fingerTables[nodes.index(currentNode)]
                break
            else:
                if node+limit >= closestFtValue:
                    currentNode = node
                    currentFT = fingerTables[nodes.index(currentNode)]
                    break
    else:
        
        foundNewNode = False
        for node in nodes:
            if node >= closestFtValue:
                currentNode = node
                currentFT = fingerTables[nodes.index(currentNode)]
                foundNewNode = True
                break
        while(not foundNewNode):
            for node in nodes:
                if node+limit >= closestFtValue:
                    currentNode = node
                    currentFT = fingerTables[nodes.index(currentNode)]
                    foundNewNode = True
                    break
                
visits.append(currentNode)
visitsFT.append(currentFT)


print(" ")
print("Visited Nodes: ", visits)
print("Finger Tables: ", visitsFT)
