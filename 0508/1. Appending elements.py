# 1. 빈 리스트를 생성하고 그 안에 임의의 정수 3개를 저장, 출력해보세요.
# obj.append(): 리스트 끝에 새로운 element 추가

import random as rd

list = []
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))

print(list)
