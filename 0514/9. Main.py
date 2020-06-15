from car import Car

# instance의 주소가 Class에서 return 되어 기억됨
carList = [
    Car('tivoly', 2019, 1597, 'navy', 2033),
    Car('tivoly', 2019, 1597, 'navy', 2033),
    Car('tivoly', 2019, 1597, 'navy', 2033)
]

for car in carList:
    car.printinfo()