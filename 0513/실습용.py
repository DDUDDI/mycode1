# 11. 임의의 수를 함수에 전달하면 그 함수는 argument의 수를 화면에 표시한다.

import random as rd

def func(*a):
    print(len(a))


print(func(3, 4, 5))
