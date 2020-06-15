# 3. 20~1 까지 화면에 표시

# 1) 내림차순 정렬
num = list(range(1, 21))
print(sorted(num, reverse=True))

# 2) reverse()
num2 = list(range(1, 21))
num2.reverse() # reverse()는 값 return X
print(num2)

# 3-1) reversed()
num3 = list(range(1, 21))
print(list(reversed(num3))) # reversed()는 값 return O


# 3-2) for문 + reversed()
lis = list(range(1, 21))
for i in reversed(lis) :
    print(i, end=' ')

# 4) list[::-1] : 역순으로 출력
num4 = list(range(1, 21))
print('\n', num4[20::-1])

# 5) step = -1 : 역순으로 출력
num5 = list(range(20, 0, -1))
print(num5)

'''다중행 문자열 만들기
    주석처럼 사용함'''