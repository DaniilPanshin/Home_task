class Sequence:

    alphabet = []
    mol_mass = {}

    def __init__(self, name, seq):
        self.name = name
        self.seq = seq

    def name(self):
        return self.name  # возвращает имя последовательности

    @property
    def len(self):
        return len(self.seq) #возвращает длину последовательности

    def sequence(self):
        return self.seq #возвращает саму последовательность

    def statistics(self):
        stat = dict.fromkeys(self.alphabet, 0)
        for i in self.seq:
            stat[i] += 1
        return stat # возвращает статистику по использованию символов

    def mass(self):
        mass = 0
        for i in self.seq:
            mass += self.mol_mass[i]
        return mass  # возвращает молекулярную массу

class DNA(Sequence):

    alphabet = ['A', 'T', 'G', 'C']
    mol_mass = {'A': 313.21, 'T': 304.2, 'G': 329.21, 'C': 289.18}

    def __init__(self, name, seq):
        super().__init__(name, seq)

    def complement(self):
        comp_seq = ''
        comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        for i in self.seq:
            comp_seq += comp[i]
        return comp_seq #возвращает комплементарную последовательность

    def transcription(self):
        rna_seq = ''
        comp = {'A': 'Y', 'T': 'A', 'G': 'C', 'C': 'G'} #ДНК как матричная
        for i in self.seq:
            rna_seq += comp[i]
        return rna_seq #возвращает последовательность РНК

class RNA(Sequence):

    alphabet = ['A', 'U', 'G', 'C']
    mol_mass = {'A': 313.21, 'U': 306.2, 'G': 329.21, 'C': 289.18}

    def __init__(self, name, seq):
        super().__init__(name, seq)

    def complement(self):
        comp_seq = ''
        comp = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
        for i in self.seq:
            comp_seq += comp[i]
        return comp_seq  # возвращает комплементарную последовательность

    def translation(self):
        protein = []
        pr_name = 0
        pr = ''
        code = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                'UAU': 'Y', 'UAC': 'Y', 'UAA': 'stop', 'UAG': 'stop', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                'UGU': 'C', 'UGC': 'C', 'UGA': 'stop', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', }
        for i in range(0, self.len-2, 3):
            # проверка на стоп кодон, если да, то добавляет в список белков
            if code[self.seq[i:i + 3]] == 'stop':
                protein.append(pr)
                pr = ''
            # проверка, что это либо старт кодон и последовательность пустая, либо последовательность не пустая
            if (code[self.seq[i:i + 3]] == 'M' and pr == '') or pr != '':
                pr += code[self.seq[i:i+3]]
        return protein #возвращает список из белков, закодированных в РНК

class Protein(Sequence):
    alphabet = ['G', 'L', 'Y', 'S', 'E', 'Q', 'D', 'N', 'F', 'A', 'K', 'R', 'H', 'C', 'V', 'P', 'W', 'I', 'M', 'T']
    mol_mass = {'G': 75.0669, 'L': 131.1736, 'Y': 181.1894, 'S': 105.093, 'E': 147.1299, 'Q': 146.1451, 'D': 133.1032,
                'N': 132.1184, 'F': 165.19, 'A': 89.0935, 'K': 146.1882, 'R': 174.2017, 'H': 155.1552, 'C': 121.159,
                'V': 117.1469, 'P': 115.131, 'W': 204.2262, 'I': 131.1736, 'M': 149.2124, 'T': 119.1197}

    def __init__(self, name, seq):
        super().__init__(name, seq)


# функция сортировки вставкой, возвращает отсортированный список
def insert_sort(l):
    for i in range(1, len(l)):
        current = l[i]
        j = i - 1
        while j >= 0 and l[j] > current:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = current
    return l



# функция создания последовательностей определенного типа
def seqs_creation(t):
    ls = [i for i in input().split()]
    seqs = []
    for i in range(0, len(ls), 2):
        if t == 1:
            seqs.append(DNA(ls[i], ls[i + 1]))
        elif t == 2:
            seqs.append(RNA(ls[i], ls[i + 1]))
        elif t == 3:
            seqs.append(Protein(ls[i], ls[i + 1]))
    return seqs

# функция создания словаря с количеством замен у последовательностей
def dict_of_replace(r, s):
    replaces_dict = dict.fromkeys(s, 0)
    flag = True
    for i in range(len(s)):
        if r.len == s[i].len:
            for j in range(len(r.seq)):
                if r.seq[j] != s[i].seq[j]:
                    replaces_dict[s[i]] += 1
        else:
            flag = False
    return flag, replaces_dict

# функция сортировки последовательностей по количеству замен
def seq_sort(r, l):
    fl, d = dict_of_replace(r, l)
    if fl == False:
        print('Длина последовательностей различается. Сортировка не будет выполнена')
    else:
        for i in range(1, len(l)):
            current = l[i]
            j = i - 1
            while j >= 0 and d[l[j]] > d[current]:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = current
    return l

if __name__ == '__main__':

    #Сортировка списка чисел вставкой из пользовательского ввода
    print('Введите список чисел для сортировки:')
    lst = [int(i) for i in input().split()]
    print(insert_sort(lst))

    #Выбор класса для сравнения последовательностей
    print('Выберите число, соответствующее классу последовательностей для сравнения:'
          '\n1: DNA\n2: RNA\n3: Protein')
    typ = int(input())

    #Создание референса и списка последовательностей
    print('Введите референс:')
    ref = seqs_creation(typ)[0]
    print('Введите последовательности для сортировки:')
    seq = seqs_creation(typ)

    # Сортировка последовательностей вставкой
    ranged = seq_sort(ref, seq)
    for i in range(len(ranged)):
        print(ranged[i].name, ranged[i].seq)





