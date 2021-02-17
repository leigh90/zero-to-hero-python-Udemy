# def gen_fibon(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b, a+b

# for number in gen_fibon(10):
#     print(number)

# if you didnt use a generator 
# def gen_fibon(n):
#     a = 1
#     b = 1
#     output = []
#     for i in range(n):
#         output.append(a)
#         a,b = b, a+b
#     return output
#     # please note that the return statement is essential so it does not return None 

# print(gen_fibon(10))


# def simple_gen():
#     for x in range(3):
#         yield x

# # for number in simple_gen():
# #     print(number)

# g = simple_gen()
# print(next(g))
# # will print 0
# print(next(g))
# # will print 1
# print(next(g))
# # will print 2


# ITER()

s = 'hello'
# for i in s:
#     print(i)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))





