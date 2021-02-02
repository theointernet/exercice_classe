"""
C'est mon github
"""


import random

class NPC:
    def __innit__(self):
        self.class_armure = die_roll(1d12)
        self.nom = ""
        self.race = ""
        self.espece = ""
        self.point_hp #d20
        self.profession = ""
        self.afficher_caractereriste

        #stats
        self.force = dice_roll("")
        self.agilite = dice_roll()
        self.constitution = dice_roll()
        self.intelligence = dice_roll()
        self.sagesse = dice_roll ()
        self.charisme = dice_roll()
    def set_string(self):
        self.nom = string
        self.race = string
        self.espece = string
        self.profession = string

class dice_roll:
    def __innit__(self, text input):
        self.diceamount = 0
        self.faceamount = 0
        dice_amount = int(text_input[0])
        face_amount = int(text_input[1])
        for i in range(4):
            values.append([random.randint(1, face_amount) for i in range(dice_amount)])
            print(values)
        return values.max()

    def get_max(self):
        return max(values)
    def somme(self):



class Kobold (NPC):