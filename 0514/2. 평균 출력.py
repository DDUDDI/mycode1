# 2. 임의의 갯수의 정수를 어떤 함수에 전달하면
# 호출된 함수는 그 정수들의 평균을 구해서 출력하는 기능

# 가변 매개변수
# *a : packing(argument)->Tuple
def getAvg(*a):
    # print(*a) # unpacking: *붙인 곳에 또 *붙임, 낱개의 데이터로 추출됨
    # print([*a]) # 낱개->List
    return sum(a)/len(a)

avg = getAvg(1, 2, 3, 4)
print('평균 : ' avg)

# 문제 잘못 이해함
'''
import random as rd

def getAvg(a):
    numList = []
    for i in range(a):
        numList.append(rd.randint(0, 100))
    total = sum(numList)
    avg = total/int(a)
    return avg

x = rd.randint(0, 10)
res = getAvg(x)
print(f'\t평균 : {res}')
'''