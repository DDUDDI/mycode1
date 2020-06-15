# 2. 리스트 요소를 오름차순으로 정렬하기

import random as rd

list = []
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.sort()
# list.sort(): 리스트 정렬
# asc: list.sort(); desc: list.sort(reverse=True) or list.reverse()
print(list)
print(sorted(list))
# list.sort():  기존의 리스트를 변경하여 정렬 후 값을 return 하지 않음
# #원본 변경이 문제가 되는 경우, 다른 method 사용 필요
# sorted(): 기존의 리스트를 변경하는 것이 아니라 정렬된 새로운 리스트 반환

