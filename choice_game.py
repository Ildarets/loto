from game import player_computer
from game_comp import computer_computer
from many_comp import many_comp

print("Выберите игру. Игрок компьютер или компьютер с компьютером.")
answer = int(input("1 - Игрок с компьютером \n2 - Компьютер с компьютером: \n3 - Несколько компьютеров \n"))

if answer == 1:
    player_computer()
elif answer == 2:
    computer_computer()
elif answer == 3:
    count_comp = int(input("Введите число компьютеров: "))
    count_card = int(input("Введите кол-во карточек: "))
    many_comp(count_comp, count_card)