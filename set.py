collection={1,2,3,4,"Hello","World"}
print(collection)
print(type(collection))

set1={1,2,2,2,"Hello","World","World"}
print(set1)
print(type(set1))

# len() returns length
print(len(set1))

set2=set()    # empty set
print(type(set2))

# set.add(el) # add an element
set2.add(1)
set2.add(2)
set2.add(2)
print(set2)

# set.remove(el) # removes the element
set2.remove(1)
print(set2)

# set2.remove(7)
# print(set2)

set2 = set()
set2.add(1)
set2.add(2)
set2.add("apnacollege")
set2.add((1,2,3))
print(set2)

# set2.add([1,2,3])
# print(set2)

print(len(set2))

set2.clear()
print(len(set2))

print(set2)

set2={"hello","apnacollege","world","coding","python"}
print(set2.pop())

print(set2.pop())
print(set2.pop())

# set.union(set2)      # combines both set values & return new
# set.intersection(set2)  # combines common values & returns new
s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))         # {1,2,3,4}

print(s1)
print(s2)
print(s1.intersection(s2))      # {2,3}