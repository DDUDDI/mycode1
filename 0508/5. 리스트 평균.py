# 5. 리스트 element의 평균 구하기

import random as rd

list = []
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))
list.append(rd.randint(1, 100))

print(sorted(list))
msg = f'element의 평균 : {sum(list)/len(list)}' 
print(msg)
