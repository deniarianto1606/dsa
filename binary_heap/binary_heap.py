values = []
def insert(num):
    if len(values) == 0:
        values.append(num)
        return
    values.append(num)
    index = len(values) - 1
    parentIndex = (index-1) // 2 #(n-1)/2 to search parent
    while(parentIndex >= 0 and values[parentIndex] < values[index]): #loop until top parent index
        temp = values[index]
        values[index] = values[parentIndex]
        values[parentIndex] = temp
        index = parentIndex #swap current index to parent (new inserted value)
        parentIndex = (index-1) // 2 #search parent for current index

def extractMax():
    #swap first item with last item
    values[0] = values[len(values)-1]
    values.pop()
    index = 0
    while True:
        leftIndex = 2 * index + 1 #2*n+1
        rightIndex = 2 * index + 2 #2*n+2

        #handling outbound array
        if rightIndex >= len(values) and leftIndex >= len(values):
            break
        if rightIndex >= len(values):
            temp = values[leftIndex]
            values[leftIndex] = values[index]
            values[index] = temp
            index = leftIndex
            continue
        elif leftIndex >= len(values):
            temp = values[rightIndex]
            values[rightIndex] = values[index]
            values[index] = temp
            index = rightIndex
            continue

        #when left and right not empty
        if(values[rightIndex] > values[leftIndex] or values[leftIndex] == values[rightIndex]):
            temp = values[rightIndex]
            values[rightIndex] = values[index]
            values[index] = temp
            index = rightIndex
        else:
            temp = values[leftIndex]
            values[leftIndex] = values[index]
            values[index] = temp
            index = leftIndex

 
insert(41) 
insert(39)
insert(33)
insert(18)
insert(27)
insert(12)
# insert(55)
# insert(1)
# insert(45)
# insert(199)
extractMax()
print(values)