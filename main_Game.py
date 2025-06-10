import random
import time
import sys
alive = True
delay = 3
round_counter = 1
Hero = None  # Initialize Hero variable
Enemy = None  # Initialize Enemy variable
# Global variable to track if the game is alive
titles = [
    "Neporazitelný",
    "Khemrikara",
    "Velký král Nehekhary",
    "Král králů",
    "Velekrál Khemri",
    "Potomek bohů",
    "Velký jestřáb nebes",
    "Vyvolený Ptry",
    "Posvátný potomek Usiriana",
    "Šampion Velké pouště",
    "Pán Země",
    "Vládce oblohy",
    "Přinášející světlo",
    "Vyvolený bohů",
    "Překonavší kodex mrtvých",
    "Věčný vládce dvou zemí",
    "První kněžský král",
    "Světlo Nehekhary",
    "Nepokojný",
    "Zlatý faraon",
    "Metla bezvěrců",
    "Věčný král",
    "Nesporný vládce Khemri a celé Nehekhary",
    "Jediný pravý král",
    "Král Divokého honu",
    "Řezník světů",
    "Chladný plamen prázdnoty",
    "Elfská záhada",
    "Bílý plamen tančící na mohylách svých nepřátel",
    "Zrádce z Thaneddu",
    "Bestie v lidské kůži",
    "Ohař Vilgefortze",
    "Bestie z Beauclairu",
    "Pán zrcadel",
    "Oheň Salamandry",
    "Vrah králů",
    "Falešný prorok",
    "Šílený král",
    "Černý jezdec",
    "Šeptač ze stínů",
    "Čarodějka stínů",
    "Pavoučí tkadlec války",
    "Čepel v zahradě",
    "Paní kontroly"
]


enemy_names = [
    "Eredin",
    "Imlerith",
    "Caranthir",
    "Avallac'h",
    "Emhyr",
    "Vilgefortz",
    "Bonhart",
    "Rience",
    "Dettlaff",
    "Gaunter",
    "Azar",
    "Letho",
    "Jacques",
    "Radovid",
    "Cahir",
    "Stefan",
    "Fringilla",
    "Sigismund",
    "Reynard",
    "Tissaia",
    "Settra"
]

characters = [
    "Witcher",
    "Sorcerer",
    "Archer",
    "Jarl",
    "Bard",
    "Monster"
]

class Attack:
    def __init__(self, attacker, name, base_dmg, dmg_type, effects=None):
        self.attacker = attacker  # instance postavy, která útočí
        self.name = name
        self.base_dmg = base_dmg
        self.dmg_type = dmg_type
        self.effects = effects or None
        self.multiplier = Hero.skill  # vynásobíme dovedností, možnist přidání multiplieru z vybavení

    def calculate_damage(self):
        return int(self.base_dmg * self.multiplier)
    
