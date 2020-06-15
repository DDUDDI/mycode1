# 키보드에서 2명의 회원정보(num, name, phone)을 받아서
# 딕셔너리에 저장하고 회원정보를 [{},{},...] 형식으로 생성한 후에
# 파일에 저장할 때 json 문자열 형식으로 저장한다.
# 다시 파일에서 읽어올 때는 json 문자열을 딕셔너리 형식으로 읽어서 사용한다.

import json
import os.path

from jsonIO import *

def showMenu():
    m = input('회원정보 추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ')
    return m

while True:
    m = showMenu()
    if m == 'a':
        addMem(inputMem())
    elif m == 's':
        printMemList(readMemList())

        '''
        
    elif m == 'f':
        # 회원정보 검색
    elif m == 'u':
        # 회원정보 수정
    elif m == 'd':
        # 회원정보 삭제
    elif m == 'x':
        # 프로그램 종료
'''
