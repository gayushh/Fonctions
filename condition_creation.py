def conditions_creation(player, type_new_unit):
    
    """
    Verify all conditions to make sure the creation of a unit is possible, returns true if creation is possible, false if not.
 
    Parameters
    ——————
    player: player that wants to create the new unit(str)
    type_new_unit: type of new unit tanker or cruiser (str)
 
    Returns
    ——————
    True : creation is possible (bool)
    False : creation unpossible (bool)
 
    Version
    ——————
    specification: Caroline Heijmans(v.1 19 / 02 / 2020)
    specification : Caroline Heijmans(v.2 10 / 03 / 2020)
 
    """

    if nb_creation <= 2 :

        nb_creation +=1

        if type_new_unit = cruiser :
            if calcul_energy >= 750 :
                return True 

        elif type_new_unit = tanker :
            if calcul_energy >= 1000 :
                return True 

        else :
            return False


def creation_units(name_new_unit, type_new_unit, player):
 
    """" 
    This function creates a unit with a name and coordinates, according to what the player chooses.It returns the dictionnary with all the infos about the player and also the one about the map called info_player_x and info_map.
 
    Parameters
    ——————
    name_new_unit : name to give to the new unit(str)
    type_new_unit : type of unit, tanker or cruiser(str)
    player : name of the player who want to create an unit

    Returns
    ——————
    info_player_x: dictionnary that containts infos about the player who just created a new unit(str)
    info_map: dictionnary that containts infos about the map(str)
 
    Version
    ——————
    specification: Caroline Heijmans(v.1 19 / 02 / 2020)
    specification: Caroline Heijmans(v.2 05 / 03 / 2020)
 
    """

    # If player est le player 1? comment faire => ne pas mettre le nom du joueur mais le dico associé? #
    # Changer spec si ça marche avec les autres fonctions #
    # Ici j'ai fait comme si c'était joueur 1 mais il va falloir adapter ! #

    # Get where new unit is gonna appear

    hub_range = info_player_1['hub']['range']
    hub_column = info_player_1['hub']['column']

    # Check conditions

    if conditions_creation == True :

       
        if type_new_unit == cruiser :

            # create cruiser in info_player
            info_player_1['cruisers'][name_new_unit] = {}
            info_player_1['cruisers'][name_new_unit]['energy'] = 400
            info_player_1['cruisers'][name_new_unit]['capacity'] = 400
            info_player_1['cruisers'][name_new_unit]['structure_points'] = 100
            info_player_1['cruisers'][name_new_unit]['move_price'] = 10
            info_player_1['cruisers'][name_new_unit]['fight_price'] = 10
            info_player_1['cruisers'][name_new_unit]['shooting_range'] = 1
            info_player_1['cruisers'][name_new_unit]['range'] = hub_range
            info_player_1['cruisers'][name_new_unit]['column'] = hub_column

            # create cruiser in info_map
            info_map['('hub_range','hub_column')') = name_new_unit

            print('cruiser was created')

        # create tanker in info_player
        elif type_new_unit == tanker :

            info_player_1['tankers'][name_new_unit] = {}
            info_player_1['tankers'][name_new_unit]['energy'] = 600
            info_player_1['tankers'][name_new_unit]['capacity'] = 600
            info_player_1['tankers'][name_new_unit]['structure_points'] = 50
            info_player_1['tankers'][name_new_unit]['move_price'] = 0
            info_player_1['tankers'][name_new_unit]['range'] = hub_range
            info_player_1['tankers'][name_new_unit]['column'] = hub_column

            # create cruiser in info_map
            info_map['('hub_range','hub_column')') = name_new_unit

            print('tanker was created')

        else :
            print ('There must be an error when you type your order with creation')

    else :

        print('New unit can t be created because conditions aren t respected')

    return info_player_x , info_map
        






 
