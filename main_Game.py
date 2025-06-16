import random
import time
import sys
from text import *
from chractering import *
from potion import *
from items import *
from effect import *
from h_characters import *
from e_chracters import *
from base_character import *


alive = True
delay = 2


# class Attack:
#     def __init__(self, attacker, name, base_dmg, dmg_type, effects=None):
#         self.attacker = attacker  # instance postavy, která útočí
#         self.name = name
#         self.base_dmg = base_dmg
#         self.dmg_type = dmg_type
#         self.effects = effects or []
#         self.multiplier = Hero.skill  # vynásobíme dovedností, možnist přidání multiplieru z vybavení

#     def calculate_damage(self):
#         return int(self.base_dmg * self.multiplier)
    
# class Character:
#     def __init__(self, name, char_class,):
#         self.is_alive = True
#         self.bck = False
#         self.name = name
#         self.char_class = char_class 
#         self.hp = 100
#         self.stamina = 100
#         self.mana = 0
#         self.defense = 70
#         self.skill = 1 # dmg multiplier
#         self.respect = 15
#         self.abilities = []
#         self.h_amount = 0
#         self.s_amount = 0

#         self.effects = {"burning": {"is" : False, "duration": 0}, 
#                         "poisoned": {"is" : False, "duration": 0}, 
#                         "stunned": {"is" : False, "duration": 0}, 
#                         "frozen": {"is" : False, "duration": 0}, 
#                         "bleeding": {"is" : False, "duration": 0}, 
#                         "healing": {"is" : False, "duration": 0}, 
#                         "stamina regen": {"is" : False, "duration": 0},
#                         "shielding" : {"is": False, "duration" : 0},
#                         }
#         self.elixiers = {
#             "healing potion": {"own": 3,"amount": 50},
#             "stamina potion": {"own": 3,"amount": 45},
#             "mana potion": {"own": 3,"amount": 35}, 
#             "vlaštovka": {"own": 1,"amount": 25, "duration" : 4}, # duration healing
#             "hrom": {"own": 2,"amount": 1.5}, # dmg multiplier
#             "vlk": {"own": 2,"amount": 0.15}, # sklill multiplier
#             "medvěd": {"own": 2,"amount": 0.25}, # defense multiplier
#             "blizzard": {"own": 1,"amount": 20, "duration" : 4}, # stamina regen
#             }
        
#         self.equip = {
#             # "iron claws": {"own":False,"dmg_mutipl": 0.25},  # [owned, dmg multiplier]
#             # "elven lute": {"own":False,"dmg_mutipl": 0.25},  
#             # "siderite sword": {"own":False,"dmg_mutipl": 0.25},
#             # "skellige axe": {"own":False,"dmg_mutipl": 0.25},
#             # "brokilon bow": {"own":False,"dmg_mutipl": 0.25},
#             # "dimeritium staff": {"own":False,"dmg_mutipl": 0.25},
#             # "mahakam hammer" : {"own":False,"dmg_multiplier": 0.35}
#             "bomb": {"own":True,"dmg": 60, "effect": None},  # [owned, base dmg]
#             "poison bomb": {"own":True,"dmg": 50, "effect": "poisoned"},  # [owned, base dmg, effect]
#             "fire bomb": {"own":True,"dmg": 50, "effect": "burning"},  
#             "frost bomb": {"own":True,"dmg": 50, "effect": "frozen"}, 
#             }

# def is_alive_check(self):
#     self.is_alive = False if self.hp <= 0 else True
#     if not self.is_alive:
#         time.sleep(1)
#         print(f"\n{self.name} byl poražen!!")
#         global alive
#         alive = False
#         if not Hero.is_alive:
#             print(f"{Hero.name} byl poražen! Konec hry.\n")
#             alive = False
#             sys.exit(0)
#         if not Enemy.is_alive:
#             print(f"{Enemy.name} byl poražen!!! Gratuluji!\n")
#             alive = False
#             sys.exit(0)

# def mana_check(self):
#     if self.mana < 20:
#         print("Nemáš dost many!")
#         return
#     else:
#         self.mana -= 20

# def stamina_check(self):
#     if self.stamina < 20:
#         print("Nemáš dost staminy!")
#         return
#     else:
#         self.stamina -= 20


# def take_damage(self, attack: Attack):
#     raw_dmg = attack.calculate_damage()
#     reduced_dmg = max(raw_dmg - self.defense, 0)
#     self.hp -= reduced_dmg
#     print(f"{self.name} dostal {reduced_dmg} poškození od útoku {attack.name}.")

#     # Efekty
#     for effect in attack.effects:
#         self.effects[effect]["is"] = True
#         print(f"{self.name} je nyní ovlivněn efektem: {effect}.")
    
#     self.is_alive_check()


def apply_effects(self, h_amount, s_amount):    # možnost přidání časiového omezení efektů
    if self.effects["bleeding"]["is"] == True:
        if self.effects["bleeding"]["duration"] == 0:
            self.effects["bleeding"]["is"] == False
        else:
            print(f"\n{self.name} krvácí a ztrácí 10 HP.\n")
            self.hp -= 10
            self.effects["bleeding"]["duration"] -= 1
            if self.effects["bleeding"]["duration"] <= 0:
                self.effects["bleeding"]["is"] = False
                print(f"{self.name} přestal krvácet.\n")

    if self.effects["burning"]["is"] == True:
        if self.effects["burning"]["duration"] == 0:
                self.effects["burning"]["is"] == False
        else:
            print(f"\n{self.name} hoří a ztrácí 15 HP.\n")
            self.hp -= 15
            self.effects["burning"]["duration"] -= 1
            if self.effects["burning"]["duration"] <= 0:
                self.effects["burning"]["is"] = False
                print(f"{self.name} přestal hořet.\n")

    if self.effects["poisoned"]["is"] == True:
        if self.effects["poisoned"]["duration"] == 0:
            self.effects["poisoned"]["is"] == False
        else:
            print(f"\n{self.name} je otráven a ztrácí 5 HP.\n")
            self.hp -= 5
            self.effects["poisoned"]["duration"] -= 1
            if self.effects["poisoned"]["duration"] <= 0:
                self.effects["poisoned"]["is"] = False
                print(f"{self.name} přestal být otráven.\n")

    if self.effects["stunned"]["is"] == True:
        if self.effects["stunned"]["duration"] == 0:
            self.effects["stunned"]["is"] = False
            print(f"{self.name} se zotavil z omráčení.\n")
        else:
            self.effects["stunned"]["duration"] -= 1
            print(f"\n{self.name} je omráčen a nemůže se hýbat toto kolo.\n")
            # časový limit pro omráčení, např. 1

    if self.effects["frozen"]["is"] == True:
        if self.effects["frozen"]["duration"] == 0:
            self.effects["frozen"]["is"] = False
            self.skill += 0.5
            print(f"{self.name} se zotavil z omrznutí.\n")
        else:
            self.effects["frozen"]["duration"] -= 1
            print(f"\n{self.name} je zmrzlý.\n")
            #časový limit pro zmrazení, např. 1 partly stunned

    if self.effects["healing"]["is"] == True:
        if self.effects["healing"]["duration"] == 0:
            self.h_amount = 0
            self.effects["healing"]["is"] == False
        else:
            print(f"\n{self.name} se léčí a získává {h_amount} HP.\n")
            self.hp += h_amount
            self.effects["healing"]["duration"] -= 1
            if self.effects["healing"]["duration"] <= 0:
                self.effects["healing"]["is"] = False
                print(f"{self.name} přestal regenerovat HP.\n")
                
    if self.effects["stamina regen"]["is"] == True:
        if self.effects["stamina regen"]["duration"] == 0:
            self.s_amount = 0
            self.effects["stamina regen"]["is"] = False
        else:
            print(f"\n{self.name} regeneruje {s_amount} staminy.\n")
            self.stamina += s_amount
            self.effects["stamina regen"]["duration"] -= 1
            if self.effects["stamina regen"]["duration"] <= 0:
                self.effects["stamina regen"]["is"] = False
                print(f"{self.name} přestal regenerovat staminu.\n")
    #if self.effects["shielding"]["is"] == True:
        # if self.effects["shielding"]["duration"] == 0:
        #     self.effects["shielding"]["is"] = False
        #     print(f"{self.name} se přetal bránit.\n")
        # else:
        #     self.effects["shielding"]["duration"] -= 1
        #     print(f"\n{self.name} se brání .\n")
    else:
        pass

    self.is_alive_check()

