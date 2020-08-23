# It is used to find whether an element is present in a list or not.
#  there is a brute force solution called as linear search which has order of n

import time

l=[1,2,5,6,7,8,3,45,54,32,94,75]
l.sort()
target=32

def linear_search(data,target):
    for i in data:
        if i==target:
            return True
    return False

def bin_search(data,target): #order of log(n)   # works only on sorted list
    low=0
    high=len(data)-1
    
    while low<=high:
        mid=(low+high)//2
        if data[mid]==target:
            return True
        elif data[mid]<target:
            low=mid+1
        else:
            high=mid-1

    return False


# initial=time.time()
# print(linear_search(l,target))
# print(time.time()-initial)
# initial2=time.time()
print(bin_search(l,target))
# print(time.time()-initial2)