class Character:
    def __init__(self, name, char_class,):
        self.is_alive = True
        self.name = name
        self.char_class = char_class 
        self.hp = 100
        self.stamina = 100
        self.mana = 0
        self.defense = 70
        self.skill = 1.2  # dmg multiplier
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
                        "stamina regen": {"is" : False, "duration": 0}}
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
            "crossbow": {"own":True,"dmg_mutipl": 0.3},  # [owned, dmg multiplier]
            "dagger": {"own":True,"dmg_mutipl": 0.2},  # [owned, dmg multiplier]
            "sword": {"own":True,"dmg_mutipl": 0.15},
            "axe": {"own":False,"dmg_mutipl": 0.25},
            "bow": {"own":True,"dmg_mutipl": 0.2},
            "bomb": {"own":True,"dmg": 60, "effect": None},  # [owned, base dmg]
            "poison bomb": {"own":True,"dmg": 50, "effect": "poisoned"},  # [owned, base dmg, effect]
            "fire bomb": {"own":True,"dmg": 50, "effect": "burning"},  # [owned, base dmg, effect]
            "frost bomb": {"own":True,"dmg": 50, "effect": "frozen"},  # [owned, base dmg, effect]
            }

    def is_alive_check(self):
        self.is_alive = False if self.hp <= 0 else True
        if not self.is_alive:
            time.sleep(1)
            print(f"{self.name} byl poražen.")
            global alive
            alive = False
            if not Hero.is_alive:
                print(f"{Hero.name} byl poražen. Konec hry.\n")
                sys.exit(0)
            if not Enemy.is_alive:
                print(f"{Enemy.name} byl poražen. Gratuluji!\n")
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
            self.effects[effect] = True
            print(f"{self.name} je nyní ovlivněn efektem: {effect}.")
        
        self.is_alive_check()


    def apply_effects(self, h_amount, s_amount):    # možnost přidání časiového omezení efektů
        if self.effects["bleeding"]["is"] == True:
            if self.effects["bleeding"]["duration"] == 0:
                pass
            else:
                print(f"\n{self.name} krvácí a ztrácí 10 HP.\n")
                self.hp -= 10
                self.effects["bleeding"]["duration"] -= 1
                if self.effects["bleeding"]["duration"] <= 0:
                    self.effects["bleeding"]["is"] = False
                    print(f"{self.name} přestal krvácet.\n")

        if self.effects["burning"]["is"] == True:
            if self.effects["burning"]["duration"] == 0:
                pass
            else:
                print(f"\n{self.name} hoří a ztrácí 15 HP.\n")
                self.hp -= 15
                self.effects["burning"]["duration"] -= 1
                if self.effects["burning"]["duration"] <= 0:
                    self.effects["burning"]["is"] = False
                    print(f"{self.name} přestal hořet.\n")

        if self.effects["poisoned"]["is"] == True:
            if self.effects["poisoned"]["duration"] == 0:
                pass
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
                print(f"\n{self.name} je omráčen a nemůže se hýbat tento kolo.\n")
                # časový limit pro omráčení, např. 1

        if self.effects["frozen"]["is"] == True:
            if self.effects["frozen"]["duration"] == 0:
                self.effects["frozen"]["is"] = False
                print(f"{self.name} se zotavil z omrznutí.\n")
            else:
                self.effects["frozen"]["duration"] -= 1
                print(f"\n{self.name} je zmrzlý, tento kolo se může hýbat jen omezeně.\n")
                #časový limit pro zmrazení, např. 1 partly stunned

        if self.effects["healing"]["is"] == True:
            if self.effects["healing"]["duration"] == 0:
                self.h_amount = 0
            else:
                print(f"\n{self.name} se léčí a získává {h_amount}.\n")
                self.hp += h_amount
                self.effects["healing"]["duration"] -= 1
                if self.effects["healing"]["duration"] <= 0:
                    self.effects["healing"]["is"] = False
                    print(f"{self.name} přestal regenerovat HP.\n")
                    
        if self.effects["stamina regen"]["is"] == True:
            if self.effects["stamina regen"]["duration"] == 0:
                self.s_amount = 0
            else:
                print(f"\n{self.name} regeneruje {s_amount} Stamina.\n")
                self.stamina += s_amount
                self.effects["stamina regen"]["duration"] -= 1
                if self.effects["stamina regen"]["duration"] <= 0:
                    self.effects["stamina regen"]["is"] = False
                    print(f"{self.name} přestal regenerovat staminu.\n")
        else:
            pass
        # self.is_alive_check()

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
                print(f"{self.name} má nyní sílu {self.skill}%.")
                time.sleep(1)

            elif potion_type == "vlk":
                self.potion_usage("vlk")
                time.sleep(0.7)
                self.skill += self.elixiers[potion_type]["amount"]
                print(f"{self.name} vypil lektvar a získal {self.elixiers[potion_type]['amount'] * 100}% síly.")
                print(f"{self.name} má nyní sílu {self.skill}%.")
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
                f"8. Blizzard        (regeneruje 20 Stamina po dobu 3 kol)  [kusů : {self.elixiers['blizzard']['own']}]\n")
        
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


    def attcking(self, target):

        if self.char_class == "Witcher":
            print(f"{self.name} útočí stříbrným mečem.")
            self.silver_sword(target)

        elif self.char_class == "Sorcerer":
            print(f"{self.name} používá Fireball.")
            self.fireball(target)
        elif self.char_class == "Archer":
            print(f"{self.name} střílí z luku.")
            # Implement Archer's attack
        elif self.char_class == "Jarl":
            print(f"{self.name} zařve bojový pokřik.")
            # Implement Jarl's attack
        elif self.char_class == "Bard":
            print(f"{self.name} zpívá povzbuzující píseň.")
            # Implement Bard's attack
        elif self.char_class == "Monster":
            print(f"{self.name} zaútočí drápem.")
            # Implement Monster's attack



    def use_item(self):
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
                        else:
                            print(f"\nNemáš {item_name}. Zkus to znovu.\n")
                            Hero.use_item()
                        time.sleep(2)
                    
                    else :
                        if Hero.equip[item_name]['own'] == True:
                            Hero.skill += Hero.equip[item_name]["dmg_mutipl"]  # Apply the multiplier if the item is owned
                            print(f"""Máš {item_name} a ten ti zlepšuje sílu o {Hero.equip[item_name]["dmg_mutipl"] * 100:.0f}%.""")
                            print(f"{Hero.name} má nyní sílu {Hero.skill * 100:.0f}%.")
                        else:
                            print(f"\nNemáš {item_name}. Zkus to znovu.\n")
                            Hero.use_item()
                        time.sleep(2)

                else:
                    print(f"\nNemáš {item_name}.Zkus to znovu.\n")
            else:
                print("\nNeplatná volba.\n")
     
        else:
            print("Zadej číslo nástroje.\n")




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





