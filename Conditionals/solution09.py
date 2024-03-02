year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This",  year , "is a leap year")
else:
    print(year, "Is NOT a leap year")