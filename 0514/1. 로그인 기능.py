# 1. 함수(function)을 이용한 로그인 기능 구현
# login(uid, pwd)라는 함수를 정의하고 이용자가 입력하는 정보를
# 이 함수에 전달하면 True/False를 리턴하여 로그인 성공여부를 판단하도록 한다.
# memDic에 미리 5명의 회원정보를 저장해 두고 로그인시 사용한다.
# 이 프로그램은 최종적으로 '[SMITH] 로그인 성공/실패'를 표시한다.


# 로그인 정보 생성
memDic = {'Kim': 'k1234',
          'Lee': 'l1234',
          'Jung': 'j1234',
          'Park': 'p1234',
          'Song': 's1234'
          }

# login 함수 정의
def login(uid, pwd):

    uid = uid.lower() # 소문자로 바꾸기
    loginOK = False
    if uid in memDic.keys() and pwd == memDic[uid]: # ID와 PWD가 일치하면
        loginOK = True
    else:
        loginOK = False
    return loginOK

# 로그인 정보 입력
info = input('로그인 : ')
data = info.split()
# res 함수 호출, return loginOK 값을 res가 받음
res = login(uid=data[0], pwd=data[1])
# 메세지 출력
msg = (f'\t[{data[0]}] 로그인 성공' if res else f'\t[{data[1]}] 로그인 실패')
print(msg)



