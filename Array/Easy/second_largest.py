""" 
Problem Statement: 
Given an array, find the second smallest and second largest element in the array.
Print ‘-1’ in the event that either of them doesn’t exist.

Example 1:
Input:
 [1, 2, 4, 7, 7, 5]  
Output:
  
Second Smallest : 2  
Second Largest : 5  
Explanation:
  The elements are sorted as 1, 2, 4, 5, 7, 7.  
Hence, the second smallest element is 2, and the second largest element is 5.

Example 2:
Input:
 [1]  
Output:
  
Second Smallest : -1  
Second Largest : -1  
Explanation:
  Since there is only one element in the array, it is both the largest and smallest element.  
Therefore, there is no second smallest or second largest element present.
"""

# Brute Force(Self)
# T.C - O(NlogN) + O(N) {only for finding slargest}
# S.C = O(1) for all

def brute(arr):
    if len(arr) == 0:
        return (-1,-1)
    arr.sort() 
    largest = arr[-1]
    second_largest = -1
    smallest = arr[0]
    second_smallest=-1
    for i in arr:
        if i != smallest:
            second_smallest = i
            break

    prev = -1
    for i in arr:
        if i == largest:
            second_largest = prev
            break
        prev = i
    return second_smallest, second_largest


# T.C = O(2N) {only for finding slargest}
def better(arr):

    # using 2nd pass method

    largest = arr[0]
    slargest = -1
    for i in arr:
        if i > largest:
            largest = i
    for i in arr:
        if i > slargest and i != largest:
            slargest = i
    print(slargest) 


# T.C = O(N) {only for finding slargest}
def optimal(arr):
    if len(arr) in (0,1):
        return (-1,-1)
    

    def second_largest(arr):
        largest = arr[0]
        slargest = -1
        for i in arr:
            if i > largest :
                slargest = largest
                largest = i
            elif i < largest and i > slargest:
                slargest = i
        return slargest

    def second_smallest(arr):
        smallest = arr[0]
        ssmallest = float('inf')

        for i in arr:
            if i < smallest:
                ssmallest = smallest
                smallest = i
            elif i > smallest and i < ssmallest:
                ssmallest = i
        return ssmallest
     
    slargest = second_largest(arr)
    ssmallest = second_smallest(arr)

    return ssmallest, slargest


arr = [1,3,2,4,53,25,6232,22,322,7,]
arr1=[1]

# better(arr)
# print(optimal(arr1))
# print(brute(arr1))

