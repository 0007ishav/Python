distance = int(input("Distance: "))

if distance < 3:
    transport = "Walk"
elif distance <=15:
    transport = "bike"
else:
    transport = "Car"

print("AI recommends you the transport of:", transport)