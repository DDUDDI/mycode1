# from arithmetic_01 import Arithmetic
from arithmetic_01 import *

arith = Arithmetic() # class 사용할 때 () 붙이기
ops = ['+', '-', '*', '/'] # operator을 list로 저장하여 loop 돌리기 편하게 함

exp = input('계산식 입력: ')
#print(f'{exp}={eval(exp)}') # eval(): string을 산술식으로 계산
completed = False
for op in ops: # 연산자가 무엇이 들었는지 확인
    try:
        exp.index(op) # error나면 excpet로 감, 문자열도 index로 접근 가능
        token = exp.split(op) # 연산자를 중심으로 split
        print(f'{token[0]} {op} {token[1]} = ' # token[0] = num1, token[1] = num2
              f'{arith.calculator(op, token[0], token[1])}')
        completed = True
    except ValueError as ve:
        continue # 반복문을 다시 시작해라

if not completed: # completed = False
    print('계산식 입력 오류')
