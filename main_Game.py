import random, time, sys
from contants import *
from attack import *
from base_character import *
from h_characters import *


Enemy = Character(f"{random.choice(enemy_names)}", f"{random.choice(characters)}")  # Initialize Enemy character
Enemy.en_classing(f"{random.choice(characters)}")  

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

                        # add signs as 3. option with euqual chance for all signs
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
                            if random.randint(1, 5) == 1:
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
                            print(f"{Enemy.name} použil útok 'Terrifying Roar'! (15 až 25 dmg, sníží obranu a má šanci na omráčení)")
                            terrifying_roar_attack = Attack(Enemy, "Terrifying Roar", base_dmg=random.randint(15, 25), dmg_type="psychic", effects=None)
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
