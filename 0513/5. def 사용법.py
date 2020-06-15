# 5. def 사용법

def average(records): # 값 외부->함수
    total = 0
    for p in records:
        total += p
    avg = total/len(records)
    # print('평균 : ', avg)
    return avg # return: 값 함수->외부, * 정보를 준 곳으로 내보냄

a = average([10, 20, 30, 100])
print(a) # return avg 받아서 출력