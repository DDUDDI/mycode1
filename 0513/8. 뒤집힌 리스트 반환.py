# 8. 리스트를 받아서 리스트의 원소를 뒤집어서 리턴하는 기능을 작성

# 원본 뒤집음
def getList1(num1):
    num1.reverse()
    return num1

num1 = [1, 2, 3]
a = getList1(num1)
print(a)

# 원본 유지
def getList2(num2):
    res = num2[:] # 원본 복사
    res.reverse()
    return res

num2 = [1, 2, 3]
b = getList2(num2)
print(b)