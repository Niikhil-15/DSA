

arr = [1,2,3,1,1,1,4,3,2,3,2,3,4]

# brute force by using loops only
# Time Complexity - O(N^2)
# Space Complexity - O(N)
def count(arr):
    visited=[]
    for i in arr:
        if i in visited:
            continue
        i_count = 0
        for j in arr:
            if i == j:
                i_count+=1
        visited.append(i)
        print(i, i_count)
    


# count(arr)


# using dictionary
# Time Complexity - O(N) - as dict operation takes O(1) in best, average case and take O(N) in worst case but it happens rarely due to collisions. So consider O(1) => O(N) + O(1) = O(N) 
# Space Complexity - O(N) as storing frequncies in dict

def count_dict(arr):
    counting ={}
    for i in arr:
        if i in counting:
            counting[i] = counting[i]+1
        else:
            counting[i] = 1
    return counting

# print(count_dict(arr))


def hashing(num, arr):
    """
    Hashing using Array/List,
    let each element be not more than 12 and is 0 or positive
    """
    hash = [0]* 13
    for i in arr:
        hash[i]+=1
    # print(hash)
    return hash[num]
print(hashing(4,arr))


# Time Complexity - O(N) effectively as O(N) also comes from loop adding both gives - O(2N) but can be written as O(N) 
# Space Complexity - O(N) this comes from creating hash or dict

def min_and_max_freq(arr):
    freq=count_dict(arr)
    
    M,m =0,len(arr)
    for key, value in freq.items():
        if value>M:
            M = key

        elif value<m:
            m = key
        # print(M,m)
    return M,m

# print(min_and_max_freq(arr)) 




