def print_integers(lst)
    


def main():
    while True:
        print('1. Citire date. ')
        print('2.')
        print('3.')
        print('4.')
        print('x. Iesire.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            lst = []
            n = int(input('Dimensiunea listei: '))
            for i in range(0, n):
                e = float(input())
                lst.append(e)
            print(lst)
        elif potiune == 'x':
            break
        else:
            print('Optiune Invalida!')

main()