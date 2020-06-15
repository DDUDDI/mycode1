# 키보드에서 가감승제 계산식을 입력 받아서 해당 계산을 수행하고
# 그 계산식 결과를 화면에 표시하는 기능을 작성하는데
# Atrithmetic이라는 클래스 안에 가감승제 기능을 정의한다
import sys
# 내가 한거 #
class Arithmetic():

    def __init__(self, num1, operator, num2):
        self.num1 = int(num1)
        self.operator = operator
        self.num2 = int(num2)

    def calculator(self):
        try:
            if self.operator == '+':
                res = self.num1 + self.num2
                return res
            elif self.operator == '-':
                res = self.num1 - self.num2
                return res
            elif self.operator == '*':
                res = self.num1 * self.num2
                return res
            elif self.operator == '/':
                res = self.num1 / self.num2
                return res
        except Exception:
            print('연산자 오류')
            sys.exit()