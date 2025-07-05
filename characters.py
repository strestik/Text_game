import time, random, sys
from contants import *
# from attack import *
from base_character import *


class Witcher(Character):
    def __init__(self, name):
        super().__init__(name, "Witcher")
        self.hp = 150
        self.mana = 35
        self.defense = 25
        self.skill = 1.2
        self.equip["siderite sword"] = {"own":True,"dmg_mutipl": 0.25}
        self.abilities = {"Steel Sword" : "30 až 40 dmg" ,
                            "Silver Sword" : "25 až 35 nebo 40 až 50 dmg pro monstra",}
        self.signs = {
            "Igni": "Ohnivý útok; 30 dmg a hoření za 15",               # burning 3 rounds
            "Aard": "Magické odhození; 20 dmg a stun na 1 kolo",        # stunned 1 round
            "Quen": "Kouzelná zeď; zvýší def o 30 za cenu 20 hp",       # giant def 1 round 
            "Axii": "Proud síly; doplní 20 many",                       # mana + 20 
            "Yrden": "Magické posílení; zlepší útoky o 10%",            # skill +
            "Heliotrop": "Kouzelný štít; zlepší def o 10"}              # def +

    def witcher_attacking(self):
        while True:
            time.sleep(1)
            choice = input("Vyber si útok nebo znamení (|x| - napiš x): ").strip()
            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 2 :
                    if choice == 2:
                        print(f"\n{Hero.name} použil útok Silver Sword.")
                        Hero.silver_sword(Enemy)

                    elif choice == 1:
                        print(f"\n{Hero.name} použil útok Steel Sword.")
                        Hero.steel_sword(Enemy)

                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    break

                elif 11 <= choice <= len(Hero.signs) + 10:
                    print(f"Mana: {Hero.mana}/100")
                    Hero.use_sign(Enemy, choice)
                    time.sleep(2)
                    print(f"\n{Hero.name} má nyní {Hero.mana}/100 many.")
                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    break

                else:
                    print("\nNeplatná volba. Zkus to znovu.\n")
                    continue
            else:
                print("\nNeplatná volba. Zkus to znovu.\n")
                continue





class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, "Sorcerer")
        self.hp = 120
        self.stamina = 0
        self.mana = 100
        self.defense = 15
        self.t_cooldown = 3
        self.equip["dimeritium staff"] = {"own":True,"dmg_mutipl": 0.25}
        self.abilities = {"Fireball" : "30 až 45 dmg a hoření",
                            "Thunder" : "60 az 70 dmg ale jen 1 použití za 3 kola",
                            "Ice Spike" : "20 až 35 dmg a zmrazení",
                            "Smite" : "50 až 60 dmg ignorujících def"}  # fireball is more effective against humans 30 if enemy.char_class != "Monster" else 20

    def sorcerer_attacking(self):
        while True:
            time.sleep(1)
            choice = input("\nVyber si magický útok (|x| - napiš x): ").strip()
            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 4 :
                    if choice == 1:
                        print(f"\n{Hero.name} použil útok Fire ball!!.")
                        Hero.fireball(Enemy)

                    elif choice == 2:
                        if round_counter  < 4:
                            print("\nBlesk můžeš použít až na 4. kole.")
                            continue
                        else:
                            print(f"\n{Hero.name} použil útok Thunder!!.")
                            Hero.thunder(Enemy)

                    elif choice == 3:
                        print(f"\n{Hero.name} použil útok Ice Spike!!.")
                        Hero.icespike(Enemy)
                        print(f"\n{Enemy.name} je zmrzlý, další dvě kola má sílu nižší o 50%.\n")

                    elif choice == 4:
                        print(f"\n{Hero.name} použil útok Smite!!.")
                        Hero.smite(Enemy)

                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    break
                else:
                    print("Neplatná volba. Zkus to znovu.")
                    continue
            else:
                print("Neplatná volba. Zkus to znovu.")
                continue


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, "Archer")
        self.hp = 130
        self.defense = 20
        self.equip["brokilon bow"] = {"own":True,"dmg_mutipl": 0.25}
        self.abilities = {"Arrow Rain" : "4 až 8 krát poškodí za 10 dmg", 
                          "Poison Arrow" : "20 až 25 dmg a otrávení", 
                          "Explosive Arrow" : "60 až 80 dmg, objetování 20 až 30 hp a šance na zapálení nepřítele"}

    def archer_attacking(self):
        while True:
            time.sleep(1)
            choice = input("\nVyber si útok (|x| - napiš x): ").strip()
            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 3 :
                    if choice == 1:
                        print(f"\n{Hero.name} použil útok Arrow Rain!!.")
                        Hero.arrow_rain(Enemy)

                    elif choice == 2:
                        print(f"\n{Hero.name} použil útok Poison Arrow!!.")
                        Hero.poison_arrow(Enemy)

                    elif choice == 3:
                        print(f"\n{Hero.name} použil útok Explosive Arrow!!.")
                        Hero.explosive_arrow(Enemy)
                        print(f"{Hero.name} má nyní {Hero.hp} HP")

                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    break
                else:
                    print("Neplatná volba. Zkus to znovu.")
                    continue
            else:
                print("Neplatná volba. Zkus to znovu.")
                continue

