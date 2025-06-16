# přidat classing, en_classing a naming
import random
import time
import sys
from text import *
from potion import *
from items import *
from effect import *
from h_characters import *
from e_chracters import *
from base_character import *
from attack import *

def nameing(self):
    name = input("-- Zadej jméno: ").strip()
    if not name:
        print("--> Jméno nesmí být prázdné.\n")
        self.nameing()
    elif name.isdigit():
        print("--> Jméno nesmí být číslo.\n")
        self.nameing()
    else:
        while True:
            change_name = input(f"\n-- Chceš změnit jméno ? (y/n): ").strip().lower()
            if change_name == 'y':
                self.nameing()
                break
            elif change_name == 'n':
                Hero.name = name
                return
            else:
                print("--> Neplatná volba, zkus to znovu.")
            


def classing(self):
    print("1. Witcher\n"
            "2. Sorcerer\n"
            "3. Archer\n"
            "4. Jarl\n"
            "5. Bard\n"
            "6. Monster\n")
    while True:
        char_class = input("Zadej číslo třídy: ").strip()
        if not char_class.isdigit():
            print("--> Neplatný vstup, zkus to znovu.\n")
            continue
        char_class = int(char_class)
        if char_class == 1:
            return Witcher(self.name)
        elif char_class == 2:
            return Sorcerer(self.name)
        elif char_class == 3:
            return Archer(self.name)
        elif char_class == 4:
            return Jarl(self.name)
        elif char_class == 5:
            return Bard(self.name)
        elif char_class == 6:
            return Monster(self.name)
        else:
            print("--> Neplatná třída, zkus to znovu.\n")

def en_classing(self, char_class):
    if char_class == "Witcher":
        return Witcher(self.name)
    elif char_class == "Sorcerer":
        return Sorcerer(self.name)
    elif char_class == "Archer":
        return Archer(self.name)
    elif char_class == "Jarl":
        return Jarl(self.name)
    elif char_class == "Bard":
        return Bard(self.name)
    elif char_class == "Monster":
        return Monster(self.name)
    else:
        print("--> Neplatná třída, zkus to znovu.\n")