class Witcher(Character):
    def __init__(self, name):
        super().__init__(name, "Witcher")
        self.hp = 150
        self.stamina = 100
        self.mana = 35
        self.defense = 30
        self.skill = 1.5
        self.abilities = ["Silver Sword", "Steel Sword"]
        self.signs = {
            "Igni": "Ohnivý útok; 30 dmg a hoření za 15",               # burning 3 rounds
            "Aard": "Magické odhození; 20 dmg a stun na 1 kolo",        # stunned 1 round
            "Quen": "Kouzelná zeď; zvýší def o 30 na 1 kolo",           # giant def 1 round 
            "Axii": "Proud síly; doplní 20 many",                       # mana + 20 
            "Yrden": "Magické posílení; zlepší útoky o 10%",            # skill +
            "Heliotrop": "Kouzelný štít; zlepší pernamentně def o 10"}  # def +
        
    def steel_sword(self, target):
        steel_sword_attack = Attack(self, "Steel Sword", base_dmg=random.randint(30, 40), dmg_type="slash", effects=["bleeding"])  # steel sword is more effective against humans 35 if enemy.char_class != "Monster" else 20
        Enemy.take_damage(steel_sword_attack)
        Enemy.effects["bleeding"]["duration"] += 3 
        self.apply_effects()

        
    def silver_sword(self, target):
        base = random.randint(40, 50) if Enemy.char_class == "Monster" else random.randint(25, 35)
        silver_sword_attack = Attack(self, "Silver Sword", base_dmg= base, dmg_type="slash", effects = ["bleeding"],)  # silver sword is more effective against monsters 45 if enemy.char_class == "Monster" else 30
        Enemy.take_damage(silver_sword_attack)
        Enemy.effects["bleeding"]["duration"] += 3 
        Enemy.effects["bleeding"]["is"] = True   # Set bleeding duration to 3 rounds 
        
        

    def use_sign(self, target, choice):
        while True:
            sign_choice = choice

            if sign_choice < 11 or sign_choice > len(self.signs) + 10:
                print("\nNeplatné číslo znamení. Zkus to znovu.\n")
                continue

            if not sign_choice == 14 and self.mana < 10:
                print("\nNemáš dost many na použití znamení.\n")
                break

            if sign_choice == 11:
                print(f"\n{self.name} použil znamení Igni a zapálil nepřítele.")
                time.sleep(1)
                igni_attack = Attack(Hero, "Igni", base_dmg=30, dmg_type="fire", effects=["burning"])
                self.mana -= 10  # Reduce mana for using the sign
                time.sleep(1)
                Enemy.take_damage(igni_attack)
                break
            
            elif sign_choice == 12:
                print(f"\n{self.name} použil znamení Aard a omráčil nepřítele.")
                aard_attack = Attack(Hero, "Aard", base_dmg=20, dmg_type="stun", effects=["stunned"])
                self.mana -= 10  
                Enemy.take_damage(aard_attack)
                break
            
            elif sign_choice == 13:
                self.defense += 30
                self.mana -= 10
                print(f"\n{self.name} použil znamení Quen a zvýšil svou obranu na {self.defense}.")  
                break
            
            elif sign_choice == 14:
                print(f"\n{self.name} použil znamení Axii a získal 20 many.")
                self.mana = min(self.mana + 20, 100)  # Ensure mana does not exceed max
                break
            
            elif sign_choice == 15:
                self.skill += 0.1
                self.mana -= 10  
                print(f"\n{self.name} použil znamení Yrden a zvýšil svou dovednost na {self.skill * 100:.0f}%.")
                break
                
            elif sign_choice == 16:
                self.defense += 10
                self.mana -= 10 
                print(f"\n{self.name} použil znamení Heliotrop a zvýšil svou obranu na {self.defense}.")
                break
                    
            else:
                print("Neplatné znamení. Dostupné možnosti:")
                for sign in self.signs:
                    print(f" - {sign.capitalize()}")
                continue
            # else:
            #     print("Neplatné znamení. Dostupné možnosti:")
            #     for sign in self.signs:
            #         print(f" - {sign.capitalize()}")
            #     continue


