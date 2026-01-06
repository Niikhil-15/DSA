import math

def count_digits(num):
    """
     Brute Force
     Time complexity - O( log₁₀N )
     Space Complexity - O(1)
    """
    count = 0
    while num > 0:
        # last_digit = num % 10
        # print(last_digit)
        count += 1
        num //= 10
    
    return count

def count_digits_opt(num):
    """
    Optimal
    Time Complexity - O(1) as log func takes constant time
    """
    return int(math.log10(num) + 1)

def reverse_digits(num):
    """
    Time complexity - O( log₁₀N )
    Space Complexity - O(1)
    """
    rev = 0
    while num > 0:
        last_digit = num % 10
        rev = rev * 10 + last_digit
        num //= 10
    return rev

def check_pallin(num):
    return True if num == reverse_digits(num) else False

def check_armstrong(num):
    """
    
    """
    dup = num
    no_of_digits = len(str(num))
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit**no_of_digits
        num //= 10
    return True if dup == sum else False

def all_divisor(num):
    """
    Time Complexity : O(N)
    Space Complexity : O(N)
    """
    all_div_list=[]
    for i in range(1,num+1):
        if num % i == 0:
            all_div_list.append(i)
    return all_div_list

def all_divisor_optimal(num):
    """
    Time Complexity: O(sqrt(N)), we check for every number between 1 and sqaure root of N.
    Space Complexity: O(2*sqrt(N)), extra space used for storing divisors.
    """
    all_div_list = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            all_div_list.append(i)
            if ((num//i) != i):
                all_div_list.append(num//i)
    all_div_list.sort()
    return all_div_list

def check_prime(num):
    all_div_list = all_divisor_optimal(num)
    if len(all_div_list) == 2:
        return True
    else:
        return False

def find_gcd(num1, num2):
    """
    Brute Force
    Time Complexity: O(min(num1,num2))
    Space Complexity: O(1)

    Better Approach
    start from end instead from 1 as we are finding greated commom divisor, but
    Time Complexity remains sames as in worst case it still runs for min(N1, N2). 

    """
    gcd=1
    for i in range(1, min(num1, num2)+1):
        if num1 % i==0 and num2 % i==0 :
            gcd=i
    return gcd

def find_gcd_euclid(num1, num2):
    """
    Euclid :
        gcd(a, b) = gcd(a-b, b)  - if a > b 
        preform this repeatedly until one becomes 0. So other is gcd

    Time Complexity: O(logᵩ(min(num1, num2)))
    """
    while num1>0 and num2>0:
        if num1>num2:
            num1 %= num2

        else:
            num2 %= num1
    return num1 if num2 ==0 else num2
    


# print(reverse_digits(123))
# print(count_digits(1234567))
# print(count_digits_opt(7654321))
# print(check_pallin(1211))
# print(check_armstrong(153))
# print(all_divisor(36))
# print(all_divisor_optimal(72))
# print(check_prime(19))
# print(find_gcd(10,20))
# print(find_gcd_euclid(10,20))
