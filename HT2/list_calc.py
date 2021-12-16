import math


def add(l):
    result = [0] * len(l[0])
    for i in l:
        for j in range(len(i)):
            result[j] += i[j]
    return result


def sub(l):
    result = [0] * len(l[0])
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0:
                result[j] = l[i][j]
            else:
                result[j] -= l[i][j]
    return result


def mult(l):
    result = [0] * len(l[0])
    print(result)
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(i, j)
            if i == 0:
                result[j] = l[i][j]
            else:
                result[j] *= l[i][j]
    return result


def div(l):
    result = [0] * len(l[0])
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0:
                result[j] = l[i][j]
            else:
                if l[i][j] != 0:
                    result[j] /= l[i][j]
                else:
                    print('Введено недопустипое значение')
                    result[j] = False
    return result


def pow(l):
    result = [0] * len(l[0])
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0:
                result[j] = l[i][j]
            else:
                result[j] **= l[i][j]
    return result


def sqrt(l):
    result = [[0] * len(l[0]) for i in range(len(l))]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] >= 0:
                result[i][j] = l[i][j] ** 0.5
            else:
                print('Введено недопустипое значение, корень из отрицательных чисел не определен')
                result[i][j] = False
    return result


def log(l, base):
    if base > 0 and base != 1:
        result = [[0] * len(l[0]) for i in range(len(l))]
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] > 0:
                    result[i][j] = math.log(l[i][j], base)
                else:
                    print('Введено недопустипое значение')
                    result[i][j] = False
    else:
        print('Введено недопустимое основание логарифма')
    return result


if __name__ == '__main__':
    st = input().split()
    lst = []
    while ('/' not in st) and ('*' not in st) and ('-' not in st) and ('+' not in st) and ('log' not in st) and (
            '**' not in st) and ('sqrt' not in st):
        for j in range(len(st)):
            st[j] = int(st[j])
        lst.append(st)
        st = input().split()

    max_len = 0
    for i in range(len(lst)):
        if max_len <= len(lst[i]):
            max_len = len(lst[i])

    for i in range(len(lst)):
        while len((lst[i])) != max_len:
            lst[i].append(0)

    if st == ['+']:
        print('Сумма чисел в списках = ', add(lst))
    elif st == ['-']:
        print('Разность чисел между первым и последующими списками = ', sub(lst))
    elif st == ['/']:
        print('Частное чисел первого и последующих списков = ', div(lst))
    elif st == ['*']:
        print('Произведение чисел первого и последующих списков = ', mult(lst))
    elif st == ['**']:
        print('Возведение в степень чисел первого списка = ', pow(lst))
    elif st == ['sqrt']:
        print('Взятие корня из всех чисел списков = ', sqrt(lst))
    elif st == ['log']:
        print('Введите основание логарифма:')
        base = int(input())
        print('Логарифм по основанию', base, 'всех чисел списков = ', log(lst, base))
