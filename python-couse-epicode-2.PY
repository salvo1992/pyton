class Car: 
    wheels = 4
    total_built_car = 0
    total_drove_km = 0

    def __init__(self, band,max_speed,year,is_electric):
        self.band = band
        self.max_speed = max_speed
        self.year = year
        self.is_electric = is_electric
        Car.total_built_car +=1

    def drive(self,kilometers):
        print(f"La{self.band} guida per {kilometers} chilometri")
        Car.total_drove_km +=kilometers
    def __str__(self):
        return f"Sono un bellissima {self.brand} del {self.year}"
    
    
car1 = Car("fiat",200.0, 2020, True)
car2 = Car("ferrari", 300.0, 2010, False)

#car1.drive(50)
#car1.drive(100)
#car1.drive(150)

#car1.total_drove_km = 0

#print(car1.total_drove_km)

#setattr(car1, "is_electric", False)
print(car1.is_electric)
