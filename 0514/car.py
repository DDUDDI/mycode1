# 8. Car 클래스(클래스는 Att와 method로 이루어진다)
# 객체의 속성(Attributes): 차종, 연식, 배기량, 색상, 가격
# method(실물 객체의 기능): printinfo() -> 5개의 속성을 화면에 표시하는 기능

class Car:
    # class 변수, static 변수, class명.class변수
    # 객체 소속 X, 건드릴 수 없음, 모든 객체가 동일한 값을 가지는 경우 사용(for 메모리 절약)
    company = '현대 자동차'
    def __init__(self, type, year, disp, color, price):
        self.type = type # 객체 내에 존재하는 instance 변수, 동적 변수, instance명.instance변수(method명명
        self.year = year
        self.disp = disp
        self.color = color
        self.price = price

    def printinfo(self):
        print(f'\t{self.type}', end='\t')
        print(f'\t{self.year}', end='\t')
        print(f'\t{self.disp}', end='\t')
        print(f'\t{self.color}', end='\t')
        print(f'\t{self.price}', end='\t')