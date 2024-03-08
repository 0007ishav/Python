# def print_kwargs(name, power):
#     print("Name: ", name, " Power: ", power)


# print_kwargs(name = "Shaktimaan", power = "Laser")
# # print_kwargs(power = "Laser", name = "Shaktimaan")


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Shaktimaan", power = "Laser")
print_kwargs(name = "Shaktimaan")
print_kwargs(name = "Shaktimaan", power = "Laser", enemy = "Dr. Jackaal")