num = input('두 숫자를 입력해주세요 : ')
list = num.split()
num1 = list[0]
num2 = list[1]
res = int(num1) + int(num2)
msg = f'{num1} + {num2} = {res} 입니다.'
print(msg)
print(f'List: {list}\nnum1: {num1}\nnum2: {num2}')