def potion_usage(self, potion_type):
    if self.elixiers[potion_type]["own"] > 0:
        self.elixiers[potion_type]["own"] -= 1
        print(f"{self.name} nyní má {self.elixiers[potion_type]['own']} kusů lektvaru {potion_type}.")
    else:
        print(f"{self.name} nemá žádné {potion_type}. Zkus to znovu.")
        self.potion()

def potion_effect(self, potion_type):
        if potion_type == "healing potion":
            self.potion_usage("healing potion")
            time.sleep(0.7)
            self.hp += self.elixiers[potion_type]["amount"]
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount']} HP.")
            print(f"{self.name} má nyní {self.hp} HP.")
            time.sleep(1)

        elif potion_type == "stamina potion":
            self.potion_usage("stamina potion")
            time.sleep(0.7)
            self.stamina += self.elixiers[potion_type]["amount"]
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount']} staminy.")
            print(f"{self.name} má nyní {self.stamina} staminy.")
            time.sleep(1)

        elif potion_type == "mana potion":
            self.potion_usage("mana potion")
            time.sleep(0.7)
            self.mana += self.elixiers[potion_type]["amount"]
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount']} many.")
            print(f"{self.name} má nyní {self.mana} many.")
            time.sleep(1)

        elif potion_type == "vlaštovka":
            self.elixiers[potion_type]["duration"] = 4 # Reset amount for next use
            self.potion_usage("vlaštovka")
            time.sleep(0.7)
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount']} HP.")
            self.hp += self.elixiers[potion_type]["amount"]
            print(f"{self.name} má nyní {self.hp} HP.")
            self.effects["healing"]["is"] = True
            self.effects["healing"]["duration"] = self.elixiers["vlaštovka"]["duration"]
            self.h_amount = self.elixiers[potion_type]["amount"]
            self.apply_effects(self.h_amount, 0)
            print(f"{self.name} bude regenerovat {self.elixiers[potion_type]['amount']} HP po dobu {self.elixiers[potion_type]['duration']} kol.")
            print(f"{self.name} má nyní {self.hp} HP.\n")
            time.sleep(1)
            
        elif potion_type == "hrom":
            self.potion_usage("hrom")
            time.sleep(0.7)
            self.skill *= self.elixiers[potion_type]["amount"]
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount']} krát víc síly.")
            print(f"{self.name} má nyní sílu {self.skill * 100}%.")
            time.sleep(1)

        elif potion_type == "vlk":
            self.potion_usage("vlk")
            time.sleep(0.7)
            self.skill += self.elixiers[potion_type]["amount"]
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount'] * 100}% síly.")
            print(f"{self.name} má nyní sílu {self.skill * 100}%.")
            time.sleep(1)

        elif potion_type == "medvěd":
            self.potion_usage("medvěd")
            time.sleep(0.7)
            self.defense += self.elixiers[potion_type]["amount"]
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount'] * 100}% obrany.")
            print(f"{self.name} má nyní {self.defense} štítu.")
            time.sleep(1)
        
        elif potion_type == "blizzard":
            self.elixiers[potion_type]["duration"] = 4
            self.potion_usage("blizzard")
            time.sleep(0.7)
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount']} Stamina.")
            self.stamina += self.elixiers[potion_type]["amount"]
            print(f"{self.name} má nyní {self.stamina} staminy.")
            self.effects["stamina regen"]["is"] = True
            self.effects["stamina regen"]["duration"] = self.elixiers[potion_type]["duration"]
            self.s_amount = self.elixiers[potion_type]["amount"]
            self.apply_effects(0, self.s_amount)
            print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount']} staminy.")
            print(f"{self.name} bude regenerovat {self.elixiers[potion_type]['amount']} Stamina po dobu {self.elixiers[potion_type]['duration']} kol.")
            print(f"{self.name} má nyní {self.stamina} staminy.\n")
            time.sleep(1)
        else:
            print(f"{self.name} nemá žádný takový lektvar. Zkus to znovu.")
            self.potion()
            return
            
        
def potion(self):
    print("\nDostupné lektvary:\n"
            f"1. Healing Potion  (léčí 50 HP)                           [kusů : {self.elixiers['healing potion']['own']}]\n"
            f"2. Stamina Potion  (regeneruje 45 staminy)                [kusů : {self.elixiers['stamina potion']['own']}]\n"
            f"3. Mana Potion     (regeneruje 35 many)                   [kusů : {self.elixiers['mana potion']['own']}]\n"
            f"4. Vlaštovka       (regeneruje 15 HP po dobu 3 kol)       [kusů : {self.elixiers['vlaštovka']['own']}]\n"
            f"5. Hrom            (zvyšuje násobí 1.5 krát sílu)         [kusů : {self.elixiers['hrom']['own']}]\n"
            f"6. Vlk             (zvyšuje sílu o 15%)                   [kusů : {self.elixiers['vlk']['own']}]\n"
            f"7. Medvěd          (zvyšuje obranu o 25%)                 [kusů : {self.elixiers['medvěd']['own']}]\n"
            f"8. Blizzard        (regeneruje 20 staminu po dobu 3 kol)  [kusů : {self.elixiers['blizzard']['own']}]\n")
    
    potion_type = input("Vyber si lektvar (číslo): ").strip().lower()
    if potion_type.isdigit():
        potion_type = int(potion_type)

        if potion_type == 1:
            self.potion_effect("healing potion")
        elif potion_type == 2:
            self.potion_effect("stamina potion")
        elif potion_type == 3:
            self.potion_effect("mana potion")
        elif potion_type == 4:
            self.potion_effect("vlaštovka")
        elif potion_type == 5:
            self.potion_effect("hrom")
        elif potion_type == 6:
            self.potion_effect("vlk")
        elif potion_type == 7:
            self.potion_effect("medvěd")
        elif potion_type == 8:
            self.potion_effect("blizzard")
        else:
            print("Zadali jste špatné číslo, zkuste to znovu.")
            self.potion()
    else:
        print("\nNeplatný vstup. Zkus to znovu.\n")
        self.potion()



