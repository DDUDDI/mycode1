numbers = list(range(1, 6)) # 리스트 쉽게 만들기
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for i in range(1, 11) :
    squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(1, 11)] # List comprehensions
print(squares2)
