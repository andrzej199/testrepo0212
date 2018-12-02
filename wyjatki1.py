import random


def init():
    random.seed()


def main():
    init()
    number_to_guess = random.randint(0, 10)
    while True:
        num = input('Podaj liczbe: ')
        try:
            num = int(num)
        except ValueError:
            print("podaj liczbę całkowitą")
            #contnue - to można użyc bez else
        else:               # raczej nie używać else w try
            if num < number_to_guess:
                print('Za malo')
            elif num > number_to_guess:
                print('Za duzo')
            else:
                print('Zgadles')
                break #continue przerywa bierzącą operację i wraca do pętli


main()