def use_item(self):
    while True:
        item_choice = input("Vyber si nástroj (číslo): ").strip()

        if item_choice.isdigit():
            item_choice = int(item_choice)

            if 1 <= item_choice <= len(Hero.equip):
                item_name = list(Hero.equip.keys())[item_choice - 1]

                if Hero.equip[item_name]:
                    print("")
                    if item_name == "bomb":
                        if Hero.equip[item_name]['own'] == True:
                            print(f"Máš {item_name} ten dává {Hero.equip[item_name]['dmg']} základního poškození.")
                            bomb_attack = Attack(Hero, "Bomb", base_dmg=Hero.equip[item_name]['dmg'], dmg_type="explosive")
                            Enemy.take_damage(bomb_attack)
                            print(f"{Enemy.name} má nyní {Enemy.hp} HP.")
                            Hero.equip[item_name]['own'] = False 
                            break
                        else:
                            print(f"\nNemáš {item_name}. Zkus to znovu.\n")
                            Hero.use_item()
                        time.sleep(2)

                    elif item_name == "poison bomb":
                        if Hero.equip[item_name]['own'] == True:
                            print(f"{Hero.name} použil {item_name} a způsobil {Hero.equip[item_name]['dmg']} poškození s efektem otravy.")
                            poison_attack = Attack(Hero, "Poison Bomb", base_dmg=Hero.equip[item_name]['dmg'], dmg_type="explosive", effects=["poisoned"])
                            Enemy.take_damage(poison_attack)
                            print(f"{Enemy.name} má nyní {Enemy.hp} HP.")
                            Hero.equip[item_name]['own'] = False 
                            break
                        else:
                            print(f"\nNemáš {item_name}. Zkus to znovu.\n")
                            Hero.use_item()
                        time.sleep(2)

                    elif item_name == "fire bomb":
                        if Hero.equip[item_name]['own'] == True:
                            print(f"{Hero.name} použil {item_name} a způsobil {Hero.equip[item_name]['dmg']} poškození s efektem hoření.")
                            fire_attack = Attack(Hero, "Fire Bomb", base_dmg=Hero.equip[item_name]['dmg'], dmg_type="explosive", effects=["burning"])
                            Enemy.take_damage(fire_attack)
                            print(f"{Enemy.name} má nyní {Enemy.hp} HP.")
                            Hero.equip[item_name]['own'] = False
                            break
                        else:
                            print(f"\nNemáš {item_name}. Zkus to znovu.\n")
                            Hero.use_item()
                        time.sleep(2)
                    
                    elif item_name == "frost bomb":
                        if Hero.equip[item_name]['own'] == True:
                            print(f"{Hero.name} použil {item_name} a způsobil {Hero.equip[item_name]['dmg']} poškození s efektem zmrazení.")
                            frost_attack = Attack(Hero, "Frost Bomb", base_dmg=Hero.equip[item_name]['dmg'], dmg_type="explosive", effects=["frozen"])
                            Enemy.take_damage(frost_attack)
                            print(f"{Enemy.name} má nyní {Enemy.hp} HP.")
                            Hero.equip[item_name]['own'] = False  # Remove the item after use
                            break
                        else:
                            print(f"\nNemáš {item_name}. Zkus to znovu.\n")
                            Hero.use_item()
                        time.sleep(2)
                    
                    else :
                        if Hero.equip[item_name]['own'] == True:
                            Hero.skill += Hero.equip[item_name]["dmg_mutipl"]  # Apply the multiplier if the item is owned
                            print(f"""Máš {item_name} a ten ti zlepšuje sílu o {Hero.equip[item_name]["dmg_mutipl"] * 100:.0f}%.""")
                            print(f"{Hero.name} má nyní sílu {Hero.skill * 100:.0f}%.")
                            Hero.equip[item_name]['own'] = False
                            break
                        else:
                            print(f"\nNemáš {item_name} nebo jej už používáš. Zkus to znovu.\n")
                            Hero.use_item()
                        time.sleep(2)

                else:
                    print(f"\nNemáš {item_name}.Zkus to znovu.\n")
                    continue
            else:
                print("\nNeplatná volba.\n")
                continue
    
        else:
            print("Zadej číslo nástroje.\n")
            continue




# def nameing(self):
#     name = input("-- Zadej jméno: ").strip()
#     if not name:
#         print("--> Jméno nesmí být prázdné.\n")
#         self.nameing()
#     elif name.isdigit():
#         print("--> Jméno nesmí být číslo.\n")
#         self.nameing()
#     else:
#         while True:
#             change_name = input(f"\n-- Chceš změnit jméno ? (y/n): ").strip().lower()
#             if change_name == 'y':
#                 self.nameing()
#                 break
#             elif change_name == 'n':
#                 Hero.name = name
#                 return
#             else:
#                 print("--> Neplatná volba, zkus to znovu.")
            


# def classing(self):
#     print("1. Witcher\n"
#             "2. Sorcerer\n"
#             "3. Archer\n"
#             "4. Jarl\n"
#             "5. Bard\n"
#             "6. Monster\n")
#     while True:
#         char_class = input("Zadej číslo třídy: ").strip()
#         if not char_class.isdigit():
#             print("--> Neplatný vstup, zkus to znovu.\n")
#             continue
#         char_class = int(char_class)
#         if char_class == 1:
#             return Witcher(self.name)
#         elif char_class == 2:
#             return Sorcerer(self.name)
#         elif char_class == 3:
#             return Archer(self.name)
#         elif char_class == 4:
#             return Jarl(self.name)
#         elif char_class == 5:
#             return Bard(self.name)
#         elif char_class == 6:
#             return Monster(self.name)
#         else:
#             print("--> Neplatná třída, zkus to znovu.\n")

# def en_classing(self, char_class):
#     if char_class == "Witcher":
#         return Witcher(self.name)
#     elif char_class == "Sorcerer":
#         return Sorcerer(self.name)
#     elif char_class == "Archer":
#         return Archer(self.name)
#     elif char_class == "Jarl":
#         return Jarl(self.name)
#     elif char_class == "Bard":
#         return Bard(self.name)
#     elif char_class == "Monster":
#         return Monster(self.name)
#     else:
#         print("--> Neplatná třída, zkus to znovu.\n")





# class Witcher(Character):
#     def __init__(self, name):
#         super().__init__(name, "Witcher")
#         self.hp = 150
#         self.mana = 35
#         self.defense = 25
#         self.skill = 1.2
#         self.equip["siderite sword"] = {"own":True,"dmg_mutipl": 0.25}
#         self.abilities = {"Steel Sword" : "30 až 40 dmg" ,
#                             "Silver Sword" : "25 až 35 nebo 40 až 50 dmg pro monstra",}
#         self.signs = {
#             "Igni": "Ohnivý útok; 30 dmg a hoření za 15",               # burning 3 rounds
#             "Aard": "Magické odhození; 20 dmg a stun na 1 kolo",        # stunned 1 round
#             "Quen": "Kouzelná zeď; zvýší def o 30 za cenu 20 hp",       # giant def 1 round 
#             "Axii": "Proud síly; doplní 20 many",                       # mana + 20 
#             "Yrden": "Magické posílení; zlepší útoky o 10%",            # skill +
#             "Heliotrop": "Kouzelný štít; zlepší def o 10"}              # def +
        
#     def witcher_attacking(self):
#         while True:
#             time.sleep(1)
#             choice = input("Vyber si útok nebo znamení (|x| - napiš x): ").strip()
#             if choice.isdigit():
#                 choice = int(choice)
                
#                 if 1 <= choice <= 2 :
#                     if choice == 1:
#                         print(f"\n{Hero.name} použil útok Silver Sword.")
#                         Hero.silver_sword(Enemy)
                        
