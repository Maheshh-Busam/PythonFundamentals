nums = {10,20,10,30,50,20}
print(nums)
print("----")

# Common set operations

skills = {"Java", "Python"}
skills.add("SQL")
print(skills)
print("----")

skills.remove("Java")
print(skills)
print("----")

# Use discard() if you want to remove a value without raising an error when it is missing.

skills.discard("SQL")
print(skills)
print("----")

# Set operations

a = {1,2,3}
b = {3,4,5}

print(a | b) # Union
print(a & b) # Intersection
print(a - b) # Difference
print("----")

# When to use: Removing duplicates, finding common items, or comparing collections.
