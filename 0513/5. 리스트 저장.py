# 6. 함수를 호출하면 항상 임의의 수 5개가 입력된 리스트가 return 되도록 하라

import random as rd

# 임의의 수 5개를 리스트에 저장하는 함수
def getnums():
    nums = []
    for i in range(5):
        tmp = rd.randint(0, 100)
        nums.append(tmp)
    return nums

res = getnums()
print(res)