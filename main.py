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

'''
Functie ajutatoare preluata din tema lab 3 
'''
def digit_number(n):
    '''
    determinarea numarului de cifre
    :param n:
    :return:
    '''
    nr = 1
    while n > 9:
        n = n // 10
        nr = nr + 1
    return nr

def concat_numbers(x,y):
    '''
    concatenarea a doua numere
    :param x:
    :param y:
    :return:
    '''
    x = x * pow(10, digit_number(y)) + y
    return x

def is_palindrome(n):
    '''
    functia verifica daca un numar este palindrom
    :param n:
    :return:
    '''
    aux = n
    ogl = 0
    while aux > 0:
        c = aux % 10
        ogl = ogl * 10 + c
        aux = aux // 10
    if ogl == n:
        return True
    return False

def get_mirrored(n):
    '''
    functia determina oglinditul unui numar
    :param n:
    :return:
    '''
    aux = n
    ogl = 0
    while aux > 0:
        c = aux % 10
        ogl = ogl * 10 + c
        aux = aux // 10
    return ogl

def get_palindrome_concat(A, n, B, m):
    lst = []
    if n > m:
        x = m
    else:
        x = n
    for i in range(0, x):
        concat = concat_numbers(A[i], B[i])
        if is_palindrome(concat) == True:
            lst.append(concat)
    return lst

def modify_lists(A,B,C,n,m):
    for i in range(0, n):
        ok = 1
        for j in C:
            if A[i] % j != 0:
                ok = 0
        if ok == 1:
            A[i] = get_mirrored(A[i])
    for i in range(0, m):
        ok = 1
        for j in C:
            if B[i] % j != 0:
                ok = 0
        if ok == 1:
            B[i] = get_mirrored(B[i])


def main():
    while True:
        print('1. Citire date. ')
        print('2. Verificare daca multimile au acelasi numar de elemente pare')
        print('3. Intersectia multimilor A si B. ')
        print('4. Afisarea palindroamelor obinute prin concatenarea elementelor de pe aceleasi pozitii')
        print('5. Inlocuirea elementelor din lista cu oglinditul lor daca sunt divizibile cu toate elementele din multimea C')
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
        elif optiune == '4':
            y = get_palindrome_concat(A, n, B, m)
            if y == []:
                print('Nu exista astfel de elemente')
            else:
                print(f'Palindroamele rezultate din concatenare sunt: {y}')
        elif optiune == '5':
            C = []
            p = int(input('Dimensiunea multimii C'))
            for i in range(0, p):
                e = int(input())
                C.append(e)
            H = A
            J = B
            modify_lists(A,B,C,n,m)
            if A == H and J == B:
                print('listele au ramas nemodificate.')
            print(A,B)

        elif optiune == 'x':
            break
        else:
            print('Optiune Invalida!')

test_has_same_number_of_even_nr()
main()

