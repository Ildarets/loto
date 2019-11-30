import random


class Card:
    """
    класс, который генерирует карточки со случайными числами
    """

    def __init__(self):
        self.number = None
        self.card_list = []
        self.i = 0
        self.stroka = []
        self.card_constuct = []
        self.full_card = []
        self.index_card = []
        for i in range(27):
            self.full_card.append(0)

    def card_full(self):
        """
        Функция выдает список с числами от 1 до 90 в количестве 15 шт.
        """
        self.full_card_str = []

        while len(self.card_list) != 15: # генерируем числа от 1 до 90 и вставляем в список длино1 15
            self.number = random.randint(1, 91)
            if self.number in self.card_list:
                continue
            else:
                self.card_list.append(self.number)

        return self.card_list

    def card_mod(self):
        """
        Функция для построения карточки
        """
        card_list1 = card_list[0:5]
        card_list2 = card_list[5:10]
        card_list3 = card_list[10:15]

        full_card1 = []
        full_card2 = []
        full_card3 = []

        while len(self.index_card) != 5: # генерируем числа от 0 до 8, которые будут индексами в строке
            self.ind = random.randint(0, 8)
            if self.ind in self.index_card:
                continue
            else:
                self.index_card.append(self.ind)

        for i in range(len(self.index_card1)): # вставляем в соответствии с индуексом числа в карточку
            self.full_card1[self.index_card1[i]] = self.card_list1[i]

        for i in range(len(self.index_card2)):  # вставляем в соответствии с индуексом числа в карточку
            self.full_card2[self.index_card2[i]] = self.card_list2[i]

        for i in range(len(self.index_card3)):  # вставляем в соответствии с индуексом числа в карточку
            self.full_card3[self.index_card3[i]] = self.card_list3[i]

        for i in self.full_card: # заменяем 0 пробелами
            if i == 0:
                i = ' '
            self.full_card_str.append(str(i))

        return self.full_card_str # возращаем список


    def print_card(self):
        """
        Функция для печати карточки
        """
        print('-' * 25)
        print(*self.card_full()[0:10])
        print(*self.card_full()[10:20])
        print(*self.card_full()[20:30])
        print('-' * 25)




card1 = Card()
card1.print_card()
# print(card1.card_full())
# print(len(card1.card_full()))

card2 = Card()
card2.print_card()
# print(card2.card_full())
# print(len(card2.card_full()))
# print(card1.card_const())
