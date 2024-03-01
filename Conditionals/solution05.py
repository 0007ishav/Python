weather = input("Choose the Weather(Sunny, Rainy, Snowy): ").lower()

if weather == "sunny":
    activity = "Go for a walk"

elif weather == "rainy":
    activity = "Read a book"

elif weather == "snowy":
    activity = "Build a snowman"

else:
    activity = "Stay Indoors"

print(activity)
