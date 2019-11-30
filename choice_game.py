from game import player_computer
from game_comp import computer_computer

print("Выберите игру. Игрок компьютер или компьютер с компьютером.")
answer = int(input("1 - Игрок с компьютером \n2 - Компьютер с компьютером:  "))

if answer == 1:
    player_computer()
elif answer == 2:
    computer_computer()