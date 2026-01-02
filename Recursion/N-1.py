def forward_recursion(end, n):
    if end < 1:
        return
    print(end)
    forward_recursion(end-1, n)


def backtracking(start, n):
    if start > n:
        return
    backtracking(start+1, n)
    print(start)

# forward_recursion(15,12)
backtracking(1,13)
