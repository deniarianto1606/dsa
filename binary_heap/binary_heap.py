values = []
def insert(num):
    if len(values) == 0:
        values.append(num)
        return
    values.append(num)
    index = len(values) - 1
    parentIndex = (index-1) // 2
    while(parentIndex >= 0 and values[parentIndex] < values[index]): #loop until top parent index
        temp = values[index]
        values[index] = values[parentIndex]
        values[parentIndex] = temp
        index = parentIndex #swap current index to parent (new inserted value)
        parentIndex = (index-1) // 2 #search parent for current index
 
insert(41) 
insert(39)
insert(33)
insert(18)
insert(27)
insert(12)
insert(55)
insert(1)
insert(45)
insert(199)
print(values)