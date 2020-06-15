# 키보드에서 두 수를 받아서 앞의 수를 뒤의 수로 나눗셈을 하고 그 결과식을 화면에 표시한다.
# 만약에 이용자가 뒤의 수를 0으로 입력한다면 어떤 오류가 발생하는지 확인하고 오류를 해결해보세요.

while True:
    nums = input('나눗셈할 두 수를 입력하세요: ')
    divide = nums.split()
    num1 = int(divide[0])
    num2 = int(divide[1])


    try:
        msg = f'{num1} / {num2} = {num1/num2}'
    except ZeroDivisionError:
        print('0이 아닌 수를 입력해주세요.')
    else: # error가 안나면 else
        print(msg)
        break

print('프로그램 종료')