class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, "Sorcerer")
        self.hp = 110
        self.stamina = 40
        self.mana = 100
        self.defense = 20
        self.skill = 1.4
        self.abilities = ["Fireball", "Ice Spike", "Lightning Bolt"]

    def thunder(self, target):
        if round_counter - t_cooldown > 3:
            self.mana_check()
            thunder_attack = Attack(self, "Thunder", base_dmg=random.randint(60, 70), dmg_type="magick", effects=None)  # steel sword is more effective against humans 35 if enemy.char_class != "Monster" else 20
            Enemy.take_damage(thunder_attack)
            t_cooldown = round_counter
        else: 
            print(f"Blesk můžeš použít až za {round_counter - t_cooldown}")
            return

    def fireball(self, target):
        self.mana_check()
        attack = Attack(self, "Fireball", base_dmg=random.randint(30, 45), dmg_type="fire", effects=["burning"])
        target.take_damage(attack)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, "Archer")
        self.hp = 130
        self.stamina = 100
        self.mana = 0
        self.defense = 25
        self.skill = 1.3
        self.abilities = ["Arrow Rain", "Poison Arrow", "Explosive Arrow"]

class Jarl(Character):
    def __init__(self, name):
        super().__init__(name, "Jarl")
        self.hp = 170
        self.stamina = 100
        self.mana = 0
        self.defense = 35
        self.skill = 1.1
        self.abilities = ["War Cry", "Shield Bash", "Battle Roar"]

class Bard(Character):
    def __init__(self, name):
        super().__init__(name, "Bard")
        self.hp = 120
        self.stamina = 80
        self.mana = 0
        self.defense = 10
        self.skill = 1.2
        self.respect = 100
        self.abilities = ["Song of Healing", "Inspiring Melody", "Lullaby"]

class Monster(Character):
    def __init__(self, name):
        super().__init__(name, "Monster")
        self.hp = 160
        self.stamina = 100
        self.mana = 0
        self.defense = 30
        self.skill = 1.3
        self.abilities = ["Claw Swipe", "Bite", "Roar"]
 





# Hero.witcher()  # Initialize as Witcher

# enemy = Character()  # Example enemy character


Enemy = Character(f"{random.choice(enemy_names)}", f"{random.choice(characters)}")  # Initialize Enemy character
Enemy = Enemy.en_classing(f"{random.choice(characters)}")  # Convert to Monster class

print(f"\nTvůj nepřítel je {Enemy.name} {random.choice(titles)}, třída: {Enemy.char_class}, HP: {Enemy.hp}, Stamina: {Enemy.stamina}, Mana: {Enemy.mana}, Defense: {Enemy.defense}\n")
time.sleep(2)

# Nameing
print(f"\nVýtej hráč, vyber si svou postavu:")
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
print(f"\n---> Tvoje postava je {Hero.name}, třída: {Hero.char_class}, HP: {Hero.hp}, Stamina: {Hero.stamina}, Mana: {Hero.mana}, Defense: {Hero.defense}\n")
time.sleep(2)
print(f"\nNyní můžeš začít hrát. Tvým úkolem je přežít a porazit nepřítele.") 
time.sleep(3)
print("Boj začínáš bez vybavení a vylepšení, jestli chceš použít meč nebo vypít lektvar, musíš na to využít kolo.")
time.sleep(3)
print("Ale neměj strách, protivník se připravuje, takže první tři kola na tebe nezaútočí.")



