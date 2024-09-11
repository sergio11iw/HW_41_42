class Car:
    def __init__(self, name):
        self.name = name
        self.color = 'red'
        self.fuel = 40
        self.rate = 10
        self.mileage = 0
    def drive(self, km):
        path = 100*self.fuel / self.rate
        if km <= path:
            self.fuel -= km / self.rate
            print(f'Мы проехали {km} км')
        else:
            self.fuel = 0
            print('Не хватает топлива')
    def get_mileage(self, km):
        return km


car1 = Car(name='Mini')
car1.drive(500)
print(car1.fuel)
car1.get_mileage(500)
print(km)
