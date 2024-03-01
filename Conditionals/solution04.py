fruit = input("What's the fruit(E.g - Banana): ").lower()
color = input("What's the Color(Green, Yellow, Brown): ").lower()

print(fruit)
print(color)

if fruit != "banana":
    print("I don't have the information of this fruit.")

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("OverRipe")