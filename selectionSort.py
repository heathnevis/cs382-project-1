# return the index of the largest element in the array smaller than the element at index i
def prefix_max(array, i):
    if i > 0:
        j = prefix_max(array, i-1)
        if array[i] < array[j]:
            return j
    return i
    
# swap in place the array elements found at index1 and index2
def swap(array,index1,index2):
    if is_valid(array,index1) and is_valid(array,index2):
        temp_index2 = array[index2]
        array[index2] = array[index1]
        array[index1] = temp_index2
        # return true if the values were succesfully swapped
        return True
    else:
        # otherwise return False
        return False

# helper function to check if an index is valid in a given array
def is_valid(array,index):
    return 0 <= index < len(array)

# implementation of selection sort using swap() and prefix_max()
def selection_sort(array, i=None):
    # if this is the first call, set i to the full length of the array and then recurse
    if i is None:
        i = len(array)
    if i > 0:
        # find the largest element in the array that occurs before index i
        j = prefix_max(array, i-1)
        # swap that largest element and the element at index i
        swap(array,i,j)
        # recurse leftward on the slice of the array that hasn't yet been sorted (from index 0 to index i-1)
        selection_sort(array, i-1)