import argparse #documentation: https://docs.python.org/3/library/argparse.html
import time
import makeArray
from mergeSort import Merge_Wrapper
from quickSort import quicksort_wrapper
from selectionSort import selection_sort
import sys

def timeSort(sorting_method,array):
    if sorting_method == "QuickSort":
        start_time = time.time()
        quicksort_wrapper(array)
        end_time = time.time()
    elif sorting_method == "MergeSort":
        start_time = time.time()
        Merge_Wrapper(array)
        end_time = time.time()
    elif sorting_method == "SelectionSort":
        start_time = time.time()
        selection_sort(array)
        end_time = time.time()
    else:
        return None
    return end_time - start_time

sys.setrecursionlimit(10000)

# define positional arguments
parser = argparse.ArgumentParser()
parser.add_argument('sizeMin', type=int, help="Minimum input size to test")
parser.add_argument('sizeIncr', type=int, help="Increment for input size")
parser.add_argument('sizeMax', type=int, help="Maximum input size to test")
parser.add_argument('numTrials', type=int, help="Number of trials for each input size")

# define optional arguments
parser.add_argument('--whichsorts', '-w',
                    nargs='+',
                    type=str,
                    help="One or more sorts to test. Default is to test all sorts."
                    )

parser.add_argument('--generator', '-g',
                    choices=["random", "ordered", "evil"],
                    default = "random",
                    help="Specifies the input generator to use. Default is random."
                    )

# parse command line arguments based on definitions
args = parser.parse_args()
# your code here
#makes sorts default to all if none are specified
if (args.whichsorts == None):
    args.whichsorts = ["QuickSort", "MergeSort", "SelectionSort"]
#formatting the beginning
print("N,", end="\t")

if args.whichsorts == None:
    args.whichsorts = ["QuickSort","MergeSort","SelectionSort"] # if no sorts have been provided, default to all of them

for i in args.whichsorts:
    print(i, end="\t")
print("")
#iter keeps track of the current size of the array to be tested
iter = args.sizeMin
while(iter <= args.sizeMax):
    print(iter,",", end="\t")
    for i in args.whichsorts:
        total_time = 0
        for j in range (args.numTrials):
            #makearray takes a size (iter), a generation scheme, and the sort type (only used for evil mode >:)
            array = makeArray.makeArray(iter, args.generator, i)
            #timeSort takes a sorting method and an array and returns the time taken to sort it
            total_time += timeSort(i, array)
        avg_time = total_time / args.numTrials
        print("%10s" % round(avg_time,8), end="\t")
    print("")
    iter += args.sizeIncr

#:]
