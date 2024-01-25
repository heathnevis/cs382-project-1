

def quicksort(array, l, r):
    if l < r:
        pivot = partition(array, l, r) #splits the array up based around the partitioned index
        #recurses on left half of partition
        quicksort(array, l, pivot-1)
        #recurses on right half of partition
        quicksort(array, pivot+1, r)

def partition(array, l, r):
    #sets the pivot to be the last element in the array, since it doesn't really matter what we set as the pivot
    pivot = array[r]
    #i is the pointer to the greater element
    i = l-1

    for j in range(l,r):
        if array[j] <= pivot:
            #if array[j] is smaller than the pivot, swap it with the greater element
            i += 1
            (array[i],array[j]) = (array[j],array[i])

    #swap pivot and greater element
    (array[i + 1], array[r]) = (array[r], array[i + 1])
    #position of pivot is returned
    return i+1

def quicksort_wrapper(array):
    quicksort(array,0,len(array)-1)