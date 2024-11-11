mnum = 0 
msum = 0 
counter = 0
while True: 
    try:
        n = int(input('Введи целое число: ')) 
    except ValueError:
        print('Введенный символ не является целым числом')
        continue    
    if n == 0: 
        break 
    m = n 
    s = 0 
    counter += 1
    while n: 
        s += n % 10 
        n //= 10 
    if s > msum: 
        mnum = m 
        msum = s 
if counter > 0:
    print('Число с максимальной суммой цифр', mnum, 'Сумма цифр этого числа', msum)
