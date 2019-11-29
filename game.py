import random

from card_2 import Kartochki


card_player = Kartochki()
card_comp = Kartochki()

card_list_player = card_player.card_list()
card_list_comp = card_comp.card_list()


pol = []
o  = []

flag = True


while len(pol) != 90:

    #выводим карточки игроков
    print("карточка игрока")
    card_player.card_str()
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

    answer = input("Введите y/n:  ")

    # while answer != 'n' or answer !='y':
    #     answer = input("Введите y/n:  ")
    #     continue

    o.append(answer)

    # for n, i in enumerate(card_list_player):
    #     if i == bochonok:
    #         if answer == 'y':
    #             card_list_player[n] = '--'
    #         elif answer == 'n':
    #             flag = False
    #             break
    #     elif i != bochonok:
    #         if answer == 'y':
    #             flag = False
    #             break



    if answer == 'y':
        for n, i in enumerate(card_list_player):
            if i == bochonok:
                card_list_player[n] = '--'
            elif i != bochonok:
                flag = False

        if flag == False:
            break
    elif answer == 'n':
        for n, i in enumerate(card_list_player):
            if i == bochonok:
                print("Game Over")
                flag = False

        if flag == False:
            break
    else:
        print("Введите y / n")



    for n, j in enumerate(card_list_comp):
        if j == bochonok:
            card_list_comp[n] = '--'
        else:
            print("Game Over")

    print(card_list_player)
    print(card_list_comp)
    print(o)




if flag == False:
    print("Игрок проиграл! Компьютер выиграл")
else:
    print("Игрок выиграл! Компьютер проиграл")


# print(card_list_player)

# card_comp.card_str()
#
# card_player.card_str()
# print(pol)
# print(len(pol))