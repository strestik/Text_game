import time, random, sys
from contants import *
# from attack import *
# from characters import *

class Character:
    def __init__(self, name, char_class,):
        self.is_alive = True
        self.bck = False
        self.name = name
        self.char_class = char_class 
        self.hp = 100
        self.stamina = 100
        self.mana = 0
        self.defense = 70
        self.skill = 1 # dmg multiplier
        self.respect = 15
        self.abilities = []
        self.h_amount = 0
        self.s_amount = 0

        self.effects = store_effects.copy()  # Copy the store_effects dictionary to the instance variable

        self.elixiers = store_elixirs.copy()  # Copy the store_elixirs dictionary to the instance variable

        self.equip = store_equip.copy()  # Copy the store_equip dictionary to the instance variable
    
    def __str__(self):
        return f"\n---> Tvoje postava je {Hero.name}, třída: {Hero.char_class}, HP: {Hero.hp}, Stamina: {Hero.stamina}, Mana: {Hero.mana}, Defense: {Hero.defense}, Síla: {Hero.skill * 100}%\n"


Hero = Character("Hero", "Witcher")
Enemy = Character(f"{random.choice(enemy_names)}", f"{random.choice(characters)}") 


def nameing(self):
    Hero.name = input("-- Zadej jméno: ").strip()
    if not Hero.name:
        print("--> Jméno nesmí být prázdné.\n")
        self.nameing()
    elif Hero.name.isdigit():
        print("--> Jméno nesmí být číslo.\n")
        self.nameing()
    else:
        while True:
            change_name = input(f"\n-- Chceš změnit jméno ? (y/n): ").strip().lower()
            if change_name == 'y':
                self.nameing()
                break
            elif change_name == 'n':
                # global ch_name
                # ch_name = Hero.name
                return Hero.name
            else:
                print("--> Neplatná volba, zkus to znovu.")

def is_alive_check(self):
        self.is_alive = False if self.hp <= 0 else True
        global alive
        if not Hero.is_alive:
            print(f"{Hero.name} byl poražen! Konec hry.\n")
            alive = False

        if not Enemy.is_alive:
            print(f"{Enemy.name} byl poražen!!! Gratuluji!\n")
            alive = False

def mana_check(self, mana_cost):
    if self.mana < 20:
        print("Nemáš dost many!")
        return
    else:
        self.mana -= 20

def stamina_check(self, stamina_cost):
    if self.stamina < 20:
        print("Nemáš dost staminy!")
        return
    else:
        self.stamina -= 20
