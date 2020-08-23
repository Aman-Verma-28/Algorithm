def power(m,n):
    res=1
    while n>0:
        if n%2==1:
            res*=m
        m*=m
        n=n//2
    return res

import time
m=50
n=50
x=time.time()
print(power(m,n))
print(time.time()-x)
y=time.time()
print(pow(50,50))
print(time.time()-y)

# Use the builtin pow function as it is faster
# Iterative codes are faster than recursive codes

# modulo while addition multiplcation and substraction

# addition

a=567
b=432
m=16 # modulo
print((((a%m)+(b%m))%m)==((a+b)%m))

# The above verison is around three times slower than below
res=a+b
if res>m:
    res-=m


# multiplication

print(((a%m)*(b%m)%m)==((a*b)%m))

#Substraaction
result=((a%m)-(b%m))%m
if result<0:
    result+=m

