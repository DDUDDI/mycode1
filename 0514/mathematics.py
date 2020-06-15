# 7. mathematics라는 모듈 안에서 Math라는 클래스 안에
# add(), sub(), mul(), divide() method 정의
# Main 모듈에서 Math 클래스 사용

# Math class 생성
class Math:
    # 생성자(__init__): instance를 초기화하기 위해 사용
    def __init__(self, a, b): # self: instance의 주소, 여러개의 instance를 구별하기 위해 사용
        self.a = a
        self.b = b
    # method 생성
    def add(self):
        print(f'{self.a} + {self.b} = {self.a+self.b}')

    def sub(self):
        print(f'{self.a} - {self.b} = {self.a-self.b}')

    def mul(self):
        print(f'{self.a} * {self.b} = {self.a*self.b}')

    def divide(self):
        print(f'{self.a} / {self.b} = {self.a/self.b}')
