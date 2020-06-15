from calculator import Arithmetic


def getFomulafromLine(line):
    info = line.split()
    c = Arithmetic(info[0], info[1], info[2])
    if c:
        return c
    else:
        print(f'{line} 객체 변환 실패')
        return None


def inputNum():
    data = input('계산식 : ')
    c = getFomulafromLine(data)
    return c


def printResult(c):
    print(f'{c.num1} {c.operator} {c.num2} = {c.calculator()}')
