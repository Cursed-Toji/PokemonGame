# from pokegame import Pokemon_Eletricos, Pokemon, Pokemon_Agua, Pokemon_Fogo
 #importar tudo
from pokegame import *
import random

NOMES = [
    'ashe', 'red', 'mist', 'brok', 'serei', 'yagami', 'yuta', 'gojo'
]

POKEMONS = [
    Pokemon_Fogo('charmander'),
    Pokemon_Fogo('blaziken'),
    Pokemon_Fogo('Charizard'),
    Pokemon_Agua('kyogre'),
    Pokemon_Agua('Squirtle'),
    Pokemon_Agua('Blastoise'),
    Pokemon_Eletricos('Pikachu'),
    Pokemon_Eletricos('Raichu'),
    Pokemon_Eletricos('Electabuzz'),
    Pokemon_Fogo('Magmar'),
    Pokemon_Fogo('Arcanine'),
    Pokemon_Agua('Vaporeon'),
    Pokemon_Agua('Gyarados'),
    Pokemon_Agua('Lapras'),
    Pokemon_Eletricos('Jolteon'),
    Pokemon_Eletricos('Zapdos'),
    Pokemon_Eletricos('Electivire')
]
class Personagem:

    def __init__(self, name=None, pokemon=[]):
        if name:
            self.name = name
        else:
            self.name = random.choice(NOMES)

        self.pokemon = pokemon

    def __str__(self):
        return self.name


    def mostrar_pokemon(self):
        # se eu tenho pokemon mostra o codigo
        if self.pokemon:
            print('pokemons de: ' + self.name)
            #um for pra percorrer a lista que eu tenho
            for index, pokemon in enumerate(self.pokemon):
                print("{}- {}".format(index, pokemon))
        else:
            print('{} No pokemon'.format(self.name))

    def escolher_pokemon(self):
        self.mostrar_pokemon()
        if self.pokemon:
            while True:
                escolha = input('Escolha o poke inicial: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemon[escolha]
                    print('{} pokemon escolhido'.format(pokemon_escolhido))
                    return pokemon_escolhido
                except ValueError:
                    print('print escolha invalida')
                except Exception as error:
                    print(error)
        else:
            print('Erro, jogador está sem pokemon')

    def batalhar(self, personagem):
        print('{} Iniciou uma batalha com {}'.format(self, personagem))

        personagem.mostrar_pokemon()
        personagem.escolher_pokemon()

        self.escolher_pokemon()


class Jogador(Personagem):
    tipo = 'joador'

    def capturar_pokemon(self, pokemon):
        self.pokemon.append(pokemon)
        print('{} capturou o pokemon {}'.format(self, pokemon)) # se eu passar self pokemon aparece objetc e as paradas estranhas



class Inimigo(Personagem):
    tipo = 'adversarial'
    def __init__(self, name=None, pokemon=[]):
        if not pokemon:
            for i in range(random.randint(1,6)):
                pokemon.append(random.choice(POKEMONS))

        super().__init__(name=name, pokemon=pokemon)


    def escolher_pokemon(self):
        if self.pokemon:
            pokemon_escolhido = random.choice(self.pokemon)
            print('{} Escolheu {}'.format(self.name,pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('Erro, jogador está sem pokemon')

