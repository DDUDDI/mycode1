# 전화번호 등록

nameList = ['김정연', '송하승', '방성환', '정성욱', '손주현']
phoneList = ['010-8960-9185', '010-3194-4875', '010-5097-7678', '010-4361-8876', '010-4123-4608']

name = input(f'친구 이름을 입력하세요 : ')
phone = input(f'친구 번호를 입력하세요 : ')

nameList.append(name)
phoneList.append(phone)

print(nameList[len(nameList)-1])
