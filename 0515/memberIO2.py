from member import Member

filepath = 'D:/Pycharm_Projects/0515/members.txt'

def getMemberFromLine(line):
    info = line.split()
    m = Member(int(info[0]), info[1], info[2]) # int(info[0])
    if m:
        return m
    else:
        print(f'{line} 객체 변환 실패')
        return None