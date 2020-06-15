# 간단한 계산기 프로그램
# 키보드에서 두 정수를 받아서 그 두수를 더하고
# 화면에는 덧셈식과 함께 그 결과를 표시하시오

a = int(input('첫번째 숫자 : '))
b = int(input('두번째 숫자 : '))
c = int(a) + int(b)
message = f"결과 : {a} + {b} = {c}"
print(message)

# 여러개의 숫자 한 번에 입력받기 map
num1, num2 = map(int, input('두 개의 숫자를 입력해주세요: ').split())
res= int(num1) + int(num2)
message = f"{num1} 더하기 {num2}는 {res}입니다."
print(message)
