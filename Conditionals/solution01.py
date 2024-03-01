age = int(input("What's your age: "))

# if (age < 13 and age > 0):
#     print("Child")

# elif (age >= 13 and age <= 19):
#     print("Teenager")

# elif age >= 20 and age <= 59:
#     print("Adult")

# else:
#      print("Senior")


if age == 0:
    print("Add a valid age")

elif age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")
    
else:
    print("Senior")