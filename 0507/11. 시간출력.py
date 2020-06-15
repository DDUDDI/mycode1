# 파이썬 코드를 사용하여 오늘의 날짜를
# 년-월-일-요일 시:분:초 포맷으로 출력해보세요.

import datetime
x = datetime.datetime.now()
y = x.strftime('%w')
t = ['월', '화', '수', '목', '금', '토', '일']
n = t[int(y)]
time = f'{x.year}-{x.month}-{x.day}-{n}요일 {x.hour}:{x.minute}:{x.second}'
print(time)        
print(x.strftime('%Y-%m-%d-%a %H:%M:%S'))

# 출력 포맷 바꾸기
minute=x.strftime('%M')
second=x.strftime('%S')

time2 = f'{x.year}-{x.month}-{x.day}-{n}요일 {x.hour}:{minute}:{second}'
print(time2)

