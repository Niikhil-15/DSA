arr = [1,4,6,3,52]
# using 2 pointer
# def swap(a,b):
#     return (b,a)
def reverse(arr):
    start = 0
    end = len(arr)-1
    for _ in range(end+1):
        arr[start], arr[end] =  arr[end], arr[start]
        if end-start == 0 or end-start ==1:
            return arr
        start+=1
        end-=1

def rev_rec(s,e):
    if s>=e:
        return

    arr[s], arr[e] = arr[e], arr[s]
    rev_rec(s+1,e-1)


# print(reverse(arr))
# print(arr)
# rev_rec(0,len(arr)-1)
# print(arr)

# using single pointer

def single_pointer_reverse(arr):
    n = len(arr)
    for i in range(len(arr)):
        if i >= n/2:
            return
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]


def single_pointer_reverse_rec(i,n):
    if i >= n/2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    single_pointer_reverse_rec(i+1,n)



# print(arr)
# single_pointer_reverse_rec(0,len(arr))
# print(arr)