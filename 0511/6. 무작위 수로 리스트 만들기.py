# 6. 무작위 수를 구하고 그 수만큼의 원소를 가진 리스트 생성
# 그 리스트의 뒤에서 3번째부터 끝까지 복사해서 리스트 출력

import random

a = random.randint(10, 20)
num1 = []

for i in range(a) : # 원소가 a개인 리스트 생성
    num1.append(random.randint(0, 20)) # 리스트 값은 0~20사이의 정수
print('원소의 개수 :', a)
print('원본 리스트 :', num1)

num2 = num1[-3:] # 뒤에서 3번째부터 끝까지
print('마지막 3개의 원소들 :', num2)

