"""
Problem Statement: Given an array of size n, write a program to check if 
the given array is sorted in (ascending / Increasing / Non-decreasing) 
order or not. If the array is sorted then return True, Else return False.

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.
Here element 5 is not smaller than or equal to its future elements.
            

"""

def check_sorted(arr):
    prev = arr[0]
    
    for i in range(1,len(arr)):
        curr = arr[i]
        if prev > curr :
            return False
        prev = arr[i]
    return True

arr = [1,2,3,4,5,8,8,9]
arr1 = [1,21,3,52,51,5,6]

print(check_sorted(arr))