# Game loop

    
while alive:
    time.sleep(2)
    print("\n")
    print(f"\nKolo : {round_counter}\n")
    time.sleep(1)
    Hero.apply_effects(Hero.h_amount, Hero.s_amount)  # Apply effects at the start of each round
    time.sleep(1)
    print("Zde jsou dostupné akce: \n"
        "1. Ůtočení\n"
        "2. Elixíry\n"
        "3. Nástroje a výstroj\n"
        "4. Zkontroluj svůj stav a stav nepřítele\n"
        "5. Exit Game\n"
        "6. a\n")
    
    action = input("Vyber si: ").strip().lower()
    if action.isdigit():
        action = int(action)
        if action == 1 :
            print(f"\nVyber si svůj útok--> \n")
            if Hero.char_class == "Sorcerer" :
                print(f"Jako mág můžeš používat jen magii.")
                print(f"Tvé schopnosti jsou: ")
                for x, (ability) in enumerate(Hero.abilities):
                    print(f"|{x +1}|{ability}")

                choice = input("Vyber si magický útok (|x| - napiš x): ").strip()
                if choice.isdigit():
                    choice = int(choice)
                    
                    if 1 <= choice <= 2 :
                        if choice == 1:
                            print(f"\n{Hero.name} použil útok Fire ball!!.")
                            Hero.fireball(Enemy)
                            
                        elif choice == 2:
                            print(f"\n{Hero.name} použil útok Thunder!!.")
                            Hero.thunder(Enemy)

                        print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    
                    else:
                        print("Neplatná volba. Zkus to znovu.")
                        continue

                else:
                    print("Neplatná volba. Zkus to znovu.")
                    continue
                

            elif Hero.char_class == "Witcher" :
                print(f"Tvé schopnosti jsou: ")
                for x, (ability) in enumerate(Hero.abilities):
                    print(f"|{x +1}|{ability}")
                
                print(f"\nJako zklínač můžeš používat i znamení (cena --> 10 many) :\n")
                time.sleep(1)

                for x, (key, value) in enumerate(Hero.signs.items()):
                    print(f"|1{x + 1}|{key} - {value}")
                print("")
                time.sleep(1)

                choice = input("Vyber si útok nebo znamení (|x| - napiš x): ").strip()
                if choice.isdigit():
                    choice = int(choice)
                    
                    if 1 <= choice <= 2 :
                        if choice == 1:
                            print(f"\n{Hero.name} použil útok Silver Sword.")
                            Hero.silver_sword(Enemy)
                            
                        elif choice == 2:
                            print(f"\n{Hero.name} použil útok Steel Sword.")
                            Hero.steel_sword(Enemy)

                        print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    
                    elif 11 <= choice <= len(Hero.signs) + 10:
                        print(f"Mana: {Hero.mana}/100")
                        Hero.use_sign(Enemy, choice)
                        time.sleep(2)
                        print(f"\n{Hero.name} má nyní {Hero.mana}/100 many.")
                        print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    else:
                        print("Neplatná volba. Zkus to znovu.")
                        continue

                else:
                    print("Neplatná volba. Zkus to znovu.")
                    continue

                # # attaking
                # ability_choice = input("Vyber si schopnost (číslo): ").strip()
                # if ability_choice.isdigit():
                #     ability_choice = int(ability_choice)

                #     if 1 <= ability_choice <= len(Hero.abilities):
                #         if Hero.abilities[ability_choice - 1] == "Silver Sword":
                #             Hero.silver_sword(Enemy)
                #         elif Hero.abilities[ability_choice - 1] == "Steel Sword":
                #             Hero.steel_sword(Enemy)
                #         else:
                #             print("Neplatná schopnost.")
                #     else:
                #         print("Neplatná volba.")


                        

        elif action == 2:
            print("Pozor lektvarů máš jen omezený počet. Využíj je moudře.")
            time.sleep(0.5)
            Hero.potion()
            time.sleep(1)


        elif action == 3:
            for index, item in enumerate(Hero.equip, start=1):                                                 # len(list(Hero.equip.items())):
                print(f"|{index}| {item} - {'Máš' if Hero.equip[item]['own'] == True else 'Nemáš' }")          # Hero.equip[item]
            print("\nPozor!!!, od každé bomy máš jen jeden kus, takže je používej opatrně.\n")
            Hero.use_item()  # Použití nástroje
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
            print(f"Efficiency: {Hero.skill * 100:.0f}%")
            time.sleep(3)
            round_counter -= 1
            continue

        elif action == 5:
            print("Díky za hraní! Nashledanou.\n")
            break

        else:
            print("Něco jsi zadal špatně. Opakuj.")
            continue
    else:
        print("\nNapiš číslo úkonu.")
        continue

    # Simulace útoku nepřítele
    Enemy.apply_effects(Enemy.h_amount, Enemy.s_amount)  # Apply effects at the start of each round
    time.sleep(1)
    if delay > 0:
        print(f"\n{Enemy.name} se připravuje na útok...")
        if round_counter == 3:
            delay = 0
        time.sleep(delay)
    else:
        print(f"\n{Enemy.name} útočí.")
        time.sleep(0.5)
        if Enemy.hp < Enemy.hp / 2 and Hero.hp > Hero.hp / 2:
            Enemy.potion()
            enemy_attack = Attack(Enemy, "Monster Attack", base_dmg=20, dmg_type="physical", effects=["bleeding"])  
            Hero.take_damage(enemy_attack)
            print(f"{Enemy.name} útočí na {Hero.name} a způsobuje {enemy_attack.calculate_damage()} poškození.")
            print(f"{Hero.name} má nyní {Hero.hp} HP.\n")
        
        Hero.is_alive_check()
        time.sleep(2)
        
    round_counter += 1
