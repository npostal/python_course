#  Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.


a = int(input("Введите значение: ")) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
# 987, 1597, 2584, 4181, 6765, 10946, 17711,

first = 0
second = 1
third = first + second
count = 3
while third < a:
    first = second
    second = third
    third = first + second
    count += 1
if third == a:
    print(count)
else:
    print(-1)