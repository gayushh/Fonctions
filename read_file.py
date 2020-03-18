def read_file(path):
    """Reads the file with info about the map and returns all dictionnaries nessecery tot make the game work.

    Parameters
    ----------
    path: path of file (str)

    Returns
    ----------
    info_map: dictionnary that contains info about the map
    info_peaks: dictionnary with info about peaks
    info_player_1: dictionnary with info about player 1
    info_player_2 = dictionnary with info about player 2

    """

    # open file
    fh.open(path, 'r')

    # read file and split to get a list
    list_info_map = fh.readlines().split('/n','')

    fh_close()

    # creation dictionnaries
    info_map = {}
    info_peaks = {}
    info_player_1 = {}
    info_player_2 = {}
    
    # get elements with index and put in info_map

    info_map['('list_info_map[1]','list_info_map[2]')') = 'dimension_map'

    info_map['('list_info_map[4]','list_info_map[5]')') = 'hub_player_1'
    info_map['('list_info_map[8]','list_info_map[9]')') = 'hub_player_2'

    info_map['('list_info_map[13]','list_info_map[14]')') = 'peak_1'
    info_map['('list_info_map[16]','list_info_map[17]')') = 'peak_2'
    info_map['('list_info_map[19]','list_info_map[20]')') = 'peak_3'
    info_map['('list_info_map[22]','list_info_map[23]')') = 'peak_4'
    info_map['('list_info_map[25]','list_info_map[26]')') = 'peak_5'

    # get elements with index and put in info_peaks

    info_peaks['peak_1'] = list_info_map[15]
    info_peaks['peak_2'] = list_info_map[18]
    info_peaks['peak_3'] = list_info_map[21]
    info_peaks['peak_4'] = list_info_map[24]
    info_peaks['peak_5'] = list_info_map[27]

    # create info_player_1 with different 'under'dicos

    info_player_1['hub'] = {}
    info_player_1['cruisers'] = {}
    info_player_1['tankers'] = {}


    # get elements with index and put in info_player_1

    info_player_1['hub']['energy'] = list_info_map[6]
    info_player_1['hub']['capacity'] = list_info_map[6]
    info_player_1['hub']['regeneration_rate'] = list_info_map[7]
    info_player_1['hub']['range'] = list_info_map[4]
    info_player_1['hub']['column'] = list_info_map[5]

    # get elements with index and put in info_player_2

    info_player_2['hub'] = {}

    info_player_2['hub']['energy'] = list_info_map[10]
    info_player_2['hub']['capacity'] = list_info_map[10]
    info_player_2['hub']['regeneration_rate'] = list_info_map[11]
    info_player_2['hub']['range'] = list_info_map[8]
    info_player_2['hub']['column'] = list_info_map[9]

    # return

    return info_map, info_peaks, info_player_1, info_player_2
             
    # test hbsjbcjbcjsbcjbcjh
