# from base_character import Hero
Hero = ("Hero", "") 
Enemy = ("Enemy", "") 


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