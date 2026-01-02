def forward_recursion(start, n):
    if start == n:
        return
    print(start)
    forward_recursion(start+1, n)

# forward_recursion(1, 10)

# recursion without using end+1 
def backtracking(end):
    if end <1:
        return
    backtracking(end-1)
    print(end)

# backtracking(10)
    

