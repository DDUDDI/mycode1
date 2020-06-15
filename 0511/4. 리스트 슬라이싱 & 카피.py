# 4. 리스트 Slicing & Copy

num = list(range(10, 0, -1)) # 10~1 리스트
print('원본 :', num)
num2 = num[2:] # 앞에서 3번째부터 끝까지 선택
print('Slice :', num2)

s = sum(num2)
print('Slice 합산 :', s)