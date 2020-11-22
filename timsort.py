def timsort(array):
    MIN_RUN = 32
    lenght = len(array)
    for i in range(0, lenght, MIN_RUN):
        end = min((i+MIN_RUN)-1, lenght-1)
        alt_insort(array, i, end)
    current_size = MIN_RUN
    while current_size < lenght:
        for i in range(0, lenght, current_size*2):
            mid = min(lenght-1, (i+current_size)-1)
            end = min(lenght-1, mid+current_size)
            merge(array, i, end, mid)
        current_size *= 2
    
def merge(array, start, end, mid):
    if mid==end:
        return 
    first_part = array[start:mid+1]
    second_part = array[mid+1:end+1]
    len_first = (mid - start)+1
    len_second = end - mid
    ind_first = 0
    ind_second = 0
    ind = start
    
    while ind_first < len_first and ind_second < len_second:
        if first_part[ind_first] < second_part[ind_second]:
            array[ind] = first_part[ind_first]
            ind_first += 1
        else:
            array[ind] = second_part[ind_second]
            ind_second += 1
        ind += 1
    
    while ind_first < len_first:
        array[ind] = first_part[ind_first]
        ind_first += 1
        ind += 1
    
    while ind_second < len_second:
        array[ind] = second_part[ind_second]
        ind_second += 1
        ind += 1
        
def alt_insort(array, f_part, s_part):
    for i in range(f_part+1, s_part+1):
        j = i
        while j > f_part and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1