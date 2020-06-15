# 연-월-일, 시:분:초
# 이와 같은 포맷으로 1초마다 화면에 시간을 표시한다

import time
# sleep(sec): 현재 동작 중인 프로세스를 주어진 초만큼 정지
# strftime(format, [, t]): 사용자가 정의한 문자열을 struct_time 객체로 변환
# localtime(): 현재 시간
while True:
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 시스템(현재) 시간은 따로 받지 않아도 됨
    time.sleep(1)
    print(now)

'''
선생님 코드
go = True
while go:
    date = time.strftime('%Y-%m-%d')
    hour = time.strftime('%H-%M-%S')
    print(f'{date}, {hour})
    time.sleep(1)
'''
