# 3. Packing, Unpacking 이해하기

def getAvg(*nums):
    return sum(nums)/len(nums)

tp = (1, 2, 3, 4) # tuple
ns = [1, 2, 3, 4] # list

# getAvg(tp) # 튜플을 *nums에 전달하면 오류!
print(getAvg(*tp)) # 튜플을 Unpacking 하여 전달하면 OK
print(getAvg(*ns)) # 리스트도 Unpacking 하여 전달하면 OK