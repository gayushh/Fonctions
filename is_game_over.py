info_player1 = {'hub':
                    {'energy': 1000,
                     'capacity': 5000,
                     'structure_punts': 25,
                     'coordinates': (8, 10),
                     'regeneration_rate': 300
                     }}
info_player2 = {'hub': {'energy': 0,
                        'capacity': 5000,
                        'structure_punts': 25,
                        'coordinates': (15, 20),
                        'regeneration_rate': 300
                        }}

nb_turns = 25


def is_game_over(nb_turns, info_player1, info_player2):
    """
    Tell if the game is over.

    Parameters
    ______
    nb_turns : number of turns of play
    info_player1 : player's dico 1
    info_player2 : player's dico 2

    Returns
    _______
    True : the game is over (bool)
    False : the game continue (bool)

    Version
    ______
    Specification : Marie Heneffe (v.1 19/02/2020)
    Implementation : Marie Heneffe (v.1 05/03/2020)

    """

    for hub in info_player1:
        if 'energy' in hub == 0:
            return True

    for hub in info_player2:
        if 'energy' in hub == 0:
            return True

    if nb_turns >= 40:
        return True

    return False

print(is_game_over(nb_turns, info_player1, info_player2))
