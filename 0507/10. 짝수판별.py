# 임의의 정수를 추출하여 그 수가 짝수인지 식별하여 그 결과를 화면에 표시하시오.

import random
num = random.randint(1, 100)
# import random as rd
# num = rd.radint(1, 100)
res = (num%2==0)
msg = f'"{num}"은(는) 짝수인가? : {res}'
# {} 에는 표현식(변수, 함수 등)이 올 수 있음
print(msg)

# if 문을 사용한 짝수 판별
# x = random.randint(1, 100)
# if (x%2==1) :
#    print(f'{x}는 홀수')
# else :
#    print(f'{x}는 짝수')