class Jarl(Character):
    def __init__(self, name):
        super().__init__(name, "Jarl")
        self.hp = 140
        self.defense = 30
        self.equip["skellige axe"] = {"own":True,"dmg_mutipl": 0.25}
        self.abilities = {"War cry" : "20 až 30 HP a 5 až 10 def",
                        "Bloody slash" : "30 až 40 dmg a silné krvácení",
                        "Battle Roar" : "- 5 až 15 nepřátelské def a šance na omráčení nepřítele pro toto a další kolo"}

    def jarl_attacking(self):
        while True:
            time.sleep(1)
            choice = input("\nVyber si útok (|x| - napiš x): ").strip()
            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 3 :
                    if choice == 1:
                        print(f"\n{Hero.name} použil útok War Cry!!.")
                        Hero.war_cry(Enemy)

                    elif choice == 2:
                        print(f"\n{Hero.name} použil útok Bloody slash!!.")
                        Hero.bloody_slash(Enemy)

                    elif choice == 3:
                        print(f"\n{Hero.name} použil útok Battle Roar!!.")
                        Hero.battle_roar(Enemy)

                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    break
                else:
                    print("Neplatná volba. Zkus to znovu.")
                    continue
            else:
                print("Neplatná volba. Zkus to znovu.")
                continue

class Bard(Character):
    def __init__(self, name):
        super().__init__(name, "Bard")
        self.hp = 170
        self.stamina = 80
        self.defense = 10
        self.respect = 100
        self.equip["elven lute"] = {"own":True,"dmg_mutipl": 0.25}
        self.abilities = {"Taunt" : "5 až 10 dmg, - 5 až 10 staminy a def nepříteli a 20 respektu. pokud máš více než 150 respektu máš i šanci na instakill",
                          "Power song" : "15 až 25 def a 20 až 30 staminy ",
                          "Melody of Browl" : "25 až 35 dmg a otrávení"}

    def bard_attacking(self):
        while True:
            time.sleep(1)
            choice = input("\nVyber si útok (|x| - napiš x): ").strip()
            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 3 :
                    if choice == 1:
                        print(f"\n{Hero.name} použil útok Taunt!!.")
                        Hero.taunt(Enemy)
                        print(f"{Enemy.name} má nyní {Enemy.stamina} staminy a {Enemy.defense} obrany.")

                    elif choice == 2:
                        print(f"\n{Hero.name} použil útok Power song!!.")
                        Hero.power_song(Enemy)
                        print(f"{Hero.name} zpívá mocnou píseň a získává {Hero.defense} obrany a {Hero.stamina} staminy.")

                    elif choice == 3:
                        print(f"\n{Hero.name} použil útok Melody of brawl!!.")
                        Hero.melody_of_browl(Enemy)

                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    break
                else:
                    print("Neplatná volba. Zkus to znovu.")
                    continue
            else:
                print("Neplatná volba. Zkus to znovu.")
                continue


class Monster(Character):
    def __init__(self, name):
        super().__init__(name, "Monster")
        self.hp = 160
        self.defense = 20
        self.equip["iron claws"] = {"own":True,"dmg_mutipl": 0.25}
        self.abilities = {"Claw Swipe" : "2 krát 15 až 25 dmg a krvácení",
                           "Bite" : "20až 30 dmg, krvácení a otrávení",
                            "Ripping clutches" : "25 až 35 dmg a silné krvácení"}  # smash attack

    def monster_attacking(self):
        while True:
            time.sleep(1)
            choice = input("\nVyber si útok (|x| - napiš x): ").strip()
            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 3 :
                    if choice == 1:
                        print(f"\n{Hero.name} použil útok Claw Swipe!!.")
                        Hero.claw_swipe(Enemy)

                    elif choice == 2:
                        print(f"\n{Hero.name} použil útok Bite!!.")
                        Hero.bite(Enemy)

                    elif choice == 3:
                        print(f"\n{Hero.name} použil útok Ripping clutches!!.")
                        Hero.ripping_clutches(Enemy)

                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")
                    break
                else:
                    print("Neplatná volba. Zkus to znovu.")
                    continue
            else:
                print("Neplatná volba. Zkus to znovu.")
                continue



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
        return Witcher(Enemy.name)
    elif char_class == "Sorcerer":
        return Sorcerer(Enemy.name)
    elif char_class == "Archer":
        return Archer(Enemy.name)
    elif char_class == "Jarl":
        return Jarl(Enemy.name)
    elif char_class == "Bard":
        return Bard(Enemy.name)
    elif char_class == "Monster":
        return Monster(Enemy.name)
    else:
        print("--> Neplatná třída, zkus to znovu.\n")