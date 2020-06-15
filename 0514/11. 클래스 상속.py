# 12. Car 클래스를 상속하여 자식 클래스 HybridCar를 생성하려고 한다
# att: dist

from car import Car

# Car 클래스 상속
class HybridCar(Car):
    def __init__(self, type, year, disp, color, price, dist):
        super().__init__(type, year, disp, color, price) # 부모 클래스 생성자 이용
        self.dist = dist

    # method overriding: 부모 클래스의 method를 자식 클래스에서 재정의
    def printinfo(self):
        super().printinfo() # 부모 클래스 printInfo() 사용
        print(self.dist)



hybrid = HybridCar('volt', 2018, 3.0, 'blue', 2500, 200) # dist 출력 X
hybrid.printinfo() # Car class에서 printinfo method 상속