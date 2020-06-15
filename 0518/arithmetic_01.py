# 키보드에서 가감승제 계산식을 입력 받아서 해당 계산을 수행하고
# 그 계산식과 결과를 화면에 표시하는 기능을 작성하는데
# Atrithmetic이라는 클래스 안에 가감승제 기능을 정의한다.

class Arithmetic:

    def calculator(self, op, num1, num2): # def__init__ 반드시 해야하는 거 X
        num1 = int(num1.strip()) # 공백 제거
        num2 = int(num2.strip())
        res = 0
        if op == '+':
            res = num1 + num2
            return res
        elif op == '-':
            res = num1 - num2
            return res
        elif op == '*':
            res = num1 * num2
            return res
        elif op == '/':
            res = num1 / num2
            return res