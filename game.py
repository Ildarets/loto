import random

from card_2 import Kartochki


def player_computer():
    card_player = Kartochki()
    card_comp = Kartochki()

    card_list_player = card_player.card_list()
    card_list_comp = card_comp.card_list()

    pol = []
    flag = True

    while len(pol) != 90:

        # выводим карточки игроков
        print("карточка игрока")
        card_player.card_str()
        print()
        print("карточка компьютера")
        card_comp.card_str()

        # вытаскиваем бочонки
        bochonok = random.randint(1, 90)

        if bochonok in pol:
            bochonok = random.randint(1, 90)
        else:
            pol.append(bochonok)

        print('=======    ', bochonok, '    =======')
        print("Зачеркнуть или продолжить? ")
        print("-" * 30)

        print("=======   Введите y/n: =======  ")
        answer = input()
        while answer != 'y' or answer != 'n':
            if answer == 'y' or answer == 'n':
                break
            print("=======   Введите y/n: =======  ")
            answer = input()

        if bochonok in card_list_player:
            if answer == 'y':
                for n, i in enumerate(card_list_player):
                    if i == bochonok:
                        card_list_player[n] = '--'
            elif answer == 'n':
                flag = False
                break
        else:
            if answer == 'y':
                flag = False
                break

        for n, j in enumerate(card_list_comp):
            if j == bochonok:
                card_list_comp[n] = '--'


        if card_list_player.count('--') == 15:
            flag = True
            break
        elif card_list_comp.count('--') == 15:
            flag = False
            break

    if flag == False:
        print("+"*30)
        print("Игрок проиграл! Компьютер выиграл")
        print("+" * 30)
    else:
        print("Игрок выиграл! Компьютер проиграл")

    print("." * 35)
    print("Номера бочонков: {}".format(pol))
    print("Всего бочонков: {}".format(len(pol)))