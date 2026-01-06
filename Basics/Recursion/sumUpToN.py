# brute force
'''
Time Complexity: O(n)
'''
def brute(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
    
# formula

def formula(n):
    return (n*(n+1))/2

# recursion

def sum_recursion(n):
    if n == 1:
        return 1
    return n + sum_recursion(n-1)

print(brute(10))
print(formula(10))
print(sum_recursion(10))