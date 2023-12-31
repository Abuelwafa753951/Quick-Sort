def quicksort(array, low, high):
    if low < high:
        split_position = partition(array, low, high)
        
        quicksort(array, low, split_position - 1)
        quicksort(array, split_position + 1, high)

def partition(array, low, high):
    pivot = array[high]
    
    split_index = low
    
    for i in range(low, high):
        if array[i] <= pivot:
            array[i], array[split_index] = array[split_index], array[i]
            split_index += 1
    
    array[split_index], array[high] = array[high], array[split_index]
    
    return split_index


input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


quicksort(input_array, 0, len(input_array) - 1)
print("Sorted array:", input_array)
