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
        self.full_card_str = []
        self.index_card = []
        self.full_card_ready = []
        for i in range(30):
            self.full_card.append(0)

    def card_full(self):

        while len(self.card_list) != 15:
            self.number = random.randint(1, 91)
            if self.number in self.card_list:
                continue
            else:
                self.card_list.append(self.number)

        while len(self.index_card) != 15:
            self.ind = random.randint(0, 30)
            if self.ind in self.index_card:
                continue
            else:
                self.index_card.append(self.ind)

        for i in range(len(self.card_list)):
            self.full_card[self.index_card[i]] = self.card_list[i]

        for i in self.full_card:
            if i == 0:
                i = ' '
            self.full_card_str.append(str(i))


        self.full_card_ready.append(self.full_card_str[0:10])
        self.full_card_ready.append(self.full_card_str[10:20])
        self.full_card_ready.append(self.full_card_str[20:30])


        return self.full_card_ready


    def print_card(self):
        print('-' * 25)
        print(*self.card_full()[0])
        print(*self.card_full()[1])
        print(*self.card_full()[2])
        print('-' * 25)







card1 = Card()
card1.print_card()
print(card1.card_full())
# print(card1.card_const())
