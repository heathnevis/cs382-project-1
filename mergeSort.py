import math

# helper function to construct a list object with n items and return it. 
# Helpful for populating new lists
def list_of_length(n):
    ls = []
    i = 0
    while i < n:
        ls.append(None)
        i += 1
    return(ls)

def Merge(A,p,q,r):
    n_L = q - p +1 # define the length of the left half
    n_R = r - q # define the length of the right half
    
    # use list_of_length to construct list objects with the proper left and right lengths and store them in L and R
    L = list_of_length(n_L)
    R = list_of_length(n_R)

    # populate Left with the left half of the area to be sorted
    for i in range(0,n_L):
        L[i] = A[p+i]
    
    # populate Right with the right half of the area to be sorted
    for j in range(0,n_R):
        R[j] = A[q+j+1]
    
    # set loop starter variables
    i = 0
    j = 0
    k = p

    # while we have not reached the end of either Left or Right, 
    # swap the lowest element from a comparison of Left and Right back into the main array
    while i < n_L and j < n_R:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # if any of Left remains, put it all in A in order
    while i < n_L:
        A[k] = L[i]
        i += 1
        k += 1
    
    # same as above for Right. Only one of these will execute
    while j < n_R:
        A[k] = R[j]
        j += 1
        k += 1

# use Merge() to recursively divide and conquer until the array is sorted.
# p and r define the start and end indices of the slice of array to be sorted
def Merge_Sort(A,p,r):
    if p < r:
        q = math.floor((p+r) / 2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merge(A,p,q,r)

# user-friendly wrapper of Merge_Sort() that sorts the whole array by default
def Merge_Wrapper(A):
    p = 0
    r = len(A) - 1
    Merge_Sort(A,p,r)