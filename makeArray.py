import random

#randomArray takes an int size, a string gen_type, and a string sort_type
#and returns an array of size 'size', 
def makeArray(size, gen_type, sort_type):
    ret_array =  []
    if( gen_type == "random"):
        for i in range(size):
            ret_array.append(random.randint(0,size-1))
    elif (gen_type == "ordered"):
        for i in range(size):
            ret_array.append(i)
    elif(gen_type == "evil"):
        if(sort_type == "QuickSort"): #sorted or reverse
            for i in range(size):
                ret_array.append(size-i-1)
        elif(sort_type == "SelectionSort"):#reverse order
            for i in range(size):
                ret_array.append(size-i-1)
        elif(sort_type == "MergeSort"): #probably just reverse order
            for i in range(size):
                ret_array.append(size-i-1)
    return ret_array
