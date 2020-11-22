def gnomesort(array):
    pos = 0
    while pos < len(array):
        if (pos == 0 or array[pos] >= array[pos-1]):
            pos += 1
        else:
            array[pos], array[pos-1] = array[pos-1], array[pos]
            pos -= 1