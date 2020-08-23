# Left Shift 
x=2
y=x<<2  # Left Shift by 2 digits
# Left shift by k digits basically means that x=x*(pow(2,k))

# Right shift 
x=2
y=x>>2 # Right shift by 2 places
# Right shift by k digits basically means that x=x//(pow(2,k))

# Checking if the ith bit is set or not means at that particular bit from behind is 1 or not
n=int(input())
i=int(input())
f=1
f=f<<i
if f&n==f:
    print(True)
else:
    print(False)