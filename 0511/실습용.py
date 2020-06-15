# 8. 리스트에 0-9, A-Z, a-z까지 입력하고
# 그 리스트로부터 임의의 위치를 가져와서 암호문자열을 생성하는 기능을 작성하시오
# 암호 문자열은 문자 10개로 구성

import random as rd

src = []
for i in range(10) : # 0~9
    src.append(str(i))
for i in range(ord('A'), ord('Z')+1) : # A~Z
    src.append(chr(i))
for i in range(ord('a'), ord('z')+1) : # a~z
    src.append(chr(i))
print('리스트 :\n', src) # 암호 리스트

code = []
for i in range(10) : # 10개의 요소로 구성된 암호 만들기
    idx = rd.randint(0, len(src)-1) # 리스트 인덱스
    code.append(src[idx])

str = ''.join(code)
print('암호 리스트: \n', code)
print('암호 :', str)