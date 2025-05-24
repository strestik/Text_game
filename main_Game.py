import random
import time
import sys
alive = True
#  hp, stamina, defense, skill, respect, abilities

class Character:
    def __init__(self, name, char_class,):
        self.is_alive = True
        self.name = name
        self.char_class = ["Monster", "Sorccer", "Archerer", "Witcher", "Jarl", "Bard"][char_class]
        self.hp = 100
        self.stamina = 0
        self.mana = 100 if self.char_class == "Sorccer" else 40 if self.char_class == "Witcher" else 0
        self.defense = 70
        self.skill = 1.2  # dmg multiplier
        self.respect = 100 if self.char_class == "Bard" else 15
        self.abilities = []

        self.effects = {"burning": False, "poisoned": False, "stunned": False, "frozen": False, "bleeding": False}
        self.elixiers = {
            "healing potion": False,
            "stamina potion": False,
            "mana potion": False,}
        self.items = {
            "crossbow": False,
            "sword": False,
            "axe": False,
            "bow": False,
            "bomb": False,
            "poison bomb": False,
            "fire bomb": False,
            }

    def witcher(self):
        self.hp = 150
        self.stamina = 100
        self.mana = 40
        self.char_class = "Witcher"
        self.abilities = ["Silver Sword", "Steel Sword"]
        # self.signs = sign()

    def sorccer(self):
        self.hp = 110
        self.stamina = 40
        self.mana = 100
        self.char_class = "Sorccer"
        self.abilities = ["Fireball", "Ice Spike", "Lightning Bolt"]
        # self.signs = sign()

    def archerer(self):
        self.hp = 130
        self.stamina = 100
        self.mana = 0
        self.char_class = "Archerer"
        self.abilities = ["Arrow Rain", "Poison Arrow", "Explosive Arrow"]
        
    def jarl(self):
        self.hp = 170
        self.stamina = 100
        self.mana = 0
        self.char_class = "Jarl"
        self.abilities = ["War Cry", "Shield Bash", "Battle Roar"]
    
    def bard(self):
        self.hp = 120
        self.stamina = 80
        self.mana = 0
        self.char_class = "Bard"
        self.abilities = ["Song of Healing", "Inspiring Melody", "Lullaby"]

    def monster(self):
        self.hp = 160
        self.stamina = 100
        self.mana = None
        self.char_class = "Monster"
        self.abilities = ["Claw Swipe", "Bite", "Roar"]
    
    def attack(self):
        if self.is_alive and enemy.is_alive:
            damage = random.randint(10, 20) * self.skill
            enemy.hp -= damage
            print(f"{self.name} attacks {enemy.name} for {damage:.2f} damage!")

            if enemy.hp <= 0:
                enemy.is_alive = False
                print(f"{enemy.name} has been defeated!")
        else:
            print(f"{self.name} cannot attack because they are not alive.")

    

    def punch(self):
        if self.is_alive and enemy.is_alive:
            damage = random.randint(5, 10) * self.skill
            enemy.hp -= damage
            print(f"{self.name} punches {enemy.name} for {damage:.2f} damage!")
            if enemy.hp <= 0:
                enemy.is_alive = False
                print(f"{enemy.name} has been defeated!")
        else:
            print(f"{self.name} cannot punch because they are not alive.")


        
    def sign(self):
        self.signs = {
            "Igni": {"burning": True,
                     "dmg": 20,},
            "Aard": "Wind",
            "Quen": "Shield",
            "Axii": "Mind Control",
            "Yrden": "Trap"
        }



    def potion(self, potion_type):
        pass


        #  = {
        #     "Sorccer": ["Fireball", "Ice Spike", "Lightning Bolt"],
        #     "Archerer": ["Arrow Rain", "Poison Arrow", "Explosive Arrow"],
        #     
        #     "Jarl": ["War Cry", "Shield Bash", "Battle Roar"],
        #     "Bard": ["Song of Healing", "Inspiring Melody", "Lullaby"]
        # }

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
        print(f"1. Witcher\n"
          "2. Sorccer\n"
          "3. Archerer\n"
          "4. Jarl\n"
          "5. Bard\n"
          "6. Monster\n")
        char_class = input("Zadej číslo třídy: ").strip()

        if char_class.isdigit():
            char_class = int(char_class)
            if char_class == 1:
                self.witcher()
            elif char_class == 2:
                self.sorccer()
            elif char_class == 3:
                self.archerer()
            elif char_class == 4:
                self.jarl()
            elif char_class == 5:
                self.bard()
            elif char_class == 6:
                self.monster()
            else:
                print("--> Neplatná třída, zkus to znovu.\n")
                return self.classing()
        else:
            print("--> Neplatný vstup, zkus to znovu.\n")
            return self.classing()
        
        

 
# Hero.witcher()  # Initialize as Witcher
jm2 = Character("Crach Ain Craine", 4)
jm3 = Character("Marigold", 5)
jm4 = Character("Topivec", 0)
jm4 = Character("Triss", 1)
jm5 = Character("Jestřáb", 2)

enemy = Character("Monster", 0)  # Example enemy character
# Example usage

# if Hero.char_class == "Witcher":
#     Hero.witcher()

# elif Hero.char_class == "Jarl":
#     Hero.jarl()
# elif Hero.char_class == "Bard":  
#     Hero.bard()
# elif Hero.char_class == "Monster":
#     Hero.monster()
# elif Hero.char_class == "Sorccer":
#     Hero.sorccer()
# elif Hero.char_class == "Archerer":
#     Hero.archerer()


# print(Hero.name, Hero.char_class, Hero.hp, Hero.stamina, Hero.mana, Hero.defense, Hero.skill, Hero.respect)
# print(jm2.name, jm2.char_class, jm2.hp, jm2.stamina, jm2.mana, jm2.defense, jm2.skill, jm2.respect)
# print(jm3.name, jm3.char_class, jm3.hp, jm3.stamina, jm3.mana, jm3.defense, jm3.skill, jm3.respect)
# print(jm4.name, jm4.char_class, jm4.hp, jm4.stamina, jm4.mana, jm4.defense, jm4.skill, jm4.respect)
# print(jm5.name, jm5.char_class, jm5.hp, jm5.stamina, jm5.mana, jm5.defense, jm5.skill, jm5.respect)


while alive:
    Hero = Character("Hero", 0)  # Initialize Hero character
    print(f"\nVýtej hráč, vyber si svou postavu:")
    Hero.nameing()
    print("\n--> Hmm", end='', flush=True)
    for _ in range(4):
        time.sleep(0.3)
        print('.', end='', flush=True)
    print(f" {Hero.name}, to je dobré jméno! Vítej!!!\n")
    time.sleep(3.5)
    print(f"Vyber si svou třídu:\n")
    Hero.classing()
    print(f"\n---> Tvoje postava je {Hero.name}, třída: {Hero.char_class}, HP: {Hero.hp}, Stamina: {Hero.stamina}, Mana: {Hero.mana}, Defense: {Hero.defense}, Skill: {Hero.skill}, Respect: {Hero.respect}\n")
    print("Nyní můžeš začít hrát. Zde jsou dostupné akce:")
    
   

    action = input("Choose an action: ").strip().lower()