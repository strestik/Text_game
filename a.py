class Postava:                      # třída Postava
    def __init__(self, name):       # init s vložením jména , je závislí na Postavě 
        self.hp = 1                     # hodnoty initu
        self.name = name
        self.acesori = ["luk", "meč"]
    
## def pozdrav(self):              # funkce nezávislá na Postavě s nutnosti zadávání [self] - momentální postavy ( se zadaným jménem)
##     print(f"Ahoj, já jsem {self.name}! Mám {self.hp} Hpčko a {self.acesori[1]} a {self.acesori[0]} .")

postava1 = Postava("Kal El")    # inicializace postavi1 classou Postava se zadaným jménem 
## pozdrav(postava1)               # self je zde postava1

