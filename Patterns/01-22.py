def pattern_01(n):
    """
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * * 
    """
    for i in range(n):
        for j in range(n):
            print('* ',end='')
        print()

def pattern_02(n):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    i = 1
    for i in range(n+1):
        for j in range(i):
            print('* ', end='')
        print()

def pattern_03(n):
    """
    1
    1 2
    1 2 3
    1 2 3 4
    """
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f'{j} ', end='')
        print()

def pattern_04(n):
    """
    1
    2 2 
    3 3 3 
    4 4 4 4
    """

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,'',end='')
        print()

def pattern_05(n):
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print('* ', end='')
        print()

def pattern_06(n):
    """
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    """
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,'',end='')
        print()

def pattern_07(n):
    """
        *
       ***
      *****
     *******
    *********
    """
    for i in range(1,n+1):
        # space
        for j in range(n-i):
            print(' ',end='')

        # star
        for j in range(2*i-1):
            print('*', end='')
        
        print()

def pattern_08(n):
    """
    *********
     *******
      *****
       ***
        *
    """
    for i in range(n,0,-1):
        # space
        for j in range(n-i):
            print(' ',end='')

        # star
        for j in range(2*i-1):
            print('*', end='')
        print()
       
def pattern_09(n):
    """
        *
       ***
      *****
     *******
    *********
    *********
     *******
      *****
       ***
        *
    """
    pattern_07(n)
    pattern_08(n) 

def pattern_10(n):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    for i in range(1,2*n):
        if i<=n:
            for j in range(1,i+1):
                print('* ', end='')
        else:
            for j in range(1, 2*n-i+1):
                print('* ', end='')

        print()
        
def pattern_11(n):
    """
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1
    """
    start=1
    for i in range(1,n+1):
        # if i % 2 == 0:
        #     start=0
        # else :
        #     start = 1
        start=0 if i % 2==0 else 1
        for j in range(i):
            print(start,'', end='')
            start = 1-start
        print()

def pattern_12(n):
    """
    n=4

    1      1
    12    21
    123  321
    12344321
    """
    for i in range(1,n+1):
        # pattern
        for j in range(1,i+1):
            print(j,end='')

        # space
        for j in range(0,2*n-2*i):
            print(' ',end='')

        # pattern
        for j in range(i,0,-1):
            print(j,end='')
        
        print()

def pattern_13(n):
    """
    n = 5
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    """
    start=1
    for i in range(n):
        for j in range(i+1):
            print(start, '', end='')
            start+=1
        print()

def pattern_14(n):
    """
    A
    AB
    ABC
    ABCD
    ABCDE
    """
    for i in range(n):
        for j in range(ord('A'), ('A')+i+1):
            print(chr(j),end='')
        print()

def pattern_15(n):
    """
    ABCDE
    ABCD
    ABC
    AB
    A
    """
    for i in range(n):
        for j in range(ord('A')+n-i-1, ord('A')-1, -1):
            print(chr(j), end='')
        print()  

def pattern_16(n):
    """
    A
    BB
    CCC
    DDDD
    EEEEE
    """
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i), end='')
        print()

def pattern_17(n):
    """
        A
       ABA
      ABCBA
     ABCDCBA
    ABCDEDCBA
    """
    # ----My Method ---
    # for i in range(n):
    #     # space
    #     for j in range(n-1-i, 0, -1):
    #         print(" ", end='')
        
    #     # part_1
    #     for j in range(i+1):
    #         print(chr(65+j), end='')

    #     # part_2
    #     for j in range(i,0,-1):
    #         print(chr(65+j-1), end='')

    #     print()


    # ------Striver's Method-----
 
    for i in range(n):
        A = 64
        breakpoint = i
        for j in range(n-i-1,0,-1):
            print(' ', end='')

        for j in range(2*i + 1):
            if j<=breakpoint :
                A += 1
                print(chr(A), end='')          
            else:
                A -= 1
                print(chr(A), end='')     

        print()

def pattern_18(n):
    """
    E
    D E
    C D E
    B C D E
    A B C D E
    """
    A = ord('A')
    for i in range(n):
        for j in range(n-1-i,n):
            print(chr(A+j),'',end='')
            
        print()

def pattern_19(n):
    """

    **********
    ****  ****
    ***    ***
    **      **
    *        *
    *        *
    **      **
    ***    ***
    ****  ****
    **********

    """

    for i in range(2*n):
        if i < n:
            # pattern
            for j in range(n-i):
                print('*', end ='')

            # space
            for j in range(2*i):
                print(' ', end='')

            # pattern
            for j in range(n-i):
                print('*', end='')

            print()

        else: # i > n
            k = i-n+1
             # pattern
            for j in range(k):
                print('*', end ='')

            # space
            for j in range(2*n-2*k):
                print(' ', end='')

            # pattern
            for j in range(k):
                print('*', end='')

            print()

def pattern_20(n):
    """

    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *

    """
    for i in range(1,2*n):
        if i <= n:
            # star
            for j in range(i):
                print('*', end='')

            # space
            for j in range(2*(n-i)):
                print(' ', end ='')

            # star
            for j in range(i):
                print('*', end='')
            print()

        else:
            k = 2*n - i
            # star
            for j in range(k):
                print('*', end='')

            # space
            for j in range(2*(n-k)):
                print(' ', end='')

            # star
            for j in range(k):
                print('*', end='')

            print()

def pattern_21(n):
    """
    ****
    *  *
    *  *
    ****
    """
    # for i in range(n):
    
    #     if i ==0 or i == n-1:
    #         for j in range(n):
    #             print('*',end='')
    #         print()
    #     else:
    #         print('*', end='')
    #         for j in range(n-2):
    #             print(' ', end='')
    #         print('*',end='')
    #         print()


    for i in range(n):
        for j in range(n):
            if (i ==0 or j == 0 or i == n-1 or j == n-1):
                print('*', end='')
            else:
                print(' ', end ='')
        print()

def pattern_22(n):
    """
    4 4 4 4 4 4 4     
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4 
    4 3 2 2 2 3 4
    4 3 3 3 3 3 4
    4 4 4 4 4 4 4
    """
#  convert pattern to n - num
    """
    0 0 0 0 0 0 0 
    0 1 1 1 1 1 0
    0 1 2 2 2 1 0
    0 1 2 3 2 1 0
    0 1 2 2 2 1 0
    0 1 1 1 1 1 0
    0 0 0 0 0 0 0
    """
    N=2*n -1
    for i in range(N):
        for j in range(N):
            
            left = j
            top = i
            right = N-j -1
            down = N-i -1
            print(n - min(left, right, top, down),'', end='')
        print()
      

# pattern_22(4)
