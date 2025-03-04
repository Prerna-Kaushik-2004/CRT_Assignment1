# Base class for all vehicles
class Vehicle:
    def __init__(self, model, make, year, base_rent):
        self.model = model
        self.make = make
        self.year = year
        self.base_rent = base_rent

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    def calculate_rent(self, days):
        return self.base_rent * days


class Car(Vehicle):
    def __init__(self, model, make, year, base_rent, num_doors, has_air_conditioning):
        super().__init__(model, make, year, base_rent)
        self.num_doors = num_doors
        self.has_air_conditioning = has_air_conditioning

    def get_info(self):
        air_conditioning_status = "with Air Conditioning" if self.has_air_conditioning else "without Air Conditioning"
        return f"{super().get_info()} - {self.num_doors} doors, {air_conditioning_status}"

    def calculate_rent(self, days):
        rent = super().calculate_rent(days)
        if self.has_air_conditioning:
            rent += 20  # Additional charge for AC
        return rent


class Bike(Vehicle):
    def __init__(self, model, make, year, base_rent, engine_capacity, has_helmet_included):
        super().__init__(model, make, year, base_rent)
        self.engine_capacity = engine_capacity
        self.has_helmet_included = has_helmet_included

    def get_info(self):
        helmet_status = "Helmet Included" if self.has_helmet_included else "Helmet Not Included"
        return f"{super().get_info()} - {self.engine_capacity}cc, {helmet_status}"

    def calculate_rent(self, days):
        rent = super().calculate_rent(days)
        if self.engine_capacity > 150:
            rent += 10  
        return rent


if __name__ == "__main__":
    car1 = Car("Model X", "Tesla", 2022, 50, 4, True)
    car2 = Car("Civic", "Honda", 2021, 40, 4, False)
    bike1 = Bike("Ninja ZX-6R", "Kawasaki", 2023, 30, 636, True)
    bike2 = Bike("Duke 200", "KTM", 2022, 20, 200, False)

  
    print(car1.get_info())
    print(bike1.get_info())

   
    days_rented = 5
    print(f"Rent for {car1.get_info()}: {car1.calculate_rent(days_rented)}")
    print(f"Rent for {bike1.get_info()}: {bike1.calculate_rent(days_rented)}")
