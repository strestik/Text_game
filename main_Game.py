import random
import time
import sys
alive = True

class Attack:
    def __init__(self, attacker, name, base_dmg, dmg_type, effects=None):
        self.attacker = attacker  # instance postavy, která útočí
        self.name = name
        self.base_dmg = base_dmg
        self.dmg_type = dmg_type
        self.effects = effects or []
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

        self.effects = {"burning": False, "poisoned": False, "stunned": False, "frozen": False, "bleeding": False}
        self.elixiers = {
            "healing potion": False,
            "stamina potion": False,
            "mana potion": False, 
            "vlaštovka": False, # duration healing
            "hrom": False, # dmg multiplier
            "vlk": False, # sklill multiplier
            "medvěd": False, # defense multiplier
            "blizzard": False, # stamina regen
            }
        self.equip = {
            "crossbow": [False, 0.3],  # [owned, dmg multiplier]
            "dagger": [False, 0.2],  # [owned, dmg multiplier]
            "sword": [False, 0.15],
            "axe": [False, 0.25],
            "bow": [False, 0.2],
            "bomb": [False, 60],  # [owned, base dmg]
            "poison bomb": [False, 50, "poisoned"],  # [owned, base dmg, effect]
            "fire bomb": [False, 50, "burning"],  # [owned, base dmg, effect]
            "frost bomb": [False, 50, "frozen"],  # [owned, base dmg, effect]
            }

    def is_alive_check(self):
        self.is_alive = False if self.hp <= 0 else True

    def take_damage(self, attack: Attack):
        raw_dmg = attack.calculate_damage()
        reduced_dmg = max(raw_dmg - self.defense, 0)
        self.hp -= reduced_dmg
        print(f"{self.name} dostal {reduced_dmg} poškození od útoku {attack.name}.")

        # Efekty
        for effect in attack.effects:
            self.effects[effect] = True
            print(f"{self.name} je nyní ovlivněn efektem: {effect}.")
        
        self.apply_effects()
        self.is_alive_check()


    def apply_effects(self):    # možnost přidání časiového omezení efektů
        if self.effects.get("bleeding"):
            print(f"{self.name} krvácí a ztrácí 10 HP.")
            self.hp -= 10
        if self.effects.get("burning"):
            print(f"{self.name} hoří a ztrácí 15 HP.")
            self.hp -= 15
        if self.effects.get("poisoned"):
            print(f"{self.name} je otráven a ztrácí 5 HP.")
            self.hp -= 5
        if self.effects.get("stunned"):
            print(f"{self.name} je omráčen a nemůže se hýbat tento kolo.")
            # časový limit pro zmrazení, např. 1
        if self.effects.get("frozen"):
            print(f"{self.name} je zmrzlý, tento kolo se může hýbat jen omezeně.")
            #časový limit pro zmrazení, např. 1 partly stunned
        else:
            pass
        # self.is_alive_check()

    # def potion(self, potion_type):
    #     pass

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
        steel_sword_attack = Attack(self, "Steel Sword", base_dmg=35, dmg_type="slash", effects=["bleeding"])
        Enemy.take_damage(steel_sword_attack)

        
    def silver_sword(self, target):
        base = 45 if Enemy.char_class == "Monster" else 30
        silver_sword_attack = Attack(self, "Silver Sword", base_dmg= base, dmg_type="slash", effects=["bleeding"])  # silver sword is more effective against monsters 45 if enemy.char_class == "Monster" else 30
        Enemy.take_damage(silver_sword_attack)

    

    def use_sign(self, target):
        while True:
            sign_choice = input("Vyber si znamení (|x| - napiš x): ").strip()
            
            if sign_choice.isdigit():
                sign_choice = int(sign_choice)

                if sign_choice < 11 or sign_choice > len(self.signs) + 10:
                    print("Neplatné číslo znamení. Zkus to znovu.")
                    continue

                if not sign_choice == 14 and self.mana < 10:
                    print("Nemáš dost many na použití znamení.")
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
            else:
                print("Neplatné znamení. Dostupné možnosti:")
                for sign in self.signs:
                    print(f" - {sign.capitalize()}")
                continue


