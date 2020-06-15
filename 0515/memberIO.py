# member Module에서 Member Class를 사용
from member import Member

# 텍스트 파일 경로
filepath = 'D:\Pycharm_Projects\0515\member.txt'

def getMemberFromLine(line):
    info = line.split()
    m = Member(int(info[0]), info[1], info[2])
    if m:
        return m
    else:
        print(f'{line} 객체 변환 실패')
        return None

def getList():
    # 텍스트 파일 열기
    # with문을 사용하지 않을 경우, 파일 닫기를 스스로 해줘야 하므로 비추
    with open(filepath) as file:
        lines = file.readlines() # 파일의 라인별로 리스트 형태로 return
    memList = []
    for line in lines:
        memList.append(getMemberFromLine(line)) # 각 line을 instance로 만든 것을 memList에 저장
    return memList

# member 출력
def printMemList(memList):
    for m in memList:
        m.info() # Member class의 info method

# member 입력
def inputMem():
    data = input('번호 이름 전화 : ')
    m = getMemberFromLine(data)
    return m

# 파일에 member 추가
def addMem(m):
    with open(filepath, 'a') as file: # a: 이어쓰기, r: 읽기, w: 쓰기, +: 읽기+쓰기
        file.write(f'{m.num} {m.name} {m.phone}\n') # 파일에 추가하기
    print('추가 성공!')

def inputName():
    name = input('검색할 회원명 : ')
    return name

# 이름으로 조회
def searchMem(name):
    with open(filepath) as file:
        lines = file.readlines()
    for line in lines:
        if line.split()[1] == name:
            m = getMemberFromLine(line)
            m.info()
            break

def update():
    data = input('수정할 회원명과 새 전화번호 : ')
    info = data.split()
    memList = getList() # getList() method의 return 값 저장
    for m in memList:
        if m.name == info[0]:
            m.phone = info[1]
            break
    writeMemList(memList)

def writeMemList(memList):
    with open(filepath, 'w') as file:
        for m in memList:
            line = f'{m.num} {m.name} {m.phone}'
            file.write(line+ '\n') # line+
    print('전체 다시 쓰기 성공')

def delete():
    name = input('삭제할 회원명 : ').strip() # 공백 제거
    memList = getList()
    for m in memList:
        if m.name == name:
            memList.remove(m)
            break
    writeMemList(memList)