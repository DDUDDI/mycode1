# 3. 리스트 element의 합 구하기

import random as rd

list = []
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.sort()
print(list)
res = sum(list)
# sum(obj): list의 합 구하기
print(f'element의 합: {res}')
