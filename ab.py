from a import *              # importování classi Postavy, funkce pozdrav, a proměné postava1 jakožto [self] classi Postavi

class Utok:                                      # třída Útok
    def __init__(self, postava):                 # init závislí na Utoku s vložením postava ergo v tomto případě postsva1 jako dárce vnitřních promněných
            self.name = postava.name             # vnitřní promněné hodnoty závislé na postavě postava1
            self.dmg = int(len(postava.name))

utok1 = Utok(postava1)                                          # inicializace Utoku se [self] formy postava1
def utoceni():
    print(f"Toto je utok od {utok1.name} za {utok1.dmg} dmg. ")     # prompt využívá proměnou utok1 z classi Utok

def pozdrav():                                 # tato funkce mimo classu využívá importovanou proměnou postava1 s classou Postava
    print(f"Ahoj, já jsem {postava1.name}! Mám {postava1.hp} Hpčko a {postava1.acesori[1]} a {postava1.acesori[0]} .")

# pozdrav()        # vzhledem k volání importu, není třeba zadávat typ [selfu]