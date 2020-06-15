nameList = ['김정연', '송하승', '방성환', '정성욱', '손주현']
phoneList = ['010-8960-9185', '010-3194-4875', '010-5097-7678', '010-4361-8876', '010-4123-4608']
# 리스트 생성

phone = input('친구 번호 : ')

if phone in phoneList :
    print('phone')
    num = phoneList.index(phone)
    name = nameList[num]
    msg = f'[{phone}]은(는) {name}의 번호입니다.'
    print(msg)
else :
    print('해당 번호 정보가 없습니다.')

#if phone in phoneList :
 #   name = nameList[num]
  #  msg = f'[{phone}]은(는) {name}의 번호입니다.'
   # print(msg)
#elif phone not in phoneList :
 #   print('해당 번호에 맞는 친구 정보가 없습니다.')
#else :
 #   print('다시 입력')

#if num in range(0, len(nameList)) :
 #   name = nameList[num]
  #  msg = f'[{phone}]은(는) {name}의 번호입니다.'
   # print(msg)
#elif num not in range(0, len(nameList)) :
 #   print('해당 번호에 맞는 친구 정보가 없습니다.')
#else :
 #   print('입력 오류 !')
