# pre_alpha(v0_1.1 build 20180124)
import random

import time

from myFunctions import *

import threading as th

def make_mine():
    global gold
    global mines_count
    if gold >= 50:
        gold -= 50
        mines_count += 1
    else:
        print('Нужно больше золота!')
def make_casarm():
    global gold
    global casarm_count
    if gold >= 30:
        gold -= 30
        casarm_count += 1
    else:
        print('Нужно больше золота!') # Отсылка к WarCraft 3

def target():
    while True:
        time.sleep(60)
        global army
        global gold
        global mines_count
        global casarm_count
        gold = give_gold(mines_count, gold)
        army = casarm(casarm_count, army)

t = th.Thread(target=target, daemon=True)

t.start()
def castle_attack(command, castles, attack):
    global army
    for key in castles:
        if command == 'attack '+key:
            print('Вы подошли к воротам замка - ',key)
            print('                       /^\             \n'
                  '                       | |             \n'
                  '                       |-|             \n'
                  '                  /^\  | |             \n'
                  '           /^\  / [_] \+-+             \n'
                  '          |---||-------| |             \n'
                  ' _/^\_    _/^\_|  [_]  |_/^\_   _/^\_  \n'
                  ' |___|    |___||_______||___|   |___|  \n'
                  '  | |======| |===========| |=====| |   \n'
                  '  | |      | |    /^\    | |     | |   \n'
                  '  | |      | |   |   |   | |     | |   \n'
                  '  |_|______|_|__ |   |___|_|_____|_|   \n')
            print('ИДЕТ БИТВА!')
            time.sleep(5)
            if key == 'virginia':
                castle_lvl = 1
                resist = 100 + castle_lvl * random.randint(1, 15)
                resist = resist - attack * random.randint(1, 7)
                army = army - resist
                if army < 0:
                    army = 0
                battle_result = resist - army

                if battle_result > 0 and army > 0:
                    print('Вы победили, у вас осталось',army,'войнов')
                else:
                    print('Вы проиграли')


def attack_calculate(hero_lvl,super_weapon,army):
    attack = hero_lvl + super_weapon
    return attack

army = 0

hero_lvl = 1

super_weapon = 0

my_castle = {}

castles = {'virginia': 1, 'eblantus': 2}

gold = 100

mines_count = 1

casarm_count = 1

attack = 0

defence = 0

enemy_resist = 0

command = 'default'

if command == 'default':
    print('Привет это игра castle fight. Для того что бы посмотреть правила и управление введи rules')

while True:

    command = str(input())

    if command == 'rules':
        print('что бы аттаковать замок введи: attack имя крепости \n'
              'что бы посмотреть свои характеристики напиши show_me \n'
              'посмотреть список замков доступных для атаки castle_list \n'
              'создать казарму make_casarm \n'
              'создать рудник make_mine \n')

    if command == 'show_me':
        attack = attack_calculate(hero_lvl,super_weapon,army)
        print('Количество золота:', gold)
        print('Количество армии:', army)
        print('Количество казарм:', casarm_count)
        print('Количество рудников:', mines_count)
        print('Ваша суммарная аттака:', attack)
        print('Ваша суммарная защита крепости:', defence)
        print('Уровень героя:', hero_lvl)
        print('Осадные орудия:', super_weapon)

    if command == 'castle_list':
        view_castles(castles)

    castle_attack(command, castles, attack = attack_calculate(hero_lvl,super_weapon,army))

    if command == 'make_mine':
        make_mine()

    if command == 'make_casarm':
        make_casarm()


