# json 모듈을 사용하여 메모리에 존재하는 딕셔너리와 문자열 변환을 수행해보세요.
# dumps(), loads()
# 파일 열고 닫는것 없이 바로 메모리에 write & read

import json

Dic = {'num': '1',
       'name': '김지희',
       'phone': '010-8285-2415'}

# json.dumps()
Dic_json = json.dumps(Dic) # argument 1개
print(Dic_json, type(Dic_json)) # type: string

# json.loads()
printDic = json.loads(Dic_json)
print(printDic['name'])

print('프로그램 종료')