#                     elif choice == 2:
#                         print(f"\n{Hero.name} použil útok Steel Sword.")
#                         Hero.steel_sword(Enemy)

#                     print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
#                     break
                
#                 elif 11 <= choice <= len(Hero.signs) + 10:
#                     print(f"Mana: {Hero.mana}/100")
#                     Hero.use_sign(Enemy, choice)
#                     time.sleep(2)
#                     print(f"\n{Hero.name} má nyní {Hero.mana}/100 many.")
#                     print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
#                     break

#                 else:
#                     print("\nNeplatná volba. Zkus to znovu.\n")
#                     continue
#             else:
#                 print("\nNeplatná volba. Zkus to znovu.\n")
#                 continue
                
        
#     def steel_sword(self, target):
#         steel_sword_attack = Attack(self, "Steel Sword", base_dmg=random.randint(30, 40), dmg_type="slash", effects=["bleeding"])  # steel sword is more effective against humans 35 if enemy.char_class != "Monster" else 20
#         target.take_damage(steel_sword_attack)
#         target.effects["bleeding"]["duration"] += 3 
#         target.effects["bleeding"]["is"] = True

        
#     def silver_sword(self, target):
#         base = random.randint(40, 50) if Enemy.char_class == "Monster" else random.randint(25, 35)
#         silver_sword_attack = Attack(self, "Silver Sword", base_dmg= base, dmg_type="slash", effects = ["bleeding"],)  # silver sword is more effective against monsters 45 if enemy.char_class == "Monster" else 30
#         target.take_damage(silver_sword_attack)
#         target.effects["bleeding"]["duration"] += 3 
#         target.effects["bleeding"]["is"] = True   # Set bleeding duration to 3 rounds 
        
        

#     def use_sign(self, target, choice):
#         while True:
#             sign_choice = choice

#             if sign_choice < 11 or sign_choice > len(self.signs) + 10:
#                 print("\nNeplatné číslo znamení. Zkus to znovu.\n")
#                 continue

#             if not sign_choice == 14 and self.mana < 10:
#                 print("\nNemáš dost many na použití znamení.\n")
#                 break

#             if sign_choice == 11:
#                 print(f"\n{self.name} použil znamení Igni a zapálil nepřítele.")
#                 time.sleep(1)
#                 igni_attack = Attack(Hero, "Igni", base_dmg=30, dmg_type="fire", effects=["burning"])
#                 self.mana -= 10  # Reduce mana for using the sign
#                 time.sleep(1)
#                 target.take_damage(igni_attack)
#                 target.effects["burning"]["duration"] += 3
#                 target.effects["burning"]["is"] = True
#                 break
            
#             elif sign_choice == 12:
#                 print(f"\n{self.name} použil znamení Aard a omráčil nepřítele.")
#                 time.sleep(1)
#                 aard_attack = Attack(Hero, "Aard", base_dmg=20, dmg_type="stun", effects=["stunned"])
#                 self.mana -= 10  
#                 time.sleep(1)
#                 target.take_damage(aard_attack)
#                 global delay
#                 delay += 1
#                 break
            
#             elif sign_choice == 13:
#                 time.sleep(1)
#                 self.defense += 30
#                 self.hp -= 20
#                 self.mana -= 10
#                 print(f"\n{self.name} použil znamení Quen a zvýšil svou obranu na {self.defense}. A nyní má {self.hp} HP.")
#                 break
            
#             elif sign_choice == 14:
#                 print(f"\n{self.name} použil znamení Axii a získal 20 many.")
#                 self.mana = min(self.mana + 20, 100)  # Ensure mana does not exceed max
#                 break
            
#             elif sign_choice == 15:
#                 self.skill += 0.1
#                 self.mana -= 10  
#                 print(f"\n{self.name} použil znamení Yrden a zvýšil svou dovednost na {self.skill * 100:.0f}%.")
#                 break
                
#             elif sign_choice == 16:
#                 self.defense += 10
#                 self.mana -= 10 
#                 print(f"\n{self.name} použil znamení Heliotrop a zvýšil svou obranu na {self.defense}.")
#                 break
                    
#             else:
#                 print("Neplatné znamení. Dostupné možnosti:")
#                 for sign in self.signs:
#                     print(f" - {sign.capitalize()}")
#                 continue


# class Sorcerer(Character):
#     def __init__(self, name):
#         super().__init__(name, "Sorcerer")
#         self.hp = 120
#         self.stamina = 0
#         self.mana = 100
#         self.defense = 15
#         self.t_cooldown = 3
#         self.equip["dimeritium staff"] = {"own":True,"dmg_mutipl": 0.25}
#         self.abilities = {"Fireball" : "30 až 45 dmg a hoření",
#                            "Thunder" : "60 az 70 dmg ale jen 1 použití za 3 kola",
#                             "Ice Spike" : "20 až 35 dmg a zmrazení",
#                             "Smite" : "50 až 60 dmg ignorujících def"}  # fireball is more effective against humans 30 if enemy.char_class != "Monster" else 20
        
#     def sorcerer_attacking(self):
#         while True:
#             time.sleep(1)
#             choice = input("\nVyber si magický útok (|x| - napiš x): ").strip()
#             if choice.isdigit():
#                 choice = int(choice)

#                 if 1 <= choice <= 4 :
#                     if choice == 1:
#                         print(f"\n{Hero.name} použil útok Fire ball!!.")
#                         Hero.fireball(Enemy)
                        
#                     elif choice == 2:
#                         if round_counter  < 4:
#                             print("\nBlesk můžeš použít až na 4. kole.")
#                             continue
#                         else:
#                             print(f"\n{Hero.name} použil útok Thunder!!.")
#                             Hero.thunder(Enemy)

#                     elif choice == 3:
#                         print(f"\n{Hero.name} použil útok Ice Spike!!.")
#                         Hero.icespike(Enemy)
#                         print(f"\n{Enemy.name} je zmrzlý, další dvě kola má sílu nižší o 50%.\n")

#                     elif choice == 4:
#                         print(f"\n{Hero.name} použil útok Smite!!.")
#                         Hero.smite(Enemy)

#                     print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
#                     break
#                 else:
#                     print("Neplatná volba. Zkus to znovu.")
#                     continue
#             else:
#                 print("Neplatná volba. Zkus to znovu.")
#                 continue

#     def thunder(self, target):
#         if (round_counter + 3) - self.t_cooldown > 3:
#             self.mana_check()
#             thunder_attack = Attack(self, "Thunder", base_dmg=random.randint(60, 70), dmg_type="magick", effects=None)  # steel sword is more effective against humans 35 if enemy.char_class != "Monster" else 20
#             target.take_damage(thunder_attack)
#             self.t_cooldown = round_counter + 3
#         else: 
#             print(f"Blesk můžeš použít až za {self.t_cooldown - round_counter}")
#             return 

#     def fireball(self, target):
#         self.mana_check()
#         fireball_attack = Attack(self, "Fireball", base_dmg=random.randint(30, 45), dmg_type="fire", effects=["burning"])
#         target.take_damage(fireball_attack)
#         target.effects["burning"]["duration"] += 3  # Set burning duration to 3 rounds
#         target.effects["burning"]["is"] = True  # Apply burning effect
    
