from random import randint
from time import sleep
from heplers2 import *
from data2 import *

name = input('Введи своё имя, путник: ')
players['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Магазин
3 - Показать инвентарь
4 - Информация об игроке
5 - Информация о текущем противнике
''')
    if action == '1':
        current_enemy = figh(current_enemy)
        if current_enemy == 3:
            break

    elif action == '2':
        shop()
    elif action == '3':
        display_inventory()
    elif action == '4':
        display_player()
    elif action == '5':
        display_enemy(current_enemy)


        
            


