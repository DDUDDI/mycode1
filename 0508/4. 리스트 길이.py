# 4. 리스트 element의 개수(길이) 구하기

import random as rd

list = []
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))

print(sorted(list))
print(len(list))
# len(list): list의 길이 구하
