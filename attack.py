from contants import *
from base_character import *

class Attack:
    def __init__(self, attacker, name, base_dmg, dmg_type, multiplier ,effects=None):
        self.attacker = attacker  # instance postavy, která útočí
        self.name = name
        self.base_dmg = base_dmg
        self.dmg_type = dmg_type
        self.effects = effects or []
        self.multiplier = multiplier # vynásobíme dovedností, možnist přidání multiplieru z vybavení

    def calculate_damage(self):
        return int(self.base_dmg * self.multiplier)

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
            igni_attack = Attack(self, "Igni", base_dmg=30, dmg_type="fire", effects=["burning"])
            self.mana -= 10  # Reduce mana for using the sign
            time.sleep(1)
            target.take_damage(igni_attack)
            target.effects["burning"]["duration"] += 3
            target.effects["burning"]["is"] = True
            break

        elif sign_choice == 12:
            print(f"\n{self.name} použil znamení Aard a omráčil nepřítele.")
            time.sleep(1)
            aard_attack = Attack(self, "Aard", base_dmg=20, dmg_type="stun", effects=["stunned"])
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


def taunt(self, target):
    self.stamina_check()
    if self.respect > 150 and random.randint(1, 20) == 17:
        target.hp -= target.hp + 1
        print("Nepřítel nesnesl tvoji urážku a spadl na zem mrtví. Gratuluji urazil jsi nepřítele tak moc že to nepřežil.")

    if self.respect > 200 and random.randint(1, 15) == 7:
        target.hp -= target.hp + 1
        print("Nepřítel nesnesl tvoji urážku a spadl na zem mrtví. Gratuluji urazil jsi nepřítele tak moc že to nepřežil.")

    if self.respect > 250 and random.randint(1, 10) == 3:
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
