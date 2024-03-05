while True:
    number = int(input("Enter a value b/w 1 & 10: "))

    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("invalid number, try again")
