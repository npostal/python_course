# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

N = (int(input('Введите число N ')))
stop = 0
a = 2
for i in range(N):
    if stop != 1:
        P = a ** i
        if P <= N:
            print(P, end=' ')
            P = 2
        else:
            stop = 1
    else:
        i = N