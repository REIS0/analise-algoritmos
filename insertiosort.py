def insertionsort(array):
    for i in range(len(array)):
        value = array[i]
        j = i
        while j > 0 and value < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = value