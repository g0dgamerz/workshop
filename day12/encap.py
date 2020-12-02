class Vehicle:
    def __init__(self):
        self.color="red"
        self._mileage=99 #protected attribute

    def change_mileage(self):
        self._mileage =0

my_vehicle=Vehicle()
print(f'Before ==> color= {my_vehicle.color}',f'mileage={my_vehicle._mileage}')
#modify color and _mileage attribute
my_vehicle.color="blue"
#protected attributes can be modified
my_vehicle._mileage=25
print(f'After==> color = {my_vehicle.color}',f'mileage={my_vehicle._mileage}')
#output
Before ==> color= red mileage=99
After==> color = blue mileage=25