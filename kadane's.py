# Maximum Subarray Sum | Kadane's Algorithm in O(n) time complexity

def kadane(l):
    add=0
    maxi=l[0]
    for i in l:
        add+=i
        if add>maxi:
            maxi=add
        if add<0:
            add=0
    return maxi
print(kadane([-2,-3,4,-1,-2,5,1,-3]))