# 5. 리스트 나누기

import random

a = random.randint(0, 10)
b = random.randint(11, 20)
print(f'range : {a}, {b}')

nums = list(range(b, a, -1)) # b부터 a+1까지 역순
print('원본 :', nums)

idx = int((len(nums)/2)) # 중간 index 계산, int()로 실수->정수
pre = nums[:idx]
post = nums[idx:]

print('전반부 :', pre)
print('후반부 :', post)

pre.reverse() # 역순 출력, 값 return X
post.reverse()

print('전반부_reverse :', pre)
print('후반부_reverse :', post)