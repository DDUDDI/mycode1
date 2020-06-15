# 7. 소문자 5개로 이루어진 문자열 만들기

print('a 코드 :', ord('a'))
print('b 코드 :', ord('z'))

import random

charList = []
numList = []

for i in range(5) :
    num = random.randint(97, 122)
    numList.append(num)
    char = chr(numList[i])
    charList.append(char)

str = ''.join(charList)
# '': 문자열, obj.join(): 리스트->문자열
# cf. obj.split(): 문자열->리스트

print(f'\n문자열 리스트 : {charList}')
print(f'문자열 : {str}')

# 선생님 코드
'''for i in range(5) :
    tmp = rd.randint(97, 122)
    charList.append(chr(tmp))'''