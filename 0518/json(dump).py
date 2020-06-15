# Dictionary 생성: 회원번호, 이름, 전화
# 완성된 딕셔너리를 json을 이용해 파일에 저장
# 다시 json을 이용하여 저장된 파일을 읽어서(load) 화면에 표시

import json
# json(): share data between different Python programs
# JavaScript의 object이지만 python에서 dictionary로 사용 가능
# json.dump: 매체는 하드디스크에 저장되는 file

Dic = {'num': '1',
       'name': '김지희',
       'phone': '010-8285-2415'}

# json.dump()
filename = 'list.txt'
with open(filename, 'w') as filewrite:
    json.dump(Dic, filewrite) # 딕셔너리 객체는 json의 string 형식으로 변환되어 파일에 저장됨

# json.load()
with open(filename) as fileread:
    printDic = json.load(fileread) # json string을 읽어서 딕셔너리 객체로 리턴한다
print(printDic['name'])

print('프로그램 종료')

