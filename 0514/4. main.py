# 4. login() 호출
# from module_name import function_name as fn
# from module_name import *: module 내의 모든 function을 사용하겠다


from user import login
# from user import *

# import user

info = input('\t로그인 : ')
data = info.split()
# res 함수 호출, return loginOK 값을 res가 받음
# res = user.login(uid=data[0], pwd=data[1])
res = login(uid=data[0], pwd=data[1])
# 메세지 출력
msg = (f'\t[{data[0]}] 로그인 성공' if res else f'\t[{data[0]}] 로그인 실패')
print(msg)
###################################################################
print(login.memDic['kim']) # 오류 해결하기