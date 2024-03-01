age = int(input("What's your age: "))
day = input("What's the day: ")

# day = "Wednesday"

price = 12  if age >= 18 else 8
# print(price)

if day == "Wednesday":
    price -= 2

print("Ticket price for you is $", price)