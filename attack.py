# attack a druhy attacků
import random
import time
import sys
from text import *
from chractering import *
from potion import *
from items import *
from effect import *
from h_characters import *
from e_chracters import *
from base_character import *


class Attack:
    def __init__(self, attacker, name, base_dmg, dmg_type, effects=None):
        self.attacker = attacker  # instance postavy, která útočí
        self.name = name
        self.base_dmg = base_dmg
        self.dmg_type = dmg_type
        self.effects = effects or []
        self.multiplier = self.skill  # vynásobíme dovedností, možnist přidání multiplieru z vybavení

    def calculate_damage(self):
        return int(self.base_dmg * self.multiplier)