#     def icespike(self, target):
#         self.mana_check()
#         icespike_attack = Attack(self, "Ice Spike", base_dmg=random.randint(20, 35), dmg_type="ice", effects=["frozen"])
#         target.take_damage(icespike_attack)
#         target.effects["frozen"]["duration"] += 2  # Set frozen duration to 2 rounds
#         target.effects["frozen"]["is"] = True  # Apply frozen effect
#         if target.skill > 0.5:
#             target.skill -= 0.5  # Reduce target's skill by 50%
#         else:
#             target.skill = 0
#             print(f"{target.name} je zcela zmražen a jeho síla je snížena na 0%.")

#     def smite(self, target):
#         self.mana_check()
#         d = target.defense
#         target.defense = 0
#         smite_attack = Attack(self, "Smite", base_dmg=random.randint(50, 60), dmg_type="fire", effects=None)
#         target.take_damage(smite_attack)
#         target.defense = d


# class Archer(Character):
#     def __init__(self, name):
#         super().__init__(name, "Archer")
#         self.hp = 130
#         self.defense = 20
#         self.equip["brokilon bow"] = {"own":True,"dmg_mutipl": 0.25}
#         self.abilities = {"Arrow Rain" : "4 až 8 krát poškodí za 10 dmg", 
#                           "Poison Arrow" : "20 až 25 dmg a otrávení", 
#                           "Explosive Arrow" : "60 až 80 dmg, objetování 20 až 30 hp a šance na zapálení nepřítele"}
        
#     def archer_attacking(self):
#         while True:
#             time.sleep(1)
#             choice = input("\nVyber si útok (|x| - napiš x): ").strip()
#             if choice.isdigit():
#                 choice = int(choice)
                
#                 if 1 <= choice <= 3 :
#                     if choice == 1:
#                         print(f"\n{Hero.name} použil útok Arrow Rain!!.")
#                         Hero.arrow_rain(Enemy)
                        
#                     elif choice == 2:
#                         print(f"\n{Hero.name} použil útok Poison Arrow!!.")
#                         Hero.poison_arrow(Enemy)

#                     elif choice == 3:
#                         print(f"\n{Hero.name} použil útok Explosive Arrow!!.")
#                         Hero.explosive_arrow(Enemy)
#                         print(f"{Hero.name} má nyní {Hero.hp} HP")

#                     print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
#                     break
#                 else:
#                     print("Neplatná volba. Zkus to znovu.")
#                     continue
#             else:
#                 print("Neplatná volba. Zkus to znovu.")
#                 continue
        
#     def arrow_rain(self, target):
#         self.stamina_check()
#         arrow_rain_attack = Attack(self, "Arrow Rain", base_dmg=random.randint(4, 8) * 10, dmg_type="piercing", effects=None)
#         target.take_damage(arrow_rain_attack)
    
#     def poison_arrow(self, target):
#         self.stamina_check()
#         poison_arrow_attack = Attack(self, "Poison Arrow", base_dmg=random.randint(20, 25), dmg_type="piercing", effects=["poisoned"])
#         target.take_damage(poison_arrow_attack)
#         target.effects["poisoned"]["duration"] += 3
#         target.effects["poisoned"]["is"] = True  # Apply poisoned effect

#     def explosive_arrow(self, target):
#         self.stamina_check()
#         explosive_arrow_attack = Attack(self, "Explosive Arrow", base_dmg=random.randint(60, 80), dmg_type="explosive", effects=None)
#         target.take_damage(explosive_arrow_attack)
#         self.hp -= random.randint(20, 30)  # Self-damage from explosion
#         if random.randint(1, 3) == 2:  # 50% chance to ignite the target
#             target.effects["burning"]["duration"] += 3  # Set burning duration to 3 rounds
#             target.effects["burning"]["is"] = True  # Apply burning effect
#         else:
#             pass


# class Jarl(Character):
#     def __init__(self, name):
#         super().__init__(name, "Jarl")
#         self.hp = 140
#         self.defense = 30
#         self.equip["skellige axe"] = {"own":True,"dmg_mutipl": 0.25}
#         self.abilities = {"War cry" : "20 až 30 HP a 5 až 10 def",
#                         "Bloody slash" : "30 až 40 dmg a silné krvácení",
#                         "Battle Roar" : "- 5 až 15 nepřátelské def a šance na omráčení nepřítele pro toto a další kolo"}
        
#     def jarl_attacking(self):
#         while True:
#             time.sleep(1)
#             choice = input("\nVyber si útok (|x| - napiš x): ").strip()
#             if choice.isdigit():
#                 choice = int(choice)
                
#                 if 1 <= choice <= 3 :
#                     if choice == 1:
#                         print(f"\n{Hero.name} použil útok War Cry!!.")
#                         Hero.war_cry(Enemy)
                        
#                     elif choice == 2:
#                         print(f"\n{Hero.name} použil útok Bloody slash!!.")
#                         Hero.bloody_slash(Enemy)

#                     elif choice == 3:
#                         print(f"\n{Hero.name} použil útok Battle Roar!!.")
#                         Hero.battle_roar(Enemy)

#                     print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
#                     break
#                 else:
#                     print("Neplatná volba. Zkus to znovu.")
#                     continue
#             else:
#                 print("Neplatná volba. Zkus to znovu.")
#                 continue

        
#     def war_cry(self, target):
#         self.stamina_check()
#         self.hp += random.randint(20, 30)
#         self.defense += random.randint(5, 10)
#         print(f"{self.name} použil bojový pokřik a získal {self.hp} HP a {self.defense} obrany.")

#     def bloody_slash(self, target):
#         self.stamina_check()
#         bloody_slash_attack = Attack(self, "Bloody Slash", base_dmg=random.randint(30, 40), dmg_type="slash", effects=["bleeding"])
#         target.take_damage(bloody_slash_attack)
#         target.effects["bleeding"]["duration"] += 5
#         target.effects["bleeding"]["is"] = True

#     def battle_roar(self, target):
#         self.stamina_check()
#         if target.defense - random.randint(5, 15) > 0 :
#             target.defense -= random.randint(5, 15)
#         else:
#             pass
         
#         print(f"{target.name} má nyní {target.defense} obrany.")
#         if random.randint(1, 5) == 3:
#             print(f"{target.name} je omráčen.")
#             target.effects["stunned"]["duration"] += 1  # Set burning duration to 3 rounds
#             target.effects["stunned"]["is"] = True  # Apply burning effect
#         else:
#             pass



# class Bard(Character):
#     def __init__(self, name):
#         super().__init__(name, "Bard")
#         self.hp = 170
#         self.stamina = 80
#         self.defense = 10
#         self.respect = 100
#         self.equip["elven lute"] = {"own":True,"dmg_mutipl": 0.25}
#         self.abilities = {"Taunt" : "5 až 10 dmg, - 5 až 10 staminy a def nepříteli a 20 respektu. pokud máš více než 150 respektu máš i šanci na instakill",
#                           "Power song" : "15 až 25 def a 20 až 30 staminy ",
#                           "Melody of Browl" : "25 až 35 dmg a otrávení"}
        
#     def bard_attacking(self):
#         while True:
#             time.sleep(1)
#             choice = input("\nVyber si útok (|x| - napiš x): ").strip()
#             if choice.isdigit():
#                 choice = int(choice)
                
#                 if 1 <= choice <= 3 :
#                     if choice == 1:
#                         print(f"\n{Hero.name} použil útok Taunt!!.")
#                         Hero.taunt(Enemy)
#                         print(f"{Enemy.name} má nyní {Enemy.stamina} staminy a {Enemy.defense} obrany.")
                        
