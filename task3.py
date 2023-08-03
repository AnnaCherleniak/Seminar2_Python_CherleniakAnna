# 3. Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

def sum_fractions(number1: str, number2: str):
    result = ''
    first_fraction = number1.split('/')
    second_fraction = number2.split('/')
    numerator = 0
    denominator = 0
    if first_fraction[1] == second_fraction[1]:
        numerator = int(first_fraction[0]) + int(first_fraction[0])
        denominator = first_fraction[1]
        result = str(numerator) + '/' + denominator

    return result


num1 = '5/7'
num2 = '3/7'
summ = sum_fractions(num1, num2)
print(summ)
# multi
