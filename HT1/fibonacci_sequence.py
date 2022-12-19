#! python
def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def find_prime_number(n):
    while n >= 2:
        if prime_number(n) == 1:
            return n
        else:
            n -= 1

def fibonacci(f1, f2):
    print(f1, f2, '', end='')
    for i in range(3, 16):
        f = f1 + f2
        f1 = f2
        f2 = f
        print(f2, '', end='')

print('Please, enter an integer number')
numb = int(input())
if numb <= 2:
    print('Number must be greater than 2')
else:
    fib_2 = find_prime_number(numb)
    fib_1 = find_prime_number(fib_2 - 1)
    fibonacci(fib_1, fib_2)


