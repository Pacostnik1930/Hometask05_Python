# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. 
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def  degree(a,b):
    result = a**b
    return result


print('Введите число:')
a = int(input())
print('Введите степень,в котрую будем возводить число:')
b = int(input())
result = degree(a,b)
print('результат:',degree(a,b))