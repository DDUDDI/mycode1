# 1. 100~200까지 순서대로 저장된 리스트를 생성한다
# 키보드에서 검색할 번호를 입력하면
# 해당 숫자가 리스트의 몇번째에 위치하는지 확인하여 그 인덱스를 화면에 출력한다
# 검색하려는 숫자가 리스트의 전반부에 있는지 후반부에 있는지 먼저 확인하여
# 해당 부분을 슬라이싱 적용하여 그 부분에서만 검색하도록 한다

import sys

srcList = list(range(100, 201))
mid = int(len(srcList)/2+1)
front = srcList[:mid]
end = srcList[mid:]

sNum = input('100~200 사이의 숫자를 입력하세요 : ')
iNum = int(sNum)

if iNum in front :
    idx = front.index(iNum)
    print(f'{iNum}의 위치는 {idx}입니다.')
    print('전반')
elif iNum in end :
    idx = end.index(iNum)
    print(f'{iNum}의 위치는 {idx+51}입니다.')
else :
    print('입력 오류 !')
    sys.exit()