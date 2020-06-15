# 1. 무작위 정수 50개를 추출하여 그 순서대로 화면에 출력한다
# 추출된 수 중에서 홀수만 골라서 화면에 출력한다
# 위에서 생성된 2개의 리스트를 내림차순으로 정렬하여 다시 출력한다

import random as rd

lis = []
odd = []

for i in range (0, 50) : # range (start, end+1)
    lis.append(rd.randint(1, 50)) # randint (start, end)
print(lis)
# 1부터 50사이의 무작위 정수 50개 추출

for i in range (0, 50) :
    if lis[i] % 2 != 0 :
        odd.append(lis[i])
print(odd)
# lis에서 홀수만 골라서 화면에 출력

        
print('\n====================출력 결과====================')
print('생성 리스트 :\n', sorted(lis, reverse=True)) # 내림차순 정렬
print('홀수 리스트 :\n', sorted(odd, reverse=True))


# 홀수만 출력하기 다른 코드
# for i in lis :
# if i %2 != 0 :
# odd.append(i)
