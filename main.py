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


def main():
    while True:
        print('1. Citire date. ')
        print('2. Afisarea numerelor intregi din lista')
        print('3.')
        print('4.')
        print('x. Iesire.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            A = []
            B = []
            n = int(input('dimensiune prima multime: '))
            m = int(input('dimensiune a doua multime: '))
            for i in range(0, n):
                e = int(input())
                A.append(e)
            for i in range(0, m):
                e = int(input())
                B.append(e)
            print(A,B)
        elif optiune == '2':
            if has_same_number_of_even_nr(A,B) == True:
                print('Multimile au acelasi numar de elemente pare.')
            else:
                print('Multimile nu au acelasi numar de elemente pare. ')

        elif optiune == 'x':
            break
        else:
            print('Optiune Invalida!')

test_has_same_number_of_even_nr()
main()

