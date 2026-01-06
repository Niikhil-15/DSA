arr=[23,12,89,22,9,1]

# Time Complexity - O(N²) for all cases
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_i=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i] 
    
    return arr


# print(selection_sort(arr))


# Time Complexity - Worst Case and Average Case - O(N²) but best case is O(N) if given arr is already sorted 

def bubble_sort(arr):
    for i in range(len(arr)-1):
        didSwap=0
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap=1
        if didSwap==0: break


# print(arr)
# bubble_sort(arr)
# print(arr)

# Insertion Sort

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while (j>0 and arr[j]< arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr
print(arr)
insertion_sort(arr)
print(arr)

