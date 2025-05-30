import random
import time
import sys
alive = True

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
            "crossbow": False,
            "sword": False,
            "axe": False,
            "bow": False,
            "bomb": False,
            "poison bomb": False,
            "fire bomb": False,
            }

    def is_alive_check(self):
        self.is_alive = False if self.hp <= 0 else True


        


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
        self.mana = 40
        self.defense = 80
        self.skill = 1.5
        self.abilities = ["Silver Sword", "Steel Sword"]

    def sign(self):
        self.signs = {
            "Igni": "burning 3 rounds",
            "Aard": "stunned 1 round",
            "Quen": "giant def 1 round ",
            "Axii": "mana + 20",
            "Yrden": "skill +",
            "Heliotrop": "def +"}

class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, "Sorcerer")
        self.hp = 110
        self.stamina = 40
        self.mana = 100
        self.defense = 50
        self.skill = 1.4
        self.abilities = ["Fireball", "Ice Spike", "Lightning Bolt"]

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, "Archer")
        self.hp = 130
        self.stamina = 100
        self.mana = 0
        self.defense = 60
        self.skill = 1.3
        self.abilities = ["Arrow Rain", "Poison Arrow", "Explosive Arrow"]

class Jarl(Character):
    def __init__(self, name):
        super().__init__(name, "Jarl")
        self.hp = 170
        self.stamina = 100
        self.mana = 0
        self.defense = 90
        self.skill = 1.1
        self.abilities = ["War Cry", "Shield Bash", "Battle Roar"]

class Bard(Character):
    def __init__(self, name):
        super().__init__(name, "Bard")
        self.hp = 120
        self.stamina = 80
        self.mana = 0
        self.defense = 40
        self.skill = 1.2
        self.respect = 50
        self.abilities = ["Song of Healing", "Inspiring Melody", "Lullaby"]

class Monster(Character):
    def __init__(self, name):
        super().__init__(name, "Monster")
        self.hp = 160
        self.stamina = 100
        self.mana = 0
        self.defense = 70
        self.skill = 1.3
        self.abilities = ["Claw Swipe", "Bite", "Roar"]
 





# Hero.witcher()  # Initialize as Witcher

# enemy = Character()  # Example enemy character




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
print(f"\nNyní můžeš začít hrát. Tvým úkolem je přežít a porazit nepřítele.\n") 
time.sleep(3)
print("Boj začínáš bez vybavení a vylepšení, jestli chceš použít meč nebo vypít lektvar, musíš na to využít kolo.\n")
time.sleep(3)
print("Ale neměj strách, protivník se připravuje, takže první tři kola na tebe nezaútočí.")
time.sleep(3)



while alive:
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
                for idx, (item, owned) in enumerate(Hero.equip.items(), 1):
                    print(f"{idx}. {item} - {'Máš' if owned else 'Nemáš'}")
                    print("")

                if Hero.char_class == "Witcher" :
                    print(f"Jako zklínač můžeš používat i znamení.")
                    pass

        elif action == 2:
            
                pass

        elif action == 3:
            pass

        elif action == 4:
            print(f"\n{Hero.name} - stav postavy:")
            print(f"HP: {Hero.hp}")
            print(f"Stamina: {Hero.stamina}")
            print(f"Mana: {Hero.mana}")
            print(f"Defense: {Hero.defense}")
            print(f"Abilities: {', '.join(Hero.abilities)}")

        elif action == 5:
            print("Díky za hraní! Nashledanou.\n")
            break

        else:
            print("Něco jsi zadal špatně. Opakuj.")
    else:
        print("\nNapiš číslo úkonu.")