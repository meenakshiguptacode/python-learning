# sets in python
# sets is the collection of unordered items
# Each elements in the set must me unique and immutable

nums = {1,2,3,4}

sets = {1,2,2,2}
# repeated element stored only once , so it resolved to {1,2}

null_set = set() # empty set syntax

collection = {1,2,3,4, 2}

print(collection)
print(type(collection))

print(len(collection))

# set methods 

# Adds elements
# set.add(el)

# Remove the ele 
# set.remove(el)

# empties the set
# set.clear()

# removes the random value
# set.pop()


collectionSet = set()
collectionSet.add(1)
collectionSet.add(2)
collectionSet.add(2)

collectionSet.add("test")

print(collectionSet)
print(type(collectionSet))

print(len(collectionSet))
# clear the set
#print(collectionSet.clear())


print(collectionSet.pop())
print(collectionSet)

# set methods 

# combines both set vaklues nd return new
# set.union(set2)


# combines common values and return new
# set.union(set2)



set1 = {1,2,3}

set2 = {2,2,3,4,5}

print(set1.union(set2))

print(set1.intersection(set2))

