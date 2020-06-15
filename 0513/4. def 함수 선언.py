# 4. 로그인할 때마다 위의 함수를 호출하여 인사하는 기능을 작성해세요.
# def 함수 선언: 함수명을 호출하면 작성한 기능이 실행됨
# 반복 호출, 코드 절감을 위해 사용
'''
def 함수명(argument):
    ///////////////
함수명(parameter)
'''
def greet(user):
    # user = '강호동': 함수 내에서 user 값을 받는 것은 의미 X
    s = f'{user}님 환영합니다'
    print(s)

info = input('로그인(ID 공백 PWD) : ')
id = info.split()[0]
greet(id)

