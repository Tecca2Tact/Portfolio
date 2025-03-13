class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.wheels = 4
        self.year = year

    def print_car(self):
        print(f"I am a {self.brand} {self.model} from {self.year}")

def main():
    camry = Car("Toyota", "Camry", "2018")
    camry.print_car()
    audi = Car("Audi", "R8", "2023")
    audi.print_car()
    infiniti = Car("Infiniti", "G35", "2008")
    infiniti.print_car()

if __name__ == '__main__':
    main()