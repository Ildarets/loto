import random

from card_2 import Kartochki


def computer_computer():
    card_comp1 = Kartochki()
    card_comp2 = Kartochki()

    card_list_comp1 = card_comp1.card_list()
    card_list_comp2 = card_comp2.card_list()

    pol = []
    flag = True

    while len(pol) != 90:

        # выводим карточки игроков
        print("карточка компьютера номер 1")
        card_comp1.card_str()
        print()
        print("карточка компьютера номер 2")
        card_comp2.card_str()

        # вытаскиваем бочонки
        bochonok = random.randint(1, 90)

        if bochonok in pol:
            bochonok = random.randint(1, 90)
        else:
            pol.append(bochonok)

        print('=======    ', bochonok, '    =======')

        for n, j in enumerate(card_list_comp1):
            if j == bochonok:
                card_list_comp1[n] = '--'

        for n, j in enumerate(card_list_comp2):
            if j == bochonok:
                card_list_comp2[n] = '--'

        if card_list_comp1.count('--') == 15:
            flag = True
            break
        elif card_list_comp2.count('--') == 15:
            flag = False
            break

    if flag == False:
        print("++"*30)
        print("Компьютер номер 2 -  выиграл! Компьютер номер 1 - проиграл!")
        print("++" * 30)
    else:
        print("Компьютер номер 1 -  выиграл! Компьютер номер 2 - проиграл!")

    print("." * 35)
    print("Номера бочонков: {}".format(pol))
    print("Всего бочонков: {}".format(len(pol)))
