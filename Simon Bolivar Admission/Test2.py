class superPoder:
    def __init__(self, nombre, damage):
        self.nombre = nombre
        self.damage = damage


class superPoderEspecial:
    def __init__(self, nombre, damage, bonus):
        superPoder.__init__(self, nombre, damage)
        self.bonus = bonus

class superHeroe:
    def __init__(self, nombreHeroe, nombreOriginal, salud, superPoderNormal, superPoderEspecial):
        self.nombreHeroe = nombreHeroe
        self.nombreOriginal = nombreOriginal
        self.salud = salud
        self.superPoderNormal = superPoderNormal
        self.superPoderEspecial = superPoderEspecial
        
    
    def atacar(self, power, sujeto):
        sujeto.salud = sujeto.salud - power.damage
        return
    
    def atacar2(self, power, sujeto):
        sujeto.salud = sujeto.salud - power.damage - power.bonus
        return

class villano:
    def __init__(self, nombreHeroe, nombreOriginal, salud, superPoderNormal, superPoderEspecial):

        superHeroe.__init__(self, nombreHeroe, nombreOriginal, salud, superPoderNormal, superPoderEspecial)

poder1 = superPoder("Garras Afiladas", 100)
poder2 = superPoderEspecial("Pistola", 100, 100)
hero1 = superHeroe("Batman", "Alexanyer", 2500, poder1, poder2)
villano1 = superHeroe("Tukeke", "Rangel", 1500, poder1, poder2)
hero1.atacar(poder1, villano1)
hero1.atacar2(poder2, villano1)
print(hero1.salud)
print(villano1.salud)