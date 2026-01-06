
# Time Compllexity - O(2N) if looping for printing too
# Space Complexity - O(N)
def fibo_brute(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])

    return fib
# print(*fibo_brute(5))

# No use of exxtra space 
# Time Complexity - O(n)
# Space Complexity - O(1)

def fibo_optimal(n):
    start = 0
    second = 1
    current = 0
    print(start, second,'',end='')
    for i in range(2,n+1):
        current=start+second
        print(current, end=' ')
        start = second
        second = current


# fibo_optimal(5)

# Time Complexity - O(2^n) , it is exponential as 2 functions are called and they are furter expanded n times
# Space Complexity - O(n) - as at a time there can be maximum of n busy stack space 
def fibo_recur(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        last=fibo_recur(n-1)
        slast= fibo_recur(n-2)
        return last+slast

for i in range(6):
    print(fibo_recur(i), end = ' ')