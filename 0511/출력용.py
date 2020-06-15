# 2. remove()를 이용한 구현
# remove(x) : 리스트에서 첫 번째로 나오는 x를 삭제하는 함수

import random as rd

lis = []

print('추출된 원본')
for i in range (0, 50) : # range (start, end+1)
    lis.append(rd.randint(1, 50)) # randint (start, end)
print(lis)
# 1부터 50사이의 무작위 정수 50개 추출

lis2 = [] # nums -> nums2 복사
for i in lis :
    lis2.append(i)

even = [] # 짝수만 찾아서 따로 저장    
for i in range (0, 50) :
    if lis[i] % 2 == 0 :
        even.append(lis[i])

for i in even : # 짝수를 제거한다
    lis.remove(i)
    
print('\n\n원본 리스트를 내림차순으로 정렬한 결과')

lis2.sort(reverse=True)
print(lis2)

print('\n\n홀수 내림차순')
lis.sort(reverse=True)
print(lis)
