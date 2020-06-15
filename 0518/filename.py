dir = 'D:/Pycharm_Projects/0518/'

while True:
    userInput = input('파일명 혹은 종료(x): ')
    if userInput == 'x':
        break
    path = dir+userInput
    try:
        with open(path) as file:
            print(file.read()) # 파일 읽기
            break
    except FileNotFoundError:
        print('파일명을 확인해주세요.')

print('프로그램 종료')