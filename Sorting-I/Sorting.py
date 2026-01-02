def selection_sort(arr):
    for i in range(len(arr)-1):
        min_i=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i] 
    
    return arr

arr=[23,12,89,22,9,1]
print(selection_sort(arr))