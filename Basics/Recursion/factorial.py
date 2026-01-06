def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
print(fact(5))

def fact_itr(n):
    val=1
    for i in range(1,n+1):
        val *= i
    return val
print(fact_itr(5))
