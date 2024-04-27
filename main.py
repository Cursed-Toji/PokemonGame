from pokegame import *
from personagens import *

def escolher_pokemon_inicial(player):
    print('ola {}! pode escolher o poke inicial'.format(player))

    pikachu = Pokemon_Eletricos('pikachi', level=1)
    charmanter = Pokemon_Fogo('charmanter', level=1)
    squirtle = Pokemon_Agua('squirtle', level=1)


    print('escolher o poke inicial')
    print('1-' , pikachu)
    print('2-' , charmanter)
    print('3-' , squirtle)

    while True:
        escolha = input('Escolha o poke inicial: ')
        try:
            if escolha == '1':
                player.capturar_pokemon(pikachu)
                break
            elif escolha == '2':
                player.capturar_pokemon(charmanter)
                break
            elif escolha == '3':
                player.capturar_pokemon(squirtle)
                break
            else:
                print('Escolha invalida')
        except KeyboardInterrupt:
            print('escolha errada')


player = Jogador('victor')
player.capturar_pokemon(Pokemon_Fogo('charmanter', level=1))

inimigo1 = Inimigo(name='cals', pokemon=[Pokemon_Fogo('squirtle', level=1)])


player.batalhar(inimigo1)