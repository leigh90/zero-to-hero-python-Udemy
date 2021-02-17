# generator functions allow us to write a function that can send back a value then later resume to pick up where it left off 
# generators allow us to generate a sequence of values over time
# the automatically suspend and rsume their execution and state around the last point of value generation
# instead of computing all the values upfront and then storing them in memory, the generator computes one value a time then waits till the next value is called for 

# so here you have to create all those values and store them in memory
# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     print(result)
#     return result
# create_cubes(10)

def create_cubes(n):
    for x in range(n):
        yield x**3
# what this does is produce the values as you need them without having to store them in memory
# for x in create_cubes(10):
#     print(x)

# if you dont use an iterator like the for loop you will not be able to print the values for the example printing the object below returns location of the object in memory
# print(create_cubes(10))
# this will save the values to a list
# print(list(create_cubes(10)))
print(create_cubes(10))
