# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiation(x, y):
    if y == 1:
        return x
    return exponentiation(x, y - 1) * x

print(exponentiation(int(input("Введите А: ")),int(input("Введите B: "))))