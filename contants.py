import time, random, sys

alive = True
delay = 2
round_counter = 1




titles = [
    "Neporazitelný",
    "Khemrikara",
    "Velký král Nehekhary",
    "Král králů",
    "Velekrál Khemri",
    "Potomek bohů",
    "Velký jestřáb nebes",
    "Vyvolený Ptry",
    "Posvátný potomek Usiriana",
    "Šampion Velké pouště",
    "Pán Země",
    "Vládce oblohy",
    "Přinášející světlo",
    "Vyvolený bohů",
    "Překonavší kodex mrtvých",
    "Věčný vládce dvou zemí",
    "První kněžský král",
    "Světlo Nehekhary",
    "Nepokojný",
    "Zlatý faraon",
    "Metla bezvěrců",
    "Věčný král",
    "Nesporný vládce Khemri a celé Nehekhary",
    "Jediný pravý král",
    "Král Divokého honu",
    "Řezník světů",
    "Chladný plamen prázdnoty",
    "Elfská záhada",
    "Bílý plamen tančící na mohylách svých nepřátel",
    "Zrádce z Thaneddu",
    "Bestie v lidské kůži",
    "Ohař Vilgefortze",
    "Bestie z Beauclairu",
    "Pán zrcadel",
    "Oheň Salamandry",
    "Vrah králů",
    "Falešný prorok",
    "Šílený král",
    "Černý jezdec",
    "Šeptač ze stínů",
    "Čarodějka stínů",
    "Pavoučí tkadlec války",
    "Čepel v zahradě",
    "Paní kontroly"
]


enemy_names = [
    "Eredin",
    "Imlerith",
    "Caranthir",
    "Avallac'h",
    "Emhyr",
    "Vilgefortz",
    "Bonhart",
    "Rience",
    "Dettlaff",
    "Gaunter",
    "Azar",
    "Letho",
    "Jacques",
    "Radovid",
    "Cahir",
    "Stefan",
    "Fringilla",
    "Sigismund",
    "Reynard",
    "Tissaia",
    "Settra"
]

characters = [
    "Witcher",
    "Sorcerer",
    "Archer",
    "Jarl",
    "Bard",
    "Monster"
]

# stored dictionarys for characters

store_effects = {"burning": {"is" : False, "duration": 0}, 
                "poisoned": {"is" : False, "duration": 0}, 
                "stunned": {"is" : False, "duration": 0}, 
                "frozen": {"is" : False, "duration": 0}, 
                "bleeding": {"is" : False, "duration": 0}, 
                "healing": {"is" : False, "duration": 0}, 
                "stamina regen": {"is" : False, "duration": 0},
                "shielding" : {"is" : False, "duration" : 0},
                "cleanse" : {"is" : False, "duration" : 0}
                }

store_elixirs = {# AI Ideas
                        # "white honey": {"own": 1, "amount": 0, "duration": 0},  # cleanses all effects
                        # "thunderbolt": {"own": 1, "amount": 0.25, "duration": 4},  # skill multiplier
                        # "cat": {"own": 1, "amount": 0.15, "duration": 4},  # defense multiplier
                        # "swallow": {"own": 1, "amount": 0.25, "duration": 4},  # healing multiplier
                        # "white gull": {"own": 1, "amount": 0.25, "duration": 4},  # mana multiplier
                        # "black blood": {"own": 1, "amount": 0.25, "duration": 4},  # defense against monsters
                "healing potion": {"own": 3,"amount": 50},
                "stamina potion": {"own": 3,"amount": 45},
                "mana potion": {"own": 3,"amount": 35}, 
                "vlaštovka": {"own": 1,"amount": 25, "duration" : 4}, # duration healing
                "hrom": {"own": 2,"amount": 1.5}, # dmg multiplier
                "vlk": {"own": 2,"amount": 0.15}, # sklill multiplier
                "medvěd": {"own": 2,"amount": 0.25}, # defense multiplier
                "blizzard": {"own": 1,"amount": 20, "duration" : 4}, # stamina regen
                }

store_equip = {# "iron claws": {"own":False,"dmg_mutipl": 0.25},  # [owned, dmg multiplier]
                # "elven lute": {"own":False,"dmg_mutipl": 0.25},  
                # "siderite sword": {"own":False,"dmg_mutipl": 0.25},
                # "skellige axe": {"own":False,"dmg_mutipl": 0.25},
                # "brokilon bow": {"own":False,"dmg_mutipl": 0.25},
                # "dimeritium staff": {"own":False,"dmg_mutipl": 0.25},
                # "mahakam hammer" : {"own":False,"dmg_multiplier": 0.35}
                "bomb": {"own":True,"dmg": 60, "effect": None},  # [owned, base dmg]
                "poison bomb": {"own":True,"dmg": 50, "effect": "poisoned"},  # [owned, base dmg, effect]
                "fire bomb": {"own":True,"dmg": 50, "effect": "burning"},  
                "frost bomb": {"own":True,"dmg": 50, "effect": "frozen"}, 
                }