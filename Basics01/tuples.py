tea_types = ("Black", "Green", "Oolong")
# print(tea_types)
# print(tea_types[0])
# print(tea_types[-1])
# print(tea_types[1:3])
# print(tea_types[:3])

# tea_types[0] = "Lemon"  # TypeError: 'tuple' object does not support item assignment
# print(tea_types)

print(len(tea_types))

more_tea = ("Herbal", "Earl Grey")

all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have green tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")

print(more_tea.count("Herbal"))
print(more_tea.count("herbal"))


(black, green, oolong) = tea_types   # (black, green, oolong) These are treated as variables and tuples items will be unwraped to these variables. Number count of variables and tuples items must be same.
print(black)     
print(green)
print(oolong)

print(type(tea_types))
print(type(black))