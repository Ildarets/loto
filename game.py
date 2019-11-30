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
    while answer != 'y' or answer != 'n':
        if answer=='y' or answer=='n':
            break
        answer = input("Введите y/n:  ")



    o.append(answer)

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
        # else:
        #     print("Game Over")

    print(card_list_player)
    print(card_list_comp)
    print(o)




if flag == False:
    print("Игрок проиграл! Компьютер выиграл")
else:
    print("Игрок выиграл! Компьютер проиграл")

