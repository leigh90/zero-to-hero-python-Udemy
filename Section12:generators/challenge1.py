# def gensquares(n):
#     for x in range(n):
#         yield x**2

# for num in gensquares(10):
#     print(num)


# PROBLEM 2
import random

# random.randint(n,y)
def rand_num(low,high,n):
    for x in range(n+1):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)
        
s = 'hello'
s_iter = iter(s)

print(next(s_iter))