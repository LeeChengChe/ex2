from functools import partial

# by convention, we give classes PascalCase names
class Set:
 # these are the member functions
 # every one takes a first parameter "self" (another convention)
 # that refers to the particular Set object being used
 def __init__(self, values=None):
     """This is the constructor.
     It gets called when you create a new Set.
     You would use it like
     s1 = Set() # empty set
     s2 = Set([1,2,2,3]) # initialize with values"""
     self.dict = {} # each instance of Set has its own dict property
                    # which is what we'll use to track memberships
     if values is not None:
        for value in values:
            self.add(value)
 def __repr__(self):
     """this is the string representation of a Set object
     if you type it at the Python prompt or pass it to str()"""
     return "Set: " + str(self.dict.keys())
 # we'll represent membership by being a key in self.dict with value True
 def add(self, value):
    self.dict[value] = True
 # value is in the Set if it's a key in the dictionary
 def contains(self, value):
    return value in self.dict
 def remove(self, value):
    del self.dict[value]

s = Set([1,2,3])
s.add(4)
print s.contains(4) # True
s.remove(3)
print s.contains(3) # False
print("class(set) :" + str(s))

class Set1(Set):
    def __repr__(self):
        """this is the string representation of a Set object
        if you type it at the Python prompt or pass it to str()"""
        return "Set: " + str(self.dict.keys())

s1 = Set1([1,2,3,4])
s1.add(10)
print("class(set1) :" + str(s1))
print("")

def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]


def double(x):
    return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
twice_xs = map(double, xs) # same as above
print("twice_xs - for: " + str(twice_xs))
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs)
print("twice_xs - map: " + str(twice_xs))
print("")

def is_even(x):
 """True if x is even, False if x is odd"""
 return x % 2 == 0
x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above
print("filter: " + str(x_evens))
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]
print("list_evener: " + str(x_evens))

x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24

print("reduce: " + str(x_product))
print("list_product: " + str(x_product))
print("")

print("enumerate: ")
documents = ["aa","bb","cc"]
for i, document in enumerate(documents):
    print(i, document)

print("")

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = zip(list1, list2) # is [('a', 1), ('b', 2), ('c', 3)]
print("list3: " + str(list3))
print("")

letters, numbers = zip(*list3)
print("zip(*list3): " + str(letters))
print("zip(*list3): " + str(numbers))

def magic(*args, **kwargs):
    print "unnamed args:", args
    print "keyword args:", kwargs

magic(1, 2, 3, 4, "aaaaaa", key="word", key2="word2")
# prints
# unnamed args: (1, 2)
# keyword args: {'key2': 'word2', 'key': 'word'}
