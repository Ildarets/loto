# coding=utf-8
import random

# from typing import List


class Kartochki:
    def __init__(self):
        self.list_card = []
        self.list_f = []
        self.index_str = []
        for i in range(3):
            str_ind = []
            while len(str_ind) != 5:  # генерируем числа от 0 до 8, которые будут индексами в строке
                ind = random.randint(0, 8)
                if ind in str_ind:
                    continue
                else:
                    str_ind.append(ind)
            self.index_str.append(str_ind)

    def card_list(self):
        # генерируем числа от 1 до 90 и вставляем в список длиной 15
        while len(self.list_card) != 15:
            number = random.randint(1, 90)
            if number in self.list_card:
                continue
            else:
                self.list_card.append(number)
        return self.list_card



    def card_str(self):
        # делаем из списка карточу
        list_c = []
        self.list_f = []

        for i in (0, 5, 10):
            list1 = self.list_card[i: i + 5]
            list_c.append(list1)

        for i in range(3):
            card_str = [0,0,0,0,0,0,0,0,0]
            card_str1 = []


            for j in range(len(self.index_str[i])):  # вставляем в соответствии с индексом числа в строку
                card_str[self.index_str[i][j]] = list_c[i][j]

            for k in card_str:
                if k == 0:
                    k = '  '
                card_str1.append(str(k))

            self.list_f.append(card_str1)

        print('-' * 25)
        print(* self.list_f[0])
        print(* self.list_f[1])
        print(* self.list_f[2])
        print('-' * 25)


if __name__ == '__main__':
    card = Kartochki()
    print(card.index_str)
