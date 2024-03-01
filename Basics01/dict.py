chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

# print(chai_types["Masala"])


# print(chai_types.get("Ginger"))



# print(chai_types["Masalaa"])    # KeyError: 'Masalaa'
# print(chai_types.get("Gingery")) # None



# chai_types["Green"] = "Fresh"
# print(chai_types)



# for chai in chai_types:
#     print(chai)    # it will print keys



# for chai in chai_types:
    # print(chai, chai_types[chai])    # It will print keys & values.
    # print(chai_types[chai])     # It willl print values



# for key, value in chai_types.items():    # need to use items() for using both key & values simultaneously. key + value = item
#     print(key, value)



# if "Masala" in chai_types:
#     print("I have masala chai.")

# print(len(chai_types))


# Adding item in dictionary
chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

# print(chai_types.pop("Ginger"))  
# print(chai_types)

# print(chai_types.popitem())  # It will pop out the last item
# print(chai_types)

# del chai_types["Green"]    # "del" deletes the item from the memory space
# print(chai_types)


chai_types_copy = chai_types.copy()
# print(chai_types_copy)

tea_shop = { "chai": {"Masala": "Spicy", "Ginger": "Zesty"}, 
            "tea" : {"Green": "Mild", "Black": "Strong"}
            }

# print(tea_shop)

# print(tea_shop["chai"])

# print(tea_shop["chai"]["Ginger"])

# squared_nums = {x: x ** 2 for x in range(8)}s
## squared_nums.clear()
# print(squared_nums)

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

# new_dict = dict.fromkeys(keys, default_value)
new_dict = dict.fromkeys(keys, keys)
print(new_dict)