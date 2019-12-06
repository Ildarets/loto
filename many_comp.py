# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:27:13 2019

@author: ildar
"""
import random

from class_Gamer import Gamer

def many_comp(count_comp, count_card):
    list_comp = []
    pol = []
    winner_comp = None
    for count_c in range(count_comp):
        comp = Gamer(count_c, count_card)
        list_comp.append(comp)
        
    for comp in list_comp:
        comp.creat_card()
        print("Номер компьютера: ", comp.count_comp + 1)
        comp.print_card()
        
        
    while len(pol) != 90:     
        # вытаскиваем бочонки
        bochonok = random.randint(1, 90)

        if bochonok in pol:
            bochonok = random.randint(1, 90)
        else:
            pol.append(bochonok)
            
        print()
        print("Вытащен бочонок под номером:")
        print('=======    ', bochonok, '    =======')
        
        for comp in list_comp:
            comp.find_number(bochonok)
        
            print("Номер компьютера: ", comp.count_comp + 1)
            comp.print_card()
        
            if comp.winner() == True:
                winner_comp = comp.count_comp
                
        if winner_comp != None:
            break
            
            
    print("++"*30)
    print("Выиграл компьютер номер: ", winner_comp + 1)
    print("++" * 30)
    print("." * 35)
    print("Номера бочонков: {}".format(pol))
    print("Всего бочонков: {}".format(len(pol)))