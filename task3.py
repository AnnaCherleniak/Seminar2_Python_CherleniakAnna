# 3. Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions


def sum_fractions(number1: str, number2: str):
    result = ''
    first_fraction = number1.split('/')
    second_fraction = number2.split('/')
    numerator = 0
    denominator = 0
    if first_fraction[1] == second_fraction[1]:
        numerator = int(first_fraction[0]) + int(second_fraction[0])
        denominator = first_fraction[1]
    else:
        first_fraction[0] = int(first_fraction[0]) * int(second_fraction[1])
        second_fraction[0] = int(second_fraction[0]) * int(first_fraction[1])
        numerator = first_fraction[0] + second_fraction[0]
        denominator = int(first_fraction[1]) * int(second_fraction[1])
        for d in range(int(numerator/2), 1, -1):
            if numerator % d == 0 and denominator % d == 0:
                numerator /= d
                denominator /= d
    result = str(int(numerator)) + '/' + str(int(denominator))
    return result


def multi_fractions(number1: str, number2: str):
    result = ''
    first_fraction = number1.split('/')
    second_fraction = number2.split('/')
    numerator = int(first_fraction[0]) * int(second_fraction[0])
    denominator = int(first_fraction[1]) * int(second_fraction[1])
    for d in range(int(numerator/2), 1, -1):
        if numerator % d == 0 and denominator % d == 0:
            numerator /= d
            denominator /= d
    result = str(int(numerator)) + '/' + str(int(denominator))
    return result


num1 = '8/10'
num2 = '8/20'
summ = sum_fractions(num1, num2)
print(summ)

f1 = fractions.Fraction(8, 10)
f2 = fractions.Fraction(8, 20)
print(f1 + f2)

multi = multi_fractions(num1, num2)
print(multi)
print(f1 * f2)
