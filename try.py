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


        
    def use_item(self):
        item_choice = input("Vyber si nástroj (číslo): ").strip()

        if item_choice.isdigit():
            item_choice = int(item_choice)

            if 1 <= item_choice <= len(Hero.equip):
                item_name = list(Hero.equip.keys())[item_choice - 1]

                if Hero.equip[item_name]:
                    if item_name == "bomb":
                        if Hero.equip[item_name]['own'] == True:
                            print(f"Máš {item_name} ten dává {Hero.equip[item_name]['dmg']} základního poškození.")
                            bomb_attack = Attack(Hero, "Bomb", base_dmg=Hero.equip[item_name]['dmg'], dmg_type="explosive")
                            Enemy.take_damage(bomb_attack)
                            print(f"{Enemy.name} má nyní {Enemy.hp} HP.")
                            Hero.equip[item_name]['own'] = False 
                        else:
                            print(f"Nemáš {item_name}. Zkus to znovu.")
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
                            print(f"Nemáš {item_name}. Zkus to znovu.")
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
                            print(f"Nemáš {item_name}. Zkus to znovu.")
                            Hero.use_item()
                        time.sleep(2)
                    
                    elif item_name == "frost bomb":
                        if Hero.equip[item_name]['own'] == False:
                            print(f"{Hero.name} použil {item_name} a způsobil {Hero.equip[item_name]['dmg']} poškození s efektem zmrazení.")
                            frost_attack = Attack(Hero, "Frost Bomb", base_dmg=Hero.equip[item_name]['dmg'], dmg_type="explosive", effects=["frozen"])
                            Enemy.take_damage(frost_attack)
                            print(f"{Enemy.name} má nyní {Enemy.hp} HP.")
                            Hero.equip[item_name]['own'] = False  # Remove the item after use
                        else:
                            print(f"Nemáš {item_name}. Zkus to znovu.")
                            Hero.use_item()
                        time.sleep(2)
                    
                    else :
                        if Hero.equip[item_name]['own'] == True:
                            Hero.skill += Hero.equip[item_name]["dmg_mutipl"]  # Apply the multiplier if the item is owned
                            print(f"""Máš {item_name} a ten ti zlepšuje sílu o {Hero.equip[item_name]["dmg_mutipl"] * 100:.0f}%.""")
                            print(f"{Hero.name} má nyní sílu {Hero.skill * 100:.0f}%.")
                        else:
                            print(f"Nemáš {item_name}. Zkus to znovu.")
                            Hero.use_item()
                        time.sleep(2)

                else:
                    print(f"Nemáš {item_name}.")
            else:
                print("Neplatná volba.")
        else:
            print("Zadej číslo nástroje.")
        
Enemy = Character("Enemy", "Monster")
Hero = Character("Hero", "")

while True:
    
    for index, item in enumerate(Hero.equip, start=1):                                                 # len(list(Hero.equip.items())):
        print(f"|{index}| {item} - {'Máš' if Hero.equip[item]['own'] == True else 'Nemáš' }")          # Hero.equip[item]
    print("\nPozor!!!, od každé bomy máš jen jeden kus, takže je používej opatrně.\n")
    Hero.use_item()  # Použití nástroje
    print(f"{Hero.name} má nyní {Hero.hp} HP a {Hero.skill * 100:.0f}% sílu.")
    print(f"{Enemy.name} má nyní {Enemy.hp} HP a {Enemy.skill * 100:.0f}% sílu.")
