from collections import Counter

# use counter to count the number of instances of each element in a list and orders them in order of element with the highest number of appearances
mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3]
print(Counter(mylist))
# returns a dictionary object with the elements being counted as the key values and the times they appear as the value of the keys

mysec = ['a','a',10,10,10]
print(Counter(mysec))

# it also works with strings
print(Counter('aaaabbbhhhhjkldoooo'))
# for sentences you would have to split it into strings first
sentence = "How many times does each word show up in this sentence with word"
print(Counter(sentence.split()))

# you can convert the ouput to a normal dictionary
# highest = dict(Counter(sentence.split()))

# COMMON COUNTER OBJECTS
# return te most commonly occuring element, returns a list of tuples in descending order
letters = 'aaaaabbbbbbcccccccdddddhhhhhhhh'
wow = Counter(letters)
print(wow.most_common())

# you can pass it to a list 
print(list(wow))

# defaultdict is used to assign default values where a key error would have occured 
from collections import defaultdict
d = {'a':10}
d['a']
# d['d'] #will not work because there's no key 'd'. this is where defaultdict comes in

d = defaultdict(lambda:0)
d['correct'] = 100
print(d['wrong key']) #assigns the 'wrong_key' value to 0 even though we did not assign it as would be expected to avoid wrong keyerror


# named tuple
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5, breed='Husky', name='Sam')
print(type(sammy))
print(sammy.age)
print(sammy.breed)


# SHELL UTILITY MODULE AND OS MODULE

# OPENING AND CLOSING FILES
f = open('practise.py','w+')
f.write('This is a test string')
f.close()
