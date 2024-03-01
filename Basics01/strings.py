chai  = "Masala Chai"
# print(chai)

first_char = chai[0]
# print(first_char)

sliced_chai = chai[0:6]
# print(sliced_chai)

num_list = "0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])  # One no. hoping
print(num_list[0:7:3])  

print(chai.lower())
print(chai.upper())

chai2 = "      Masala Chai     "
print(chai2.strip())

chai3 = "Lemon Chai"

print(chai3.replace("Lemon", "Ginger"))
print(chai3) # String is mutable . original chai3 is same as it is.

chai_list = "Lemon, Ginger, Masala, Mint"

print(chai_list.split())  # By default , spacing se split kr dega

print(chai_list.split(", ")) # comma & space won't be included.


print(chai.find("Chai")) # find the strings
print(chai.find("chai")) # -1 bcuz chai is lowercase is not in string.

chai4 = "Masala Chai Chai Chai"
print(chai4.count("Chai"))


# Formatter  (Able to add variables using format() into placeholders)
Chai_type = "Masala"
quantity = 2
order  = "I ordered {} cups of {} chai"
print(order.format(quantity, Chai_type))



chai_variety = ["Lemon", "Masala", "Ginger"]

print(" ".join(chai_variety))
print("_".join(chai_variety))
print(", ".join(chai_variety))

# for letter in chai:
#     print(letter)

chai5 = "He said, \"Masala chai is awesome\" " # able to use double quotes like this with backslash

path = r"c:\user\pwd"
print(path)

path2 = "c:\\user\\pwd"
print(path2)

print("Masala" in chai)