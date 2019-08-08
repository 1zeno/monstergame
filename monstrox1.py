from random import randint
class Monstros :

    def __init__(self, name, el_type, pow_attack, pow_def, hp, evo, level):
        self.name = name
        self.el_type = el_type
        self.pow_attack = pow_attack
        self.pow_def = pow_def
        self.hp = hp
        self.evo = evo
        self.level = level
        self.fstatus = 2 

    def attack(self):

        return self.pow_attack * self.evo * self.level * randint(1, 5)


    def deff(self):

        return self.pow_def * self.evo * self.level * randint(1, 3)


def duelo (tr1,tr2):

    tr1.fstatus = 1
    tr2.fstatus = 0
    count = 1
    while(tr1.hp > 0 and tr2.hp > 0):

        print("\nRound ",count ,tr1.name ,tr1.hp," contra ",tr2.name ,tr2.hp)
        count+=1
        if(tr1.fstatus == 1 and tr1.hp > 0):
            
            print("\n ",tr1.name," ATACA ",tr2.name)
            tr2.hp -= tr1.attack() - tr2.deff()
            tr1.fstatus = 0
            tr2.fstatus = 1

        if(tr2.fstatus == 1 and tr2.hp > 0):
            
            print("\n ",tr2.name," ATACA ",tr1.name,)
            tr1.hp -= tr2.attack() - tr1.deff()
            tr1.fstatus = 1
            tr2.fstatus = 0
        

    if (tr1.hp > tr2.hp):
        print("\n",tr1.name, "venceu ")

    else:
        print("\n",tr2.name, "venceu ")


mon1 = Monstros("Wildwind", "vento", 10, 5 , 5000 , 2 , 5)

mon2 = Monstros("Splash", "agua", 10, 5 , 5000 , 2 , 5)

duelo(mon1,mon2)