#                     elif choice == 2:
#                         print(f"\n{Hero.name} použil útok Power song!!.")
#                         Hero.power_song(Enemy)
#                         print(f"{Hero.name} zpívá mocnou píseň a získává {Hero.defense} obrany a {Hero.stamina} staminy.")

#                     elif choice == 3:
#                         print(f"\n{Hero.name} použil útok Melody of brawl!!.")
#                         Hero.melody_of_browl(Enemy)

#                     print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
#                     break
#                 else:
#                     print("Neplatná volba. Zkus to znovu.")
#                     continue
#             else:
#                 print("Neplatná volba. Zkus to znovu.")
#                 continue

#     def taunt(self, target):
#         self.stamina_check()
#         if self.respect > 150 and random.randint(1, 20) == 17:
#             target.hp -= target.hp + 1
#             print("Nepřítel nesnesl tvoji urážku a spadl na zem mrtví. Gratuluji urazil jsi nepřítele tak moc že to nepřežil.")
            
#         taunt_attack = Attack(self, "Taunt", base_dmg=random.randint(5, 10), dmg_type="slash", effects=None)
#         target.take_damage(taunt_attack)
#         target.stamina -= random.randint(5, 10)
#         target.defense -= random.randint(5, 10)
#         self.respect += 20

#     def power_song(self, target):
#         self.stamina_check()
#         self.defense += random.randint(15, 25)
#         self.stamina += random.randint(20, 30)

#     def melody_of_browl(self, target):
#         self.stamina_check()
#         melody_attack = Attack(self, "Melody of Brawl", base_dmg=random.randint(25, 35), dmg_type="slash", effects=["poisoned"])
#         target.take_damage(melody_attack)
#         target.effects["poisoned"]["duration"] += 2
#         target.effects["poisoned"]["is"] = True

# class Monster(Character):
#     def __init__(self, name):
#         super().__init__(name, "Monster")
#         self.hp = 160
#         self.defense = 20
#         self.equip["iron claws"] = {"own":True,"dmg_mutipl": 0.25}
#         self.abilities = {"Claw Swipe" : "2 krát 15 až 25 dmg a krvácení",
#                            "Bite" : "20až 30 dmg, krvácení a otrávení",
#                             "Ripping clutches" : "25 až 35 dmg a silné krvácení"}  # smash attack
        
#     def monster_attacking(self):
#         while True:
#             time.sleep(1)
#             choice = input("\nVyber si útok (|x| - napiš x): ").strip()
#             if choice.isdigit():
#                 choice = int(choice)
                
#                 if 1 <= choice <= 3 :
#                     if choice == 1:
#                         print(f"\n{Hero.name} použil útok Claw Swipe!!.")
#                         Hero.claw_swipe(Enemy)
                        
#                     elif choice == 2:
#                         print(f"\n{Hero.name} použil útok Bite!!.")
#                         Hero.bite(Enemy)

#                     elif choice == 3:
#                         print(f"\n{Hero.name} použil útok Ripping clutches!!.")
#                         Hero.ripping_clutches(Enemy)

#                     print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
#                     break
#                 else:
#                     print("Neplatná volba. Zkus to znovu.")
#                     continue
#             else:
#                 print("Neplatná volba. Zkus to znovu.")
#                 continue

#     def claw_swipe(self, target):
#         self.stamina_check()
#         claw_swipe_attack = Attack(self, "Claw Swipe", base_dmg=random.randint(15, 25) * 2, dmg_type="slash", effects=["bleeding"])
#         target.take_damage(claw_swipe_attack)
#         target.effects["bleeding"]["duration"] += 3
#         target.effects["bleeding"]["is"] = True

#     def bite(self, target):
#         self.stamina_check()
#         bite_attack = Attack(self, "Bite", base_dmg=random.randint(15, 25) * 2, dmg_type="pierce", effects=["bleeding"])
#         target.take_damage(bite_attack)
#         target.effects["bleeding"]["duration"] += 3
#         target.effects["bleeding"]["is"] = True
#         target.effects["poisoned"]["duration"] += 3  # vyměnít za venom
#         target.effects["poisoned"]["is"] = True

#     def ripping_clutches(self, target):
#         self.stamina_check()
#         ripping_clutches_attack = Attack(self, "Ripping clutches", base_dmg=random.randint(25, 35), dmg_type="slash", effects=["bleeding"])
#         target.take_damage(ripping_clutches_attack)
#         target.effects["bleeding"]["duration"] += 5
#         target.effects["bleeding"]["is"] = True

# # class Dwarf





Enemy = Character(f"{random.choice(enemy_names)}", f"{random.choice(characters)}")  # Initialize Enemy character
Enemy = en_classing(f"{random.choice(characters)}")  

print(f"\nVýtej hráči, tvým úkolem je přežít a porazit nepřítele.")
print(f"\nTvím nepřítelem je {Enemy.name} {random.choice(titles)}, třída: {Enemy.char_class}, HP: {Enemy.hp}, Stamina: {Enemy.stamina}, Mana: {Enemy.mana}, Defense: {Enemy.defense}, Síla: {Enemy.skill * 100}%\n")
time.sleep(2)

# Nameing
print(f"\nNyní si vyber svou postavu:")
Hero = Character("Hero", "")  # Initialize Hero character
Hero.nameing()
print("\n--> Hmm", end='', flush=True)
for _ in range(4):
    time.sleep(0.3)
    print('.', end='', flush=True)
print(f" {Hero.name}, to je dobré jméno! Vítej!!!\n")
time.sleep(3.5)



# Classing
print(f"Vyber si svou třídu:\n")
Hero = Hero.classing()
print(f"\n---> Tvoje postava je {Hero.name}, třída: {Hero.char_class}, HP: {Hero.hp}, Stamina: {Hero.stamina}, Mana: {Hero.mana}, Defense: {Hero.defense}, Síla: {Hero.skill * 100}%\n")
time.sleep(2)
print(f"\nNyní můžeš začít hrát.") 
time.sleep(2)
print("Boj začínáš bez vybavení a vylepšení, jestli chceš použít meč nebo vypít lektvar, musíš na to využít kolo.")
time.sleep(2)
print(f"Poškození způsobuješ díky síle útoků násobenou vlastní silou -> {Hero.skill * 100}%")
time.sleep(2)
print("Ale neměj strách, protivník se připravuje, takže první dvě kola na tebe nezaútočí.")


# Game loop
    
