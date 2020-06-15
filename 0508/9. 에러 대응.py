nameList = ['김정연', '송하승', '방성환', '정성욱', '손주현']
phoneList = ['010-8960-9185', '010-3194-4875', '010-5097-7678', '010-4361-8876', '010-4123-4608']

choice = input('\n친구 번호(1), 이름(2) 입력 : ')
# 번호 or 이름 검색 선택
if choice == '1' :
    num = input('\n친구 번호를 입력해주세요 : ')
    # 친구 번호 입력
    name = nameList[int(num)-1]
    phone = phoneList[int(num)-1]
     # List에서 index(친구 번호-1) 위치의 이름, 번호 찾고 변수에 저장
elif choice == '2' :
    name = input('\n검색할 이름을 입력해주세요 : ')
    try :
        idx = nameList.index(name)
        # 에러 발생이 예상되는 코드
    except Exception as e :
        print('검색 결과가 없습니다.')
        # 에러 대응 코드
         # ValueError를 통해 에러 발생 원인 검토 가능
        sys.exit() # 프로그램 종료    
    phone = phoneList[idx]

msg = f'\n★ 친구 조회 결과 ★\n이름 : {name}\n번호 : {phone}'
print(msg)
