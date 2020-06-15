# 1. 로그인 기능
# 메모리에 회원의 ID, PWD를 미리 준비해놓고 키보드에서 입력하여 로그인을 수행하는 기능을 작성한다.
# Dictionary에 아이디와 암호를 저장할 때 영문 대문자를 사용하며,
# 로그인할 때는 대소문자를 가리지 않고 사용해도 기능이 문제없이 작동하도록 한다.

# Dictionary에 ID, PWD 저장
info = {'KIM':'AAAA', 'LEE':'BBBB', 'JUNG':'CCCC'}

# ID, PWD 입력
ID = input ('ID : ')
PWD = input ('PWD : ')

# 선생님 코드
'''
login = input('로그인 : ')
inList = login.split()
ID = inList[0]
PWD = inList[1]
'''

# ID가 key 값으로 있는지 확인
if ID.upper() not in info.keys():
    print(f'{ID}은(는) 존재하지 않는 ID입니다.')
else:
    # ID와 PWD가 일치하는지 확인
    if info[ID.upper()] == PWD.upper():
        print('로그인이 완료되었습니다.')
    else:
        print('비밀번호가 일치하지 않습니다.')

# 선생님 코드
 '''
 loginOK = False
 if ID.upper in info.keys():
    if info[ID.upper()] == PWD.upper():
        login = True
 msg = '로그인 성공' if loginOK else '로그인 실패' # Ternary Operator(3항 연산자)
 print(msg)
 '''