class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, "Sorcerer")
        self.hp = 110
        self.stamina = 40
        self.mana = 100
        self.defense = 20
        self.skill = 1.4
        self.abilities = ["Fireball", "Ice Spike", "Lightning Bolt"]

    def fireball(self, target):
        if self.mana < 20:
            print("Nemáš dost many na Fireball!")
            return
        self.mana -= 20
        attack = Attack(self, "Fireball", base_dmg=45, dmg_type="fire", effects=["burning"])
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


Enemy = Character("Enemy", "Monster")  # Initialize Enemy character
Enemy = Monster(Enemy.name)  # Convert to Monster class

print(f"\nTvůj nepřítel je {Enemy.name}, třída: {Enemy.char_class}, HP: {Enemy.hp}, Stamina: {Enemy.stamina}, Mana: {Enemy.mana}, Defense: {Enemy.defense}\n")

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




    

while alive:
    time.sleep(3)
    print("\nZde jsou dostupné akce: \n"
          "1. Ůtočení\n"
          "2. Elixíry\n"
          "3. Nástroje\n"
          "4. Zkontroluj svůj stav\n"
          "5. Exit Game\n"
          "6. a\n")
    
    action = input("Vyber si: ").strip().lower()
    if action.isdigit():
        action = int(action)
        if action == 1 :
            print(f"Vyber si svůj útok: \n")
            if Hero.char_class == "Sorcerer" :
                print(f"Jako mág můžeš používat jen magii.")
                pass
            else:

                if Hero.char_class == "Witcher" :
                    print(f"Tvé schopnosti jsou: ")
                    for x, (ability) in enumerate(Hero.abilities):
                        print(f"|{x +1}|{ability}")
                    print(f"\nJako zklínač můžeš používat i znamení (cena --> 10 many) :\n")
                    time.sleep(1)
                    for x, (key, value) in enumerate(Hero.signs.items()):
                        print(f"|1{x + 1}|{key} - {value}")
                    print("")
                    time.sleep(3)
                    Hero.use_sign(Enemy)
                    time.sleep(2)
                    print(f"\n{Hero.name} má nyní {Hero.mana}/100 many.")
                    print(f"{Enemy.name} má nyní {Enemy.hp} HP.\n")

                    
                        

        elif action == 2:
            
                pass

        elif action == 3:
            for idx, (item, owned) in enumerate(Hero.equip.items(), 1):
                print(f"{idx}. {item} - {'Máš' if owned else 'Nemáš'}")
            print("")
            item_choice = input("Vyber si nástroj (číslo): ").strip()
            if item_choice.isdigit():
                item_choice = int(item_choice)
                if 1 <= item_choice <= len(Hero.equip):
                    item_name = list(Hero.equip.keys())[item_choice - 1]
                    if Hero.equip[item_name]:
                        Hero.skill += Hero.equip[item_name][1]  # Apply the multiplier if the item is owned
                        print(f"Máš {item_name} a ten ti zlepšuje sílu o {Hero.equip[item_name][1] * 100:.0f}%.")
                    else:
                        print(f"Nemáš {item_name}.")
                else:
                    print("Neplatná volba.")
            else:
                print("Zadej číslo nástroje.")

        elif action == 4:
            print(f"\n{Hero.name} - stav postavy:")
            print(f"HP: {Hero.hp}")
            print(f"Stamina: {Hero.stamina}")
            print(f"Mana: {Hero.mana}")
            print(f"Defense: {Hero.defense}")
            print(f"Abilities: {', '.join(Hero.abilities)}")
            time.sleep(4)

        elif action == 5:
            print("Díky za hraní! Nashledanou.\n")
            break

        else:
            print("Něco jsi zadal špatně. Opakuj.")
    else:
        print("\nNapiš číslo úkonu.")