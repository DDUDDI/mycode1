# 키보드에서 아이디와 암호를 입력 받아서 그 2개의 문자열을 다음과 같은 서식을 사용하여 표시하시오.
# 서식(Formatted String) ID : [아이디] / PWD : [암호]


ID = input('ID 입력 : ')
pwd = input('PASSWORD 입력 : ')
message = f"ID : [{ID}] / PWD : [{pwd}]"
print(message)

# 여러개의 string 입력 받기 split()

ID, pwd = input('ID와 PASSWORD를 입력해주세요(ID, PASSWORD) : ').split()
message = f"ID : [{ID} / PWD : [{pwd}]"
print(message)
