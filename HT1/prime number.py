def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

print('Please, enter an integer number')
numb = int(input())
if numb <= 2:
    print('Number must be greater than 2')
numb -= 1
while numb >= 2:
    if prime_number(numb) == 1:
        print('Maximum prime number less than the entered number =', numb)
        break
    else:
        numb -= 1