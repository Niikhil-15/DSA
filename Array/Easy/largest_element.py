# Brute Force 
def largest_element_brute(arr):
    arr.sort()
    return arr[-1]

# Optimal Force
def largest_element(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

arr = [1,3,2,4,5,62,5,243,4,98]

print(largest_element(arr))
print(largest_element_brute(arr))