def print_something():
    print("Something")
    print_something()

# print_something()

"""
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.
Input: N = 1
Output: Ashish 
Explanation: Name is printed once.
"""

def n_times_name(n, name="Nikhil"):
    num=11-n
    if n == 0:
        return
    print(num,name)
    n_times_name(n-1)

n_times_name(10)