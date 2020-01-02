from card_2 import Kartochki

class Gamer():
    
    def __init__(self, count_comp, count_card):
        self.count_card = count_card
        self.list_card_gamer = []
        self.count_comp = count_comp
        
    def creat_card(self):
        for i in range(self.count_card):
            card = Kartochki()
            card.card_list()
            self.list_card_gamer.append(card)
            
    def print_card(self):
        for card in self.list_card_gamer:
            card.card_str()
            
    def find_number(self, bochonok):
        for card in self.list_card_gamer:
            for n, j in enumerate(card.list_card):
                if j == bochonok:
                    card.list_card[n] = '--'
                    
    def winner(self):
        flag = False
        for card in self.list_card_gamer:
            if card.list_card.count('--') == 15:
                self.list_card_gamer.remove(card)
        if self.list_card_gamer == []:
            flag = True
        return flag
                
 