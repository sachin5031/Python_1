def removeDuplicates(array):
    size = len(array)
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            # Updating insertIndex in our main array
            array[insertIndex] = array[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex

array_1 = [1,2,2,3,3,4]
removeDuplicates(array_1)
# 4

array_2 = [1,1,3,4,5,6,6]
removeDuplicates(array_2)
# 5