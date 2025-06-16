# jednotlivý characters z Hero
import random
import time
import sys
from text import *
from chractering import *
from potion import *
from items import *
from effect import *
from e_chracters import *
# from base_character import *
from attack import *

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
                    if choice == 1:
                        print(f"\n{Hero.name} použil útok Silver Sword.")
                        Hero.silver_sword(Enemy)
                        
                    elif choice == 2:
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
                
        
    def steel_sword(self, target):
        steel_sword_attack = Attack(self, "Steel Sword", base_dmg=random.randint(30, 40), dmg_type="slash", effects=["bleeding"])  # steel sword is more effective against humans 35 if enemy.char_class != "Monster" else 20
        target.take_damage(steel_sword_attack)
        target.effects["bleeding"]["duration"] += 3 
        target.effects["bleeding"]["is"] = True

        
    def silver_sword(self, target):
        base = random.randint(40, 50) if Enemy.char_class == "Monster" else random.randint(25, 35)
        silver_sword_attack = Attack(self, "Silver Sword", base_dmg= base, dmg_type="slash", effects = ["bleeding"],)  # silver sword is more effective against monsters 45 if enemy.char_class == "Monster" else 30
        target.take_damage(silver_sword_attack)
        target.effects["bleeding"]["duration"] += 3 
        target.effects["bleeding"]["is"] = True   # Set bleeding duration to 3 rounds 
        
        

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
                target.take_damage(igni_attack)
                target.effects["burning"]["duration"] += 3
                target.effects["burning"]["is"] = True
                break
            
            elif sign_choice == 12:
                print(f"\n{self.name} použil znamení Aard a omráčil nepřítele.")
                time.sleep(1)
                aard_attack = Attack(Hero, "Aard", base_dmg=20, dmg_type="stun", effects=["stunned"])
                self.mana -= 10  
                time.sleep(1)
                target.take_damage(aard_attack)
                global delay
                delay += 1
                break
            
            elif sign_choice == 13:
                time.sleep(1)
                self.defense += 30
                self.hp -= 20
                self.mana -= 10
                print(f"\n{self.name} použil znamení Quen a zvýšil svou obranu na {self.defense}. A nyní má {self.hp} HP.")
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

    def thunder(self, target):
        if (round_counter + 3) - self.t_cooldown > 3:
            self.mana_check()
            thunder_attack = Attack(self, "Thunder", base_dmg=random.randint(60, 70), dmg_type="magick", effects=None)  # steel sword is more effective against humans 35 if enemy.char_class != "Monster" else 20
            target.take_damage(thunder_attack)
            self.t_cooldown = round_counter + 3
        else: 
            print(f"Blesk můžeš použít až za {self.t_cooldown - round_counter}")
            return 

    def fireball(self, target):
        self.mana_check()
        fireball_attack = Attack(self, "Fireball", base_dmg=random.randint(30, 45), dmg_type="fire", effects=["burning"])
        target.take_damage(fireball_attack)
        target.effects["burning"]["duration"] += 3  # Set burning duration to 3 rounds
        target.effects["burning"]["is"] = True  # Apply burning effect
    
    def icespike(self, target):
        self.mana_check()
        icespike_attack = Attack(self, "Ice Spike", base_dmg=random.randint(20, 35), dmg_type="ice", effects=["frozen"])
        target.take_damage(icespike_attack)
        target.effects["frozen"]["duration"] += 2  # Set frozen duration to 2 rounds
        target.effects["frozen"]["is"] = True  # Apply frozen effect
        if target.skill > 0.5:
            target.skill -= 0.5  # Reduce target's skill by 50%
        else:
            target.skill = 0
            print(f"{target.name} je zcela zmražen a jeho síla je snížena na 0%.")

    def smite(self, target):
        self.mana_check()
        d = target.defense
        target.defense = 0
        smite_attack = Attack(self, "Smite", base_dmg=random.randint(50, 60), dmg_type="fire", effects=None)
        target.take_damage(smite_attack)
        target.defense = d


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
        
    def arrow_rain(self, target):
        self.stamina_check()
        arrow_rain_attack = Attack(self, "Arrow Rain", base_dmg=random.randint(4, 8) * 10, dmg_type="piercing", effects=None)
        target.take_damage(arrow_rain_attack)
    
    def poison_arrow(self, target):
        self.stamina_check()
        poison_arrow_attack = Attack(self, "Poison Arrow", base_dmg=random.randint(20, 25), dmg_type="piercing", effects=["poisoned"])
        target.take_damage(poison_arrow_attack)
        target.effects["poisoned"]["duration"] += 3
        target.effects["poisoned"]["is"] = True  # Apply poisoned effect

    def explosive_arrow(self, target):
        self.stamina_check()
        explosive_arrow_attack = Attack(self, "Explosive Arrow", base_dmg=random.randint(60, 80), dmg_type="explosive", effects=None)
        target.take_damage(explosive_arrow_attack)
        self.hp -= random.randint(20, 30)  # Self-damage from explosion
        if random.randint(1, 3) == 2:  # 50% chance to ignite the target
            target.effects["burning"]["duration"] += 3  # Set burning duration to 3 rounds
            target.effects["burning"]["is"] = True  # Apply burning effect
        else:
            pass


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

        
    def war_cry(self, target):
        self.stamina_check()
        self.hp += random.randint(20, 30)
        self.defense += random.randint(5, 10)
        print(f"{self.name} použil bojový pokřik a získal {self.hp} HP a {self.defense} obrany.")

    def bloody_slash(self, target):
        self.stamina_check()
        bloody_slash_attack = Attack(self, "Bloody Slash", base_dmg=random.randint(30, 40), dmg_type="slash", effects=["bleeding"])
        target.take_damage(bloody_slash_attack)
        target.effects["bleeding"]["duration"] += 5
        target.effects["bleeding"]["is"] = True

    def battle_roar(self, target):
        self.stamina_check()
        if target.defense - random.randint(5, 15) > 0 :
            target.defense -= random.randint(5, 15)
        else:
            pass
         
        print(f"{target.name} má nyní {target.defense} obrany.")
        if random.randint(1, 5) == 3:
            print(f"{target.name} je omráčen.")
            target.effects["stunned"]["duration"] += 1  # Set burning duration to 3 rounds
            target.effects["stunned"]["is"] = True  # Apply burning effect
        else:
            pass



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

    def taunt(self, target):
        self.stamina_check()
        if self.respect > 150 and random.randint(1, 20) == 17:
            target.hp -= target.hp + 1
            print("Nepřítel nesnesl tvoji urážku a spadl na zem mrtví. Gratuluji urazil jsi nepřítele tak moc že to nepřežil.")
            
        taunt_attack = Attack(self, "Taunt", base_dmg=random.randint(5, 10), dmg_type="slash", effects=None)
        target.take_damage(taunt_attack)
        target.stamina -= random.randint(5, 10)
        target.defense -= random.randint(5, 10)
        self.respect += 20

    def power_song(self, target):
        self.stamina_check()
        self.defense += random.randint(15, 25)
        self.stamina += random.randint(20, 30)

    def melody_of_browl(self, target):
        self.stamina_check()
        melody_attack = Attack(self, "Melody of Brawl", base_dmg=random.randint(25, 35), dmg_type="slash", effects=["poisoned"])
        target.take_damage(melody_attack)
        target.effects["poisoned"]["duration"] += 2
        target.effects["poisoned"]["is"] = True

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

    def claw_swipe(self, target):
        self.stamina_check()
        claw_swipe_attack = Attack(self, "Claw Swipe", base_dmg=random.randint(15, 25) * 2, dmg_type="slash", effects=["bleeding"])
        target.take_damage(claw_swipe_attack)
        target.effects["bleeding"]["duration"] += 3
        target.effects["bleeding"]["is"] = True

    def bite(self, target):
        self.stamina_check()
        bite_attack = Attack(self, "Bite", base_dmg=random.randint(15, 25) * 2, dmg_type="pierce", effects=["bleeding"])
        target.take_damage(bite_attack)
        target.effects["bleeding"]["duration"] += 3
        target.effects["bleeding"]["is"] = True
        target.effects["poisoned"]["duration"] += 3  # vyměnít za venom
        target.effects["poisoned"]["is"] = True

    def ripping_clutches(self, target):
        self.stamina_check()
        ripping_clutches_attack = Attack(self, "Ripping clutches", base_dmg=random.randint(25, 35), dmg_type="slash", effects=["bleeding"])
        target.take_damage(ripping_clutches_attack)
        target.effects["bleeding"]["duration"] += 5
        target.effects["bleeding"]["is"] = True

# class Dwarf