# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.

# 2 2
# 4

def sum (a,b):
    result = a + b
    return result

print('Введите первое число:')
a = int(input())
print('Введите второе число:')
b = int(input())
result = sum(a,b)
print('результат:',sum(a,b))    