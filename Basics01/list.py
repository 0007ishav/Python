tea_varieties = ["Black", "Green", "Oolong", "White"]

# print(tea_varieties)


# print(tea_varieties[0])
# print(tea_varieties[-1])
# print(tea_varieties[1:3])

tea_varieties[1:2] = "Lemon" # Lemon wil be treated as an array.

# print(tea_varieties)   # ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'White']


tea_varieties2 = ["Black", "Green", "Oolong", "White"]
tea_varieties2[1:2] = ["Lemon"]  
# print(tea_varieties2)     #['Black', 'Lemon', 'Oolong', 'White']

tea_varieties3 = ["Black", "Green", "Oolong", "White"]

tea_varieties3[1:3] = ["Lemon", "Masala"]
# print(tea_varieties3)

tea_varieties4 = ["Black", "Green", "Oolong", "White"]

# print(tea_varieties4[1:1])
tea_varieties4[1:1] = ["test", "test"]
# print(tea_varieties4)
tea_varieties4[1:1] = []  # Insert nothing

# for tea in tea_varieties:
#     print(tea)

# for tea in tea_varieties2:
#     print(tea)

# for tea in tea_varieties2:
#     print(tea, end="-")


# pop() it will echo back & remove() it wont echo back anything.

# insert() i will shift the positions
    
# copy() it will create a new refernce.

# append()
    
# List comprehension
    
squared_nums = [x ** 2 for x in range(10)]

print(squared_nums)

cube = [y ** 3 for y in range(5)]
print(cube)