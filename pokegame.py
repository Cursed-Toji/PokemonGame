import random

class Pokemon:
    def __init__(self, especie, nome=None, level=None):
        self.especie = especie
        self.level = level

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        if nome:
            self.nome = nome
        else:
            self.nome = self.especie

        #eu definindo dessa forma consigo puxar no print só passando print meuu_pokemon
    def __str__(self):
        #o STR sempre vai retornar uma string
        # return self.especie
        #desta forma vai retorna os 2
        return '{} ({})'.format(self.nome, self.level)

    def atacar(self, pokemon):
        print('{} atacou {}!'.format(self, pokemon))



class Pokemon_Eletricos(Pokemon):
    tipo = 'eletrico'
    def atacar(self, pokemon):
        print('{} atacou com choque do trovão em {}'.format(self, pokemon))


class Pokemon_Fogo(Pokemon):
    tipo = 'Fogo'
    def atacar(self, pokemon):
        print('{} atacou com bola de fogo em {}'.format(self, pokemon))

class Pokemon_Agua(Pokemon):
    tipo = 'Agua'
    def atacar(self, pokemon):
        print('{} atacou com Jato de agua em {}'.format(self, pokemon))



