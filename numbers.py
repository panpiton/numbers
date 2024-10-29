mnum = 0
msum = 0

while True:
    n = int(input('Введи целое число: '))
    if n == 0:
        break
    m = n
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s > msum:
        mnum = m
        msum = s

print(f'Число с максимальной суммой цифр {mnum} Сумма цифр этого числа {msum}')