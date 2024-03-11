# Solution 1

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

# Solution 2

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# my_car = Car("Toyota", "Corolla")
# print(my_car.full_name())

# Solution 3

# class ElectriCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

# my_tesla = ElectriCar("Tesla", "Model S", "85kWh")

# print(my_tesla.model)
# print(my_tesla.full_name())

# Solution 4

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand + " !"

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
# private_car = Car("Toyota", "Corolla")
# print(private_car.__brand)   # __ made the brand private.

# Solution 5

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand + " !"

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"

# class ElectriCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"
    
# my_tesla = ElectriCar("Tesla", "Model S", "85kWh")
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())

# Solution 6

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1


    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
# safari = Car("Tata", "Safari")
# print(safari.total_car)
    
# These two are not okay to get access of total car variable.
    
# test = Car("test", "test")
# print(test.total_car)
    
print(Car.total_car)   # we can directly access the variables.
# Sometimes garbage collector dont clean immediately for optimisation purpose.
