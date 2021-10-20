




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

        elif optiune == 'x':
            break
        else:
            print('Optiune Invalida!')

main()