while alive:
    time.sleep(2)
    print("\n")
    print(f"\nKolo : {round_counter}\n")
    time.sleep(1)
    Hero.apply_effects(Hero.h_amount, Hero.s_amount) # Apply effects at the start of each round
    Enemy.apply_effects(Enemy.h_amount, Enemy.s_amount)
    time.sleep(1)

    while True:
        if Hero.effects["stunned"]["is"] == True:
            print(f"\n{Hero.name} je omráčený.")
        else:
            print("\nZde jsou dostupné akce: \n"
                "1. Ůtočení\n"
                "2. Elixíry\n"
                "3. Nástroje a výstroj\n"
                "4. Zkontroluj svůj stav a stav nepřítele\n"
                "5. Exit Game\n")
            
            action = input("Vyber si: ").strip().lower()
            if action.isdigit():
                action = int(action)

                if action == 1 :
                    print(f"\nVyber si svůj útok--> \n")

                    if Hero.char_class == "Sorcerer" :
                        print(f"Jako mág můžeš používat jen magii.")
                        print(f"Tvé schopnosti jsou: \n")
                        for x, (ability) in enumerate(Hero.abilities):
                            print(f"|{x +1}|{ability} : {Hero.abilities[ability]}")
                        
                        Hero.sorcerer_attacking()
                    

                    elif Hero.char_class == "Witcher" :
                        print(f"Jako zaklínač jsi velmi schopný bojovník s mečem i magií, proto máš {Hero.skill * 100}% síly.\n")
                        print(f"Tvé schopnosti jsou: ")
                        for x, (ability) in enumerate(Hero.abilities):
                            print(f"|{x +1}|{ability} : {Hero.abilities[ability]}")
                        
                        print(f"\nJako zklínač můžeš používat i znamení (cena --> 10 many) :\n")
                        time.sleep(1)

                        for x, (key, value) in enumerate(Hero.signs.items()):
                            print(f"|1{x + 1}|{key} - {value}")
                        print("")
                        Hero.witcher_attacking()
                            

                    elif Hero.char_class == "Archer":
                        print(f"Jako lukostřelec můžeš používat útoky na dálku.")
                        print(f"Tvé schopnosti jsou: \n")
                        for x, (ability) in enumerate(Hero.abilities):
                            print(f"|{x +1}|{ability} : {Hero.abilities[ability]}")
                        
                        Hero.archer_attacking()

                    elif Hero.char_class == "Jarl":
                        print(f"Jako Jarl můžeš používat jen bojové schopnosti.")
                        print(f"Tvé schopnosti jsou: \n")
                        for x, (ability) in enumerate(Hero.abilities):
                            print(f"|{x +1}|{ability} : {Hero.abilities[ability]}")
                        
                        Hero.jarl_attacking()

                    elif Hero.char_class == "Bard":
                        print(f"Jako Bard můžeš používat hudbu a přesvědčování.")
                        print(f"Tvé schopnosti jsou: \n")
                        for x, (ability) in enumerate(Hero.abilities):
                            print(f"|{x +1}|{ability} : {Hero.abilities[ability]}")
            
                        Hero.bard_attacking()

                    elif Hero.char_class == "Monster":
                        print(f"Jako Monstrum můžeš používat je drápy a tesáky.")
                        print(f"Tvé schopnosti jsou: \n")
                        for x, (ability) in enumerate(Hero.abilities):
                            print(f"|{x +1}|{ability} : {Hero.abilities[ability]}")
                        
                        Hero.monster_attacking()

                elif action == 2:
                    print("Pozor lektvarů máš jen omezený počet. Využíj je moudře.")
                    time.sleep(0.5)
                    Hero.potion()
                    time.sleep(1)


                elif action == 3:
                    print(f"Vezmi si svůj nástroj aby sis zvíšil svoji sílu.\n")
                    for index, item in enumerate(Hero.equip, start=1):                                                 
                        print(f"|{index}| {item} - {'Máš možnost použít' if Hero.equip[item]['own'] == True else 'Už jsi použil' }")  

                    print("\nPozor!!!, od každé bomy máš jen jeden kus, takže je používej opatrně.\n")
                    Hero.use_item()                                                                                 # Použití nástroje
                    print(f"{Hero.name} má nyní {Hero.hp} HP a {Hero.skill * 100:.0f}% sílu.")
                    print(f"{Enemy.name} má nyní {Enemy.hp} HP a {Enemy.skill * 100:.0f}% sílu.")


                elif action == 4:
                    print(f"\n{Hero.name} - stav postavy:")
                    print(f"HP: {Hero.hp}")
                    print(f"Stamina: {Hero.stamina}")
                    print(f"Mana: {Hero.mana}")
                    print(f"Defense: {Hero.defense}")
                    print(f"Abilities: {', '.join(Hero.abilities)}")
                    print(f"Efficiency: {Hero.skill * 100:.0f}%")
                    time.sleep(3)

                    print(f"\n{Enemy.name} - stav nepřítele:")
                    print(f"HP: {Enemy.hp}")
                    print(f"Stamina: {Enemy.stamina}")
                    print(f"Mana: {Enemy.mana}")
                    print(f"Defense: {Enemy.defense}")
                    print(f"Abilities: {', '.join(Enemy.abilities)}")
                    print(f"Efficiency: {Enemy.skill * 100:.0f}%\n")
                    time.sleep(3)
                    continue


                elif action == 5:
                    print("Díky za hraní! Nashledanou.\n")
                    alive = False
                    break

                else:
                    print("Něco jsi zadal špatně. Opakuj.")
                    continue
            else:
                print("\nNapiš číslo úkonu.")
                continue


        # Simulace útoku nepřítele
        time.sleep(1)
        if delay > 0:
            print(f"\n{Enemy.name} je neaktivní...")
            delay -= 1
            time.sleep(delay)
        elif Enemy.effects["stunned"]["is"] == True:
            print(f"\n{Enemy.name} je omráčený.")
        else:
            print(f"\n{Enemy.name} je na tahu.")
            time.sleep(0.5)
            if Enemy.hp < Enemy.hp / 2 and Hero.hp > Hero.hp / 2:
                if Enemy.elixiers["healing potion"]["own"] > 0:
                    Enemy.potion_effect("healing potion")
                    print(f"{Enemy.name} se léčí a získává {Enemy.elixiers['healing potion']['amount']} HP.")
                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                else:
                    print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                    pass
                
            elif Enemy.hp < Enemy.hp / 2 and random.randint(1,3) == 2:
                if Enemy.elixiers["healing potion"]["own"] > 0:
                    Enemy.potion_effect("healing potion")
                    print(f"{Enemy.name} se léčí a získává {Enemy.elixiers['healing potion']['amount']} HP.")
                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                else:
                    print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                    pass

            else:
                if Enemy.char_class == "Witcher":
                    if Enemy.stamina > 20:
                        if random.randint(1, 2) == 1:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Magick Slash'! (35 až 45 dmg, šance na omráčení)")
                            magick_slash_attack = Attack(Enemy, "Magick Slash", base_dmg=random.randint(35, 45), dmg_type="slash", effects=["stunned"])
                            Hero.take_damage(magick_slash_attack)
                            if random.randint(1, 3) == 1:
                                Hero.effects["stunned"]["duration"] += 2
                                Hero.effects["stunned"]["is"] = True
                        else:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Sharp Strike'! (30 až 50 dmg a krvácení)")
                            sharp_strike_attack = Attack(Enemy, "Sharp Strike", base_dmg=random.randint(30, 50), dmg_type="slash", effects=["bleeding"])
                            Hero.take_damage(sharp_strike_attack)
                            Hero.effects["bleeding"]["duration"] += 2
                            Hero.effects["bleeding"]["is"] = True
                    else:
                        if Enemy.elixiers["stamina potion"]["own"] > 0:
                            Enemy.potion_effect("stamina potion")
                            print(f"{Enemy.name} získává {Enemy.elixiers['stamina potion']['amount']} staminy.")
                            print(f"{Enemy.name} má nyní {Enemy.stamina} staminy.\n")
                        else:
                            print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                            Enemy.stamina += 10
                            pass

                elif Enemy.char_class == "Sorcerer":
                    if Enemy.mana > 20:
                        if random.randint(1, 2) == 2:
                            Enemy.mana_check()
                            print(f"{Enemy.name} použil kouzlo 'Energy Burn'! (20 až 35 dmg, snížení many nebo staminy)")
                            energy_burn_attack = Attack(Enemy, "Energy Burn", base_dmg=random.randint(20, 35), dmg_type="magic", effects=None)
                            Hero.take_damage(energy_burn_attack)
                            if Hero.mana < 20:
                                Hero.stamina = max(Hero.mana - 20, 0)
                                print(f"{Hero.name} ztrácí 20 staminy!")
                            elif Hero.stamina < 20:
                                Hero.mana = max(Hero.mana - 20, 0)
                                print(f"{Hero.name} ztrácí 20 many!")
                            else:
                                pass
                        
                        else:
                            Enemy.mana_check()
                            print(f"{Enemy.name} použil kouzlo 'Arcane Pulse'! (20 až 40 dmg, šance na snížení obrany)")
                            arcane_pulse_attack = Attack(Enemy, "Arcane Pulse", base_dmg=random.randint(25, 40), dmg_type="magic", effects=None)
                            Hero.take_damage(arcane_pulse_attack)
                            if random.randint(1, 2) == 1:
                                Hero.defense = max(Hero.defense - 10, 0)
                                print(f"{Hero.name} ztrácí 10 obrany!")
                    else:
                        if Enemy.elixiers["mana potion"]["own"] > 0:
                            Enemy.potion_effect("mana potion")
                            print(f"{Enemy.name} získává {Enemy.elixiers['mana potion']['amount']} many.")
                            print(f"{Enemy.name} má nyní {Enemy.mana} many.\n")
                        else:
                            print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                            Enemy.mana += 10
                            pass

                elif Enemy.char_class == "Archer":
                    if Enemy.stamina > 20:
                        if random.randint(1, 2) == 1:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Volley Shot'! (10 až 20 dmg 3 krát)")
                            volley_shot_attack = Attack(Enemy, "Volley Shot", base_dmg=random.randint(10, 20) * 3, dmg_type="piercing", effects=None)
                            Hero.take_damage(volley_shot_attack)
                        else:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Pinning Arrow'! (15 až 25 dmg a šance na omráčení)")
                            pinning_arrow = Attack(Enemy, "Pinning Arrow", base_dmg=random.randint(15, 25), dmg_type="piercing", effects=["stunned"])
                            Hero.take_damage(pinning_arrow)
                            if random.randint(1, 2) == 1:
                                Hero.effects["stunned"]["duration"] += 2
                                Hero.effects["stunned"]["is"] = True
                    else:
                        if Enemy.elixiers["stamina potion"]["own"] > 0:
                            Enemy.potion_effect("stamina potion")
                            print(f"{Enemy.name} získává {Enemy.elixiers['stamina potion']['amount']} staminy.")
                            print(f"{Enemy.name} má nyní {Enemy.stamina} staminy.\n")
                        else:
                            print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                            Enemy.stamina += 10
                            pass


                elif Enemy.char_class == "Jarl":
                    if Enemy.stamina > 20:
                        if random.randint(1, 2) == 1:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Berserker Rage'! (40 až 45 dmg a snížení vlastní obrany)")
                            berserker_rage_attack = Attack(Enemy, "Berserker Rage", base_dmg=random.randint(40, 55), dmg_type="slash", effects=None)
                            Hero.take_damage(berserker_rage_attack)
                            Enemy.defense = max(Enemy.defense - 10, 0)
                            print(f"{Enemy.name} ztrácí 10 obrany kvůli zuřivosti!")
                        else:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Shield Bash'! (20 až 30 dmg a šance na omráčení)")
                            shield_bash_attack = Attack(Enemy, "Shield Bash", base_dmg=random.randint(20, 30), dmg_type="blunt", effects=["stunned"])
                            Hero.take_damage(shield_bash_attack)
                            if random.randint(1, 3) == 1:
                                Hero.effects["stunned"]["duration"] += 2
                                Hero.effects["stunned"]["is"] = True
                    else:
                        if Enemy.elixiers["stamina potion"]["own"] > 0:
                            Enemy.potion_effect("stamina potion")
                            print(f"{Enemy.name} získává {Enemy.elixiers['stamina potion']['amount']} staminy.")
                            print(f"{Enemy.name} má nyní {Enemy.stamina} staminy.\n")
                        else:
                            print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                            Enemy.stamina += 10
                            pass



                elif Enemy.char_class == "Bard":
                    if Enemy.stamina > 20:
                        if random.randint(1, 2) == 1:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} zahrál 'Song of Weakness'! (20 až 25 dmg a sníží sílu)")
                            song_weakness_attack = Attack(Enemy, "Song of Weakness", base_dmg=random.randint(20, 25), dmg_type="psychic", effects=None)
                            Hero.take_damage(song_weakness_attack)
                            Hero.skill = max(Hero.skill - 0.1, 0)
                            print(f"{Hero.name} má nyní sílu {Hero.skill * 100:.0f}%.")
                        else:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} zahrál 'Confusing ballad'! (25 až 30 dmg a šance na omráčení)")
                            confusing_ballad_attack = Attack(Enemy, "Confusing ballad", base_dmg=random.randint(25, 30), dmg_type="psychic", effects=["stunned"])
                            Hero.take_damage(confusing_ballad_attack)
                            if random.randint(1, 2) == 1:
                                Hero.effects["stunned"]["duration"] += 2
                                Hero.effects["stunned"]["is"] = True
                    else:
                        if Enemy.elixiers["stamina potion"]["own"] > 0:
                            Enemy.potion_effect("stamina potion")
                            print(f"{Enemy.name} získává {Enemy.elixiers['stamina potion']['amount']} staminy.")
                            print(f"{Enemy.name} má nyní {Enemy.stamina} staminy.\n")
                        else:
                            print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                            Enemy.stamina += 10
                            pass
                        

                elif Enemy.char_class == "Monster":
                    if Enemy.stamina > 20:
                        if random.randint(1, 2) == 1:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Venomous Slam'! (20 až 40 dmg a otrava)")
                            venomous_slam_attack = Attack(Enemy, "Venomous Slam", base_dmg=random.randint(25, 40), dmg_type="blunt", effects=["poisoned"])
                            Hero.take_damage(venomous_slam_attack)
                            Hero.effects["poisoned"]["duration"] += 2
                            Hero.effects["poisoned"]["is"] = True
                        else:
                            Enemy.stamina_check()
                            print(f"{Enemy.name} použil útok 'Terrifying Roar'! (10 až 20 dmg, sníží obranu a má šanci na omráčení)")
                            terrifying_roar_attack = Attack(Enemy, "Terrifying Roar", base_dmg=random.randint(10, 20), dmg_type="psychic", effects=None)
                            Hero.take_damage(terrifying_roar_attack)
                            Hero.defense = max(Hero.defense - 10, 0)
                            if random.randint(1, 3) == 1:
                                Hero.effects["stunned"]["duration"] += 2
                                Hero.effects["stunned"]["is"] = True
                    else:
                        if Enemy.elixiers["stamina potion"]["own"] > 0:
                            Enemy.potion_effect("stamina potion")
                            print(f"{Enemy.name} získává {Enemy.elixiers['stamina potion']['amount']} staminy.")
                            print(f"{Enemy.name} má nyní {Enemy.stamina} staminy.\n")
                        else:
                            print(f"{Enemy.name} nemá žádné lektvary k použití.\n")
                            Enemy.stamina += 10
                            pass
                print(f"{Hero.name} má nyní {Hero.hp} HP.\n")
            
            
        Hero.is_alive_check()
        Enemy.is_alive_check() 
        time.sleep(2)   
        round_counter += 1
        break
