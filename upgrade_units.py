def upgrade_unit(type_of_improvement):
    """
    This function resumes the differents possibilities of upgrades that a player can do.

    Parameter
    ----------
    type_of_improvement: what kind of upgrade the player wants make (str)
 
    Return
    ----------
    #regeneration_rate: value of the regeneration rate of the hub
    #tanker_capacity: value of the capacity in energy of a tanker
    #shoot_range: range of the shoot of a cruiser
    #move_cost: cost for the move of a cruiser
    info_player : dico that includes all of the unities and theirs characteristics
 
    Version:
    Specification : Maxence Weyns (v.1 19/02/20)
    implementation : Caroline Heijmans (v.2 11/03/2020)
    """

    if type_of_improvement == regeneration :

        # Check conditions
        if condition_upgrade() == True :

            # Upgrade regeneration rate of the hub
            info_player_1['hub']['regeneration_rate'] += 5

            # Payement
            info_player_1['hub']['energy'] -= 750

        else :
            print('upgrade of regeneration is not possible bc not enough ressources')

    elif type_of_improvement == storage :

        # Check conditions
        if condition_upgrade() == True :

            # Upgrade storage of tankers
            for tanker in info_player_1['tankers'] :

                info_player_1['tankers'][tanker]['capacity'] += 100
            
            # Payement
            info_player_1['hub']['energy'] -= 600

        else :
            print('upgrade of regeneration is not possible bc not enough ressources')


    elif type_of_improvement == range :

        # Check conditions
        if condition_upgrade() == True :

            # Upgrade shooting range of cruisers
            for cruiser in info_player_1['cruisers'] :

                info_player_1['cruisers'][cruiser]['shooting_range'] += 1 

            # Payement
            info_player_1['hub']['energy'] -= 400

        else :
            print('upgrade of regeneration is not possible bc not enough ressources')


    elif type_of_improvement == move :

        # Check conditions
        if condition_upgrade() == True :

            # Diminuates move price of cruisers
            for cruiser in info_player_1['cruisers'] :

                info_player_1['cruisers'][cruiser]['move_price'] -= 1 

            # Payement
            info_player_1['hub']['energy'] -= 500

        else :
            print('upgrade of regeneration is not possible bc not enough ressources')

    else :
        print('there must be an error when you typed your orders')

    return info_player_1

def condition_upgrade(type_of_improvement):
    """
    This function verify if the energy in the hub is enough for actions.
    
    Parameter
    ----------
    type_of_improvement: what kind of upgrade the player wants make (str)
 
    Return:
    condition_upgrade: if conditions are okay or not (bool)
 
    Version:
    Specification : Maxence Weyns (v.1 23/02/20)
    Specification : Caroline Heijmans (v.2 19/03/2020)
    Implementation : Caroline Heijmans (v.1 19/03/2020)
    """
    if type_of_improvement == regeneration:
        
        if info_player_1['hub']['regeneration_rate'] == 50:
            print('you have the maximal regeneration rate')
            return False
        else:
            if calcul_energy >= 750 :
                return True
            else:
                print('you dont have enough money for improve regeneration')
                return False
           
       
    elif type_of_improvement == storage:
        
        for tanker in info_player_1['tankers'] :
            if info_player_1['tankers'][tanker]['capacity'] == 1200:
                print ('you have the maximal capacity for your tankers')
                return False
            else:
            if calcul_energy >= 600 :
                return True
            else:
                print('you dont have enough money for improve storage')
                return False
    
    elif type_of_improvement == range :
        
        for cruiser in info_player_1['cruisers'] :
            if info_player_1['cruisers'][cruiser]['shooting_range'] == 5:
                print ('you have the maximal range for your cruisers')
                return False
            else:
            if calcul_energy >= 400 :
                return True
            else:
                print('you dont have enough money to improve range')
                return False
            
    elif type_of_improvement == move: 
        
        for cruiser in info_player_1['cruisers'] :
            if info_player_1['cruisers'][cruiser]['move_price'] == 5 :
                print ('you have the minimal moveprice for your cruisers')
                return False
            else:
            if calcul_energy >= 500 :
                return True
            else:
                print('you dont have enough money to diminuate move price')
                return False
        
        
  
       
    
