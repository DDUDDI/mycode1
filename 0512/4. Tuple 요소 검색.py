# 4. Tuple에 5인 친구 이름을 입력하고 키보드에서 검색할 친구 이름을 입력하여
# 기존 Tuple에 존재하는지 확인하여 그 결과를 '회원이다', '회원이 아니다'로 출력하는 기능

nameTuple = ('김정연', '송하승', '방성환', '정성욱', '손주현') # Tuple은 () 사용
name = input('검색할 회원명을 입력해주세요 : ')

if name in nameTuple :
    print(f'{name}는(은) 회원이다')
else :
    print(f'{name}는(은)회원이 아니다')