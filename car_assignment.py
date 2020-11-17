#car comparison 

class Car:
    def __init__(self,model,speed,tank_capacity,fuel_usage):
        self.model = model
        self.speed = speed
        self.tank_capacity = tank_capacity
        self.fuel_usage = fuel_usage 

#maximum distance of a car ride  1 km 
    def distance(self) -> float:
        per_km = 100/ self.fuel_usage * self.tank_capacity
        return per_km

#maximum duration
    def maximum_duration(self) -> float:
        return distance()/self.speed * 60

#car comparison 
    def is_better_than(self, other_car):
        if self.distance() > other_car.distance() and self.maximum_duration() > other_car.maximum_duration:
            return "yes"
        elif self.distance > other_car.distance() or self.maximum_duration() > other_car.maximum_duration:
            return "maybe"
        else:
            return "no"

        def compare_cars(self, other_company):
            for c in other_company.cars:
                if self.is_better_than(c)== "yes":
                    self.counter += 1
        print(f" Our car, {self.model} is better than {self.counter} out of {(other_company.car)} of all the cars in the company.")

class Company:
        
        def __init__(self, name, car):
            self.name = name
            self.car = car 

    
car1 = Car("Model S", 50, 37, 8.5)
car2 = Car("Model 3", 45, 40, 10.2)
car3 = Car("Model X", 55, 46, 7.9)
car4 = Car("Rock", 50, 45, 9.4)

company1 = Company("Tebsla", [car1, car2, car3])

print(car4.is_better_than(car1)) # Prints "yes"
print(car2.is_better_than(car3)) # Prints "no"
print(car1.is_better_than(car2)) # Prints "maybe"
print(car4.compare_cars(company1)) 






