pet = input("Choose your pet(Dog, Cat): ").lower()
age = int(input("Input the age in numbers: "))


if age == 0:
    print("Invalid age")
    exit()

if pet == 'dog':
    if age <  2:
        print("Puppy dog food")
    else:
        print("Adult dog food")
elif pet == 'cat':
    if age < 5 and age > 0:
        print("Junior cat food")
    else:
        print("Senior cat food")