# 로그인 시스템을 작성할 때 ID가 'Smith'이고 암호는 '0000'인 경우에만
# True를 출력하고 그 외에는 False를 리턴하는 기능을 작성하시오.

# ID = input('ID : ')
# pwd = input('PASSWORD : ')
data = input('ID와 PASSWORD를 입력하세요: ').split()
# print(data)
# print(data[0])
# print(data[1])
print((data[0] == 'Smith' and data[1] == '0000'))
