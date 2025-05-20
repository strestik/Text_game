import random

class Character:
    def __init__(self, name, char_class, hp, stamina, defense, skill, respect, abilities):
        self.is_alive = True
        self.name = name
        self.char_class = ["Monster", "Sorccer", "Archerer", "Witcher", "Jarl", "Bard"][char_class]
        self.hp = hp
        self.stamina = stamina
        self.mana = 100 if self.char_class == "Sorccer" or "Witcher" else 0
        self.defense = defense
        self.skill = skill  # dmg multiplier
        self.abilities = abilities

        self.effects = {'burning': False, 'poisoned': False, 'stunned': False, 'frozen': False, 'bleeding': False}
        self.respect = 100 if self .char_class == "Bard" else respect
        self.elixiers = {
            "healing potion": False,
            "stamina potion": False,
            "mana potion": False,
        }
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
        self.hp = 100
        self.stamina = 100
        self.char_class = "Witcher"
        self.abilities ["Silver Sword", "Steel Sword"],
        self.signs = sign()
        
    def sign(self):
        self.signs = {
            "Igni": {"burning": True,
                     "dmg": 20,},
            "Aard": "Wind",
            "Quen": "Shield",
            "Axii": "Mind Control",
            "Yrden": "Trap"
        }
    

        #  = {
        #     "Sorccer": ["Fireball", "Ice Spike", "Lightning Bolt"],
        #     "Archerer": ["Arrow Rain", "Poison Arrow", "Explosive Arrow"],
        #     
        #     "Jarl": ["War Cry", "Shield Bash", "Battle Roar"],
        #     "Bard": ["Song of Healing", "Inspiring Melody", "Lullaby"]
        # }


        
