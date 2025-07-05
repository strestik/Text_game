import time, random
from base_character import *
from attack import *


def apply_effects(self, h_amount, s_amount):    # možnost přidání časiového omezení efektů
    if self.effects["bleeding"]["is"] == True:
        if self.effects["bleeding"]["duration"] == 0:
            self.effects["bleeding"]["is"] = False
        else:
            print(f"\n{self.name} krvácí a ztrácí 10 HP.\n")
            self.hp -= 10
            self.effects["bleeding"]["duration"] -= 1
            if self.effects["bleeding"]["duration"] <= 0:
                self.effects["bleeding"]["is"] = False
                print(f"{self.name} přestal krvácet.\n")

    if self.effects["burning"]["is"] == True:
        if self.effects["burning"]["duration"] == 0:
                self.effects["burning"]["is"] = False
        else:
            print(f"\n{self.name} hoří a ztrácí 15 HP.\n")
            self.hp -= 15
            self.effects["burning"]["duration"] -= 1
            if self.effects["burning"]["duration"] <= 0:
                self.effects["burning"]["is"] = False
                print(f"{self.name} přestal hořet.\n")

    if self.effects["poisoned"]["is"] == True:
        if self.effects["poisoned"]["duration"] == 0:
            self.effects["poisoned"]["is"] = False
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
            self.effects["healing"]["is"] = False
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

    #if self.effects["cleanse"]["is"] == True:
        # if self.effects["cleanse"]["duration"] == 0:
        #     self.effects["cleanse"]["is"] = False
        #     print(f"{self.name} se přetal být očištěný.\n")
        # else:
        #     self.effects["cleanse"]["duration"] -= 1
        #     print(f"\n{self.name} je očištěn.\n")

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
            f"1. Healing Potion  (léčí 50 HP)                             [kusů : {self.elixiers['healing potion']['own']}]\n"
            f"2. Stamina Potion  (regeneruje 45 staminy)                  [kusů : {self.elixiers['stamina potion']['own']}]\n"
            f"3. Mana Potion     (regeneruje 35 many)                     [kusů : {self.elixiers['mana potion']['own']}]\n"
            f"4. Vlaštovka       (regeneruje 15 HP po dobu 3 kol)         [kusů : {self.elixiers['vlaštovka']['own']}]\n"
            f"5. Hrom            (zvyšuje násobí 1.5 krát sílu)           [kusů : {self.elixiers['hrom']['own']}]\n"
            f"6. Vlk             (zvyšuje sílu o 15%)                     [kusů : {self.elixiers['vlk']['own']}]\n"
            f"7. Medvěd          (zvyšuje obranu o 25%)                   [kusů : {self.elixiers['medvěd']['own']}]\n"
            f"8. Blizzard        (regeneruje 20 staminu po dobu 3 kol)    [kusů : {self.elixiers['blizzard']['own']}]\n")
            # f"9. Černá krev      (následující 3 kola nemůžeš být omráčen) [kusů : {self.elixiers['černá krev']['own']}]\n")

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


