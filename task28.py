# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

def sum(a, b):
    count = 0
    if a == 0:
        return b
    return sum(a - 1, b) + 1

print(sum(int(input("Введите a: ")), int(input("Введите b: "))))