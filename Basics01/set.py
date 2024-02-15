# Set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements form them, but the elements themselves muuste be immutable(numbers, strings).

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to the set
my_set.add(6)
my_set.add(7)

# Removing elements from the set
my_set.remove(3)

# Checking membership
if 5 in my_set:
    print("5 is in the set")
else:
    print("5 is not in the set")

# Iterating over the set
for item in my_set:
    print(item)


# Set operations
other_set = {4, 5, 6, 8, 9}

union_set = my_set.union(other_set)
print("Union:", union_set)

# Intersection
intersection_set = my_set.intersection(other_set)
print("Intersection:", intersection_set)

# Difference
difference_set = my_set.difference(other_set)
print("Difference:", difference_set)



# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform intersection using &
intersection_set = set1 & set2

# Print the result
print("Intersection:", intersection_set)


# Union set
union_set = set1 | set2

# Difference 
difference_set = set1 - set2   # The - operator is used to perform the difference operation on sets. It returns a new set containing elements that are present in the first set but not in the second set.

# Symmetric Difference
symmetric_difference_set = set1 ^ set2  # The ^ operator is used to perform the symmetric difference operation on sets. It returns a new set containing elements that are present in either set, but not in both.



