# class는 메모리에 load하는 instantiation(객체화) 과정을 거쳐야 사용할 수 있음
# file(in disk)->instance(in memory)
'''
def__init__(self, name, age):
    self.name = name # self.name = instance 변수
    self.age = age
'''
# 6. 클래스 명: Greeting
#    method: greet()
#    - 이 method가 호출되면 객체 내부에 저장된 회원의 이름 뒤에
#    - '환영합니다'라는 문장이 출력되도록 하시오.

class Greeting:

    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f'{self.name}님 환영합니다.')

