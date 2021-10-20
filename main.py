def has_same_number_of_even_nr(A,B):
    '''
    functia numara elementele pare din multimi apoi le compara intre ele
    :param A:
    :param B:
    :return:
    '''
    nr1 = 0
    nr2 = 0
    for i in A:
        if i % 2 == 0:
            nr1 = nr1 + 1
    for i in B:
        if i % 2 == 0:
            nr2 = nr2 + 1
    if nr1 == nr2:
        return True
    return False

def test_has_same_number_of_even_nr():
    A = [2,4,7,5,7]
    B = [2,1,6,3,9,5]
    assert has_same_number_of_even_nr(A,B) == True
    A = [2, 4, 6, 5, 7]
    B = [2, 1, 6, 3, 9, 5]
    assert has_same_number_of_even_nr(A, B) == False

def intersection_of_A_and_B(A,B):
    AB = []
    for i in A:
        for j in B:
            if i == j:
                AB.append(i)
    return AB


def main():
    while True:
        print('1. Citire date. ')
        print('2. Verificare daca multimile au acelasi numar de elemente pare')
        print('3. Intersectia multimilor A si B. ')
        print('4.')
        print('x. Iesire.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            A = []
            B = []
            n = int(input('dimensiune prima multime: '))
            m = int(input('dimensiune a doua multime: '))
            print('elementele din prima multime: ')
            for i in range(0, n):
                e = int(input())
                A.append(e)
            print('elementele din a doua multime: ')
            for i in range(0, m):
                e = int(input())
                B.append(e)
            print(A,B)
        elif optiune == '2':
            if has_same_number_of_even_nr(A,B) == True:
                print('Multimile au acelasi numar de elemente pare.')
            else:
                print('Multimile nu au acelasi numar de elemente pare. ')
        elif optiune == '3':
            intersection = intersection_of_A_and_B(A,B)
            if intersection == []:
                print('Nu exista elemente comune intre ele')
            else:
                print(f'Intersectia dintre cele doua multimi este: {intersection}')
        elif optiune == 'x':
            break
        else:
            print('Optiune Invalida!')

test_has_same_number_of_even_nr()
main()

