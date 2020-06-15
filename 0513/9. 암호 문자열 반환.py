# 9. 정수 한개를 전달하면 그 숫자만큼의 문자로 구성된 임의의 문자열을 리턴하라

import random as rd

def getstr(a):
    src = []
    for i in range(a): # a-z: 97-122
        x = rd.randint(97, 122) # 97-122 임의의 수 생성
        src.append(chr(x)) # chr(a): 숫자->문자
    code = ''.join(src) # ''.join(src): list->string
    return code

code = getstr(10)
print(code)

