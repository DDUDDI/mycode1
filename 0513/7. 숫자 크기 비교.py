# 7. 숫자 2개의 크기를 비교 하고 작은 수가 먼저 출력되록 하라

import random as rd

def compare(a, b): # positional parameter
    if a<b:
        print(a, b)
    else:
        print(b, a)

# positional argument
compare(rd.randint(0, 100), rd.randint(0, 100))
# keyword argument
compare(b=rd.randint(0, 100), a=rd.randint(0, 100))
