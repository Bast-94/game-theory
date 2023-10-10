from itertools import product

import numpy as np

from sources import GameMatrix

game_matrix = GameMatrix()
game_matrix.init_winning_probs()
mat = game_matrix.dice_matrix - game_matrix.dice_matrix.T
# print(mat)
couples = np.array(np.where(mat > 0))
couples = couples.T
# print(couples)
dict_with_lists = {"A": [1, 2], "B": ["x", "y"], "C": [True, False]}


def gen_list_of_dicts(dict_with_lists):
    # Utilisez product pour obtenir une liste de dictionnaires
    list_of_dicts = [
        dict(zip(dict_with_lists.keys(), values))
        for values in product(*dict_with_lists.values())
    ]
    return list_of_dicts


# 'list_of_dicts' contiendra la liste de dictionnaires souhaitée
#
list_of_dicts = gen_list_of_dicts(dict_with_lists)
print(list_of_dicts)
