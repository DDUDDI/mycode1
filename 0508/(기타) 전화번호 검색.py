nameList = ['김정연', '송하승', '방성환', '정성욱', '손주현']
phoneList = ['010-8960-9185', '010-3194-4875', '010-5097-7678', '010-4361-8876', '010-4123-4608']
# 리스트 생성

phone = input('친구 번호 : ')

if phone in phoneList :
# List에 특정 element가 있는지 체크하기
    num = phoneList.index(phone)
    # List.index(element): List에서 원하는 element의 위치 찾기
    name = nameList[num]
    msg = f'[{phone}]은(는) {name}의 번호입니다.'
    print(msg)
else :
    print('해당 번호 정보가 없습니다.')
