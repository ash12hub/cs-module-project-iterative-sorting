# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        if smallest_index > cur_index:
            arr[cur_index] = arr[cur_index] + arr[smallest_index]
            arr[smallest_index] = arr[cur_index] - arr[smallest_index]
            arr[cur_index] = arr[cur_index] - arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    repeat = True
    while repeat:
        repeat = False
        for i in range(0, len(arr) - 1):
            if arr[i + 1] < arr[i]:
                # Set loop to repeat
                if repeat == False:
                    repeat = True
                # Swap Values
                arr[i] = arr[i] + arr[i + 1]
                arr[i + 1] = arr[i] - arr[i + 1]
                arr[i] = arr[i] - arr[i + 1]

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=None):
    # Your code here
    if maximum is None and len(arr) > 0:
        maximum = max(arr)
        # Check negative.
        if min(arr) < 0:
            return "Error, negative numbers not allowed in Count Sort"
    buckets = []
    indexes = []
    if maximum:
        for i in range(0, maximum + 1):
            # Add 0 to buckets.
            buckets.append(0)
            indexes.append(i)
            total = 0

            # Count values and add the count to buckets.
            if i in arr:
                for j in arr:
                    if j == i:
                        total += 1
            buckets[i] = total
        
        # Selection Sort to sort the values in buckets.
        repeat = True
        while repeat:
            repeat = False
            for i in range(0, len(buckets) - 1):
                if buckets[i + 1] < buckets[i]:
                    # Set loop to repeat
                    if repeat == False:
                        repeat = True

                    # Swap bucket values
                    buckets[i] = buckets[i] + buckets[i + 1]
                    buckets[i + 1] = buckets[i] - buckets[i + 1]
                    buckets[i] = buckets[i] - buckets[i + 1]

                    # Swap indexes
                    if indexes[i + 1] != indexes[i]:
                        indexes[i] = indexes[i] + indexes[i + 1]
                        indexes[i + 1] = indexes[i] - indexes[i + 1]
                        indexes[i] = indexes[i] - indexes[i + 1]

        # Values with 0 are not in the original array. So remove them.
        while buckets[0] == 0:
            del indexes[0]
            del buckets[0]

        # Update the original array with the sorted array.
        arr = indexes

    return arr
