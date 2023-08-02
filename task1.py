# 1. Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

MULTIPLICITY = 50
PERCENT_WITHDRAWAL = 1.5
MIN_SUM_PERCENT = 30
MAX_SUM_PERCENT = 600
LIMIT_TRANSACTION = 3
PERCENT_FOR_TRANSACTION = 3

summ = 0
count_replenishment = 0
count_withdrawal = 0

while True:
    action = input('Ваше действие? Нажмите п - если хотите ПОПОЛНИТЬ,\n'
                   'Нажмите с - если хотите СНЯТЬ,\n'
                   'Нажмите в - если хотите ВЫЙТИ,\n')
    if action == 'п':
        temp = int(input(f'сумма пополнения, кратно {MULTIPLICITY}: '))
        if temp % MULTIPLICITY != 0:
            continue

        sum_for_replenish = 0
        count_replenishment += 1
        if count_replenishment == LIMIT_TRANSACTION:
            count_replenishment = 0
            sum_for_replenish = round(temp * PERCENT_FOR_TRANSACTION / 100)

        summ += (temp - sum_for_replenish)
        print(f'Остаток денег на счету - {summ}')
    elif action == 'с':
        temp = int(input(f'сумма снятия, кратно {MULTIPLICITY}: '))
        if temp % MULTIPLICITY != 0:
            continue

        sum_percent_withdrawal = round(temp * PERCENT_WITHDRAWAL / 100)
        if sum_percent_withdrawal < MIN_SUM_PERCENT:
            sum_percent_withdrawal = MIN_SUM_PERCENT
        elif sum_percent_withdrawal > MAX_SUM_PERCENT:
            sum_percent_withdrawal = MAX_SUM_PERCENT

        sum_for_withd = 0
        count_withdrawal += 1
        if count_withdrawal == LIMIT_TRANSACTION:
            count_withdrawal = 0
            sum_for_withd = round(temp * PERCENT_FOR_TRANSACTION / 100)
        
        if (temp + sum_percent_withdrawal + sum_for_withd) > summ:
            print('Недостаточно средств для снятия!')
            continue
        
        summ -= (temp + sum_percent_withdrawal + sum_for_withd)
        print(f'Остаток денег на счету - {summ}')
    elif action == 'в':
        print(f'Остаток денег на счету - {summ}')
        break
