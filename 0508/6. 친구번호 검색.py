# 6. 전화번호 '검색'
# nameList에 친구 이름 5개 저장
# phoneList에 전화번호 5개 저장
# 키보드에서 '번호로 검색: 2'와 같이 입력하면 2번 친구의 이름과 전화번호를 화면에 표시한다.

nameList = ['김정연', '송하승', '방성환', '정성욱', '손주현']
phoneList = ['010-8960-9185', '010-3194-4875', '010-5097-7678', '010-4361-8876', '010-4123-4608']

num = input(f'번호로 검색 : ')
name = nameList[int(num)-1]
phone = phoneList[int(num)-1]

msg = f'★ {num}번 친구 ★\n이름 : {name}\n번호 : {phone}'
print(msg)
