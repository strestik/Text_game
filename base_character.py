# přidat character, is_alive, mana a stamina checky, a take damage
import random
import time
import sys
from text import *
import chractering 
from attack import *

round_counter = 1


    
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

        self.effects = {"burning": {"is" : False, "duration": 0}, 
                        "poisoned": {"is" : False, "duration": 0}, 
                        "stunned": {"is" : False, "duration": 0}, 
                        "frozen": {"is" : False, "duration": 0}, 
                        "bleeding": {"is" : False, "duration": 0}, 
                        "healing": {"is" : False, "duration": 0}, 
                        "stamina regen": {"is" : False, "duration": 0},
                        "shielding" : {"is": False, "duration" : 0},
                        }
     
        self.elixiers = {
            "healing potion": {"own": 3,"amount": 50},
            "stamina potion": {"own": 3,"amount": 45},
            "mana potion": {"own": 3,"amount": 35}, 
            "vlaštovka": {"own": 1,"amount": 25, "duration" : 4}, # duration healing
            "hrom": {"own": 2,"amount": 1.5}, # dmg multiplier
            "vlk": {"own": 2,"amount": 0.15}, # sklill multiplier
            "medvěd": {"own": 2,"amount": 0.25}, # defense multiplier
            "blizzard": {"own": 1,"amount": 20, "duration" : 4}, # stamina regen
            }
        
        self.equip = {
            # "iron claws": {"own":False,"dmg_mutipl": 0.25},  # [owned, dmg multiplier]
            # "elven lute": {"own":False,"dmg_mutipl": 0.25},  
            # "siderite sword": {"own":False,"dmg_mutipl": 0.25},
            # "skellige axe": {"own":False,"dmg_mutipl": 0.25},
            # "brokilon bow": {"own":False,"dmg_mutipl": 0.25},
            # "dimeritium staff": {"own":False,"dmg_mutipl": 0.25},
            # "mahakam hammer" : {"own":False,"dmg_multiplier": 0.35}
            "bomb": {"own":True,"dmg": 60, "effect": None},  # [owned, base dmg]
            "poison bomb": {"own":True,"dmg": 50, "effect": "poisoned"},  # [owned, base dmg, effect]
            "fire bomb": {"own":True,"dmg": 50, "effect": "burning"},  
            "frost bomb": {"own":True,"dmg": 50, "effect": "frozen"}, 
            }
        
def is_alive_check(self):
    self.is_alive = False if self.hp <= 0 else True
    if not self.is_alive:
        time.sleep(1)
        print(f"\n{self.name} byl poražen!!")
        global alive
        alive = False
        if not Hero.is_alive:
            print(f"{Hero.name} byl poražen! Konec hry.\n")
            alive = False
            sys.exit(0)
        if not Enemy.is_alive:
            print(f"{Enemy.name} byl poražen!!! Gratuluji!\n")
            alive = False
            sys.exit(0)


def mana_check(self):
    if self.mana < 20:
        print("Nemáš dost many!")
        return
    else:
        self.mana -= 20

def stamina_check(self):
    if self.stamina < 20:
        print("Nemáš dost staminy!")
        return
    else:
        self.stamina -= 20


def take_damage(self, attack: Attack):
    raw_dmg = attack.calculate_damage()
    reduced_dmg = max(raw_dmg - self.defense, 0)
    self.hp -= reduced_dmg
    print(f"{self.name} dostal {reduced_dmg} poškození od útoku {attack.name}.")

    # Efekty
    for effect in attack.effects:
        self.effects[effect]["is"] = True
        print(f"{self.name} je nyní ovlivněn efektem: {effect}.")
    
        self.is_alive_check()

Hero = Character("x", "x")  # Initialize Hero variable
Enemy = None