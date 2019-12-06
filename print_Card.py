# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:19:36 2019

@author: ildar
"""

class Print_Card:
    def card_str(self):
    # делаем из списка карточу
    list_c = []
    list_f = []

    for i in (0, 5, 10):
        list1 = self.list_card[i: i + 5]
        list_c.append(list1)

    for i in range(3):
        # index_str = []
        card_str = [0,0,0,0,0,0,0,0,0]
        card_str1 = []


        for j in range(len(self.index_str)):  # вставляем в соответствии с индуексом числа в строку
            card_str[self.index_str[i][j]] = list_c[i][j]

        for k in card_str:
            if k == 0:
                k = '  '
            card_str1.append(str(k))

        list_f.append(card_str1)

    print('-' * 25)
    print(* list_f[0])
    print(* list_f[1])
    print(* list_f[2])
    print('-' * 25)
