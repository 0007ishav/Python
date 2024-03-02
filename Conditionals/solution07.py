order_size = input("Choose the size (S, M, L): ").lower()
extra_shot = input("Would you like extra shot(T/F): ").lower()


if order_size == "m":
    size = "Medium"
elif order_size == "s":
    size = "Small"
elif order_size == "l":
    size = "Large"
else:
    print("Invalid size.")

boolean_value = None
if extra_shot == 't':
    boolean_value = True
elif extra_shot == 'f':
    boolean_value = False
else:
    print("Invalid input. Please enter t or f.")

if boolean_value:
    coffee = size + " Coffee with an extra short"
else:
    coffee = size + " Coffee "

print("Order: ",coffee)