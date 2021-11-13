print('Please, enter an integer number')
numb = int(input())
if numb <= 1:
    print('Please, enter an integer number more than 1')
else:
    print('Prime divisors of number are:')
for i in range(2, numb):
    while (numb % i) == 0:
        print(i, '')
        numb /= i
if numb != 1:
    print(numb)
