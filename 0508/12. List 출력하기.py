# 12. for문으로 List 출력하기

nameList = ['김정연', '송하승', '방성환', '정성욱', '손주현']
phoneList = ['010-8960-9185', '010-3194-4875', '010-5097-7678', '010-4361-8876', '010-4123-4608']
name = []
phone = []
for i in range(0, len(nameList)) :
    name = nameList[i]
    phone = phoneList[i]
    print(f'이름 : {name}, 번호 : {phone}')

# 더 간단하게
# for i in range(0, len(nameList)) :
#    print(f'{nameList[i]} : {phoneList[i]}')
