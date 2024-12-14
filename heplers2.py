import random
from data2 import *
from time import sleep

def figh(current_enemy):
    wave = 1
    raund = random.randint (1,5)
    enem = enemies[current_enemy]
    enem_hp = enemies[current_enemy] ["hp"]
    print(f"вражина - {enem['name']}: {enem['script']}")
    if enem == "Улитка горыныч":
        print(f"текущая волна {wave}")
        input("Нажмите огромную кнопку чтобы продолжить")
        while players ["hp"] > 0 and enem_hp > 0:
            print (f"отгодай загадку висит лампа можно скушать")
            orki = input ("ваш ответ")
            if orki == "груша":
                wave = 2 
                enem_hp -= 10
            else :
                players ["hp"] -= 35
                wave = 2
            if wave == 2:
                print(f"текущая волна {wave}")
                input("Нажмите огромную кнопку чтобы продолжить")
                while players ["hp"] > 0 and enem_hp > 0:
                    print (f"отгодай загадку какое слово всегда пишется неправильно?")
                    shreki = input ("ваш ответ")
                    if shreki == "неправильно":
                        wave = 3
                        enem_hp -= 10
                    else :
                        players ["hp"] -= 40
                        wave = 3
                    if wave == 3:
                        print(f"текущая волна {wave}")
                        input("Нажмите огромную кнопку чтобы продолжить")
                        while players ["hp"] > 0 and enem_hp > 0:
                            print (f"отгадай код его все пьют но его не кто не любит что это ")
                            water = input ("ваш ответ")
                            if water == "4":
                                wave = 4
                                enem_hp -= 15
                            else :
                                players ["hp"] -= 45
                                wave = 4
                            if  wave == 4:    
                                print(f"текущая волна {wave}")
                                input("Нажмите огромную кнопку чтобы продолжить")
                                while players ["hp"] > 0 and enem_hp > 0:
                                    print (f"кто ты воин слабак или сильный ")
                                    zmei = input ("ваш ответ")
                                    if zmei == "сильный":
                                        wave = 5
                                        enem_hp -= 15
                                    else :
                                        players ["hp"] -= 20
                                        wave = 5
                                    if wave == 5:
                                        print(f"текущая волна {wave}")
                                        input("Нажмите огромную кнопку чтобы продолжить")
                                        while players ["hp"] > 0 and enem_hp > 0:
                                            print (f"")
                                            stive = input ("ваш ответ")
                                            if stive == "":
                                                wave = 5
                                                enem_hp -= 15
                                            else :
                                                players ["hp"] -= 45
                                                wave = 5


def display_player():
    print(f"""ваш урон {players["attack"]},
           ваше количество хп {players["hp"]},
           ваша броня {players["armor"]},
            ваша удача {players["luck"]},
             ваши деньги {players["money"]}""")


def display_enemy():
    enemy = enemies['current_enemy']
    print(f"ваш враг {enemy['name']}")
    print(f"кол-во хп врага {enemy['hp']}")
    print(f"урон врага {enemy['attack']}")


def display_inventory():
    print(f"вас приветствует инвентарь! ")
    for value in players["inventory"]:
        print(value)
    print(f"{players['money']} монет.")
    print()
    if "меч начала" in players["inventory"]:
        potion = input("""Желаешь взять меч начала?
    1 - да
    2 - нет
    """)

def shop():
    print("Добро пожаловать в наш лорёк странник! ")
    print(f"У тебя есть {players['money']} монет.")
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')

    item = input()
    if item in players["inventory"]:
        print(f"У тебя уже есть {items[item]['name'] }")
    elif players ["money"] >= items [item] ["price"]:
        print(f"ты успешно приобрел {items[item]['name']}")
        players["inventory"].append(items[item]['name'])
        players["money"] -= items[item]["price"]
    else:
        print("у вас недостаточно средств!!!")
        print()
        print("приходите ещё")
        print()
    








