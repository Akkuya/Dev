"""CSCA08: Fall 2025 -- Assignment 1: Ice Hockey Fantasy Draft

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2025 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from constants import (
    POINTS_PER_GOAL,
    POINTS_PER_ASSIST,
    POINTS_PER_HIT,
    F_DCS_PER_POINT,
    D_DCS_PER_POINT,
    FORWARDS_NEEDED,
    DEFENCEMEN_NEEDED,
    GOALIES_NEEDED,
    BUDGET,
    PLAYERS_TO_SELECT,
    FORWARD,
    DEFENCEMEN,
    GOALIE,
    SV_VALUE,
    GAA_VALUE,
)


# provided
def get_player_id(player: str) -> str:
    """Return the id of player if the string is non-empty;
    otherwise return the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt

    >>> get_player_id('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    'MGO'
    >>> get_player_id('NSH_PF_G7-_A14_DC20_H73_Pr10')
    'NSH'
    >>> get_player_id('')
    ''

    """
    if len(player) == 0:
        return ''
    return player[:3]

def get_price(player: str) -> int:

    """Return the price of player if the string is non-empty;
    otherwise return 0.

    Precondition: player is the string of player stats as 
    seen in players.txt

    >>> get_price('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    5
    >>> get_price('NSH_PF_G7-_A14_DC20_H73_Pr10')
    10
    >>> get_price('')
    0
    
    """
    if len(player) == 0:
        return 0
    price = player[-2:]
    if price[1] == "-":
        return int(price[0])
    return int(price)
  
# provided
def get_position(player: str) -> str:
    """Return the position of player if player is non-empty;
    otherwise return the empty string.

    Precondition: player is the string of player stats
    as seen in players.txt

    >>> get_position('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    'D'
    >>> get_position('NSH_PF_G7-_A14_DC20_H73_Pr10')
    'F'
    >>> get_position('CLA_PG_GAA2.23_SV0.910_Pr20')
    'G'
    >>> get_position('')
    ''

    """

    if len(player) == 0:
        return ''
    return player[5]

# provided as example of calling another function as helper
def is_player_available(player: str, players_available: str) -> bool:

    """Return True if and only if the id of player is in players_available.

    Precondition: player is the string of player stats
                  as seen in players.txt,
                  players_available is the string of player ids
                  that are currently available for selection seperated
                  by _.

    >>> is_player_available('MGO_PD_G0-_A14_DC43_H70_Pr5-', 'DOL_NCA_MGO_AHS_')
    True
    >>> is_player_available('GGG_PD_G0-_A14_DC43_H70_Pr5-', 'DOL_NCA_MGO_AHS_')
    False
    >>> is_player_available('', 'DOL_NCA_MGO_AHS_')
    False
    """

    if len(player) == 0:
        return False
    return get_player_id(player) in players_available

def can_select(player: str, num_forwards: int, num_defencemen: int, num_goalies: int) -> bool:
    """Return True if and only the position of player is less than the needed amount of 
    players with that same position. If player is the empty string, return True.



    """
    
    
    if len(player) == 0:
        return True

    position = get_position(player)
    if position == 'F' and (num_forwards < FORWARDS_NEEDED):
        return True
    elif position == 'D' and (num_defencemen < DEFENCEMEN_NEEDED):
        return True
    elif position == 'G' and (num_goalies < GOALIES_NEEDED):
        return True
    
    return False

def can_afford(budget: int, player: str) -> bool:
    """Return True if and only if budget is at least the price of player.

    Precondition: budget >= 0, player is the string of player stats
                  as seen in players.txt

    >>> can_afford(10, 'MGO_PD_G0-_A14_DC43_H70_Pr5-')
    True
    >>> can_afford(4, 'NSH_PF_G7-_A14_DC20_H73_Pr10')
    False
    >>> can_afford(0, '')
    False

    """
    if len(player) == 0:
        return False
    return budget >= get_price(player)

def update_budget(budget: int, player: str) -> int:
    """Return the updated budget after subtracting the price of player from budget.
    If player string is empty, return budget without changes.

    Precondition: player is in the string of player stats as seen in players.txt

    >>> update_budget(50, 'MGO_PD_G0-_A14_DC43_H70_Pr5-')
    45
    >>> update_budget(5, 'NSH_PF_G7-_A14_DC20_H73_Pr10')
    -10
    >>> update_budget(5, ''):
    5
    """ 
    return budget - int(get_price(player))     


def add_to_team(player: str, player_ids: str) -> str:
    """Return the updated string of player_ids selected by GM, after adding
    the ID of player. If player already exists in player_ids, return the 
    unchanged string of player_ids.

    Precondition: player is in the string of player stats as seen in players.txt

    >>> add_to_team('NSH_PF_G7-_A14_DC20_H73_Pr10', 'MGO_')
    'MGO_NSH_'
    >>> add_to_team('NSH_PF_G7-_A14_DC20_H73_Pr10', 'NSH_')
    'NSH_'
    >>> add_to_team('', 'NSH_')
    'NSH_'


    """

    if len(player) == 0:
        return player_ids

    chosen_id = get_player_id(player)
    if chosen_id in player_ids:
        return player_ids
    return player_ids+chosen_id+'_'
    
def remove_player(player_ids: str, player_index: int) -> str:
    """Returns the updated string of all drafted players, after removing
    the id preceding the seperator at index player_index from player_ids. 
    If the characterat player_index is not a seperator, or player_index 
    is negative, then return the unmodified string of player_ids.

    >>> remove_player('DOL_NCA_MGO_AHS_', 7)
    'OOL_MGO_AHS_'
    >>> remove_player('DOL_NCA_MGO_AHS_', 8)
    'DOL_NCA_MGO_AHS_'
    >>> remove_player('DOL_NCA_MGO_AHS_', -1)
    'DOL_NCA_MGO_AHS_'
    
    """
    if player_ids[player_index] != '_' or player_index < 0:
        return player_ids
    return player_ids[:player_index-3] + player_ids[player_index+1:]
    

def compute_dc_points(player: str) -> int:
    """Return the defensive contribution points of player.  If the player
    is a goalie or an empty string, return 0.

    Precondition: player is in the string of player stats as seen in players.txt

    >>> compute_dc_points('NSH_PF_G7-_A14_DC20_H73_Pr10')
    
    """
    position = get_position(player)
    if position == 'G' or player == '':
        return 0
    
    points = 0
    dc = player[17:19]
    if dc[1] == '-':
        dc = dc[0]
    if position == 'F':
        points = int(dc) % F_DCS_PER_POINT
    elif position == 'D':
        points = int(dc) % D_DCS_PER_POINT

    return points

def compute_goal_points(player: str) -> int:
    """
    DOCSTRING
    """
    if get_position(player) == 'G' or len(player) == 0:
        return 0
    goals = player[8:10]
    if goals[1] == '-':
        goals = goals[0]
    return int(goals) * POINTS_PER_GOAL

def compute_assist_points(player: str) -> int:
    if get_position(player) == 'G' or len(player) == 0:
        return 0
    assists = player[12:14]
    if assists[1] == '-':
        assists = assists[0]
    return int(assists) * POINTS_PER_ASSIST

def compute_hit_points(player: str) -> float:
    if get_position(player) == 'G' or len(player) == 0:
        return 0
    hits = player[21:23]
    if hits[1] == '-':
        hits = hits[0]
    return int(hits) * POINTS_PER_HIT

def compute_fantasy_score(player: str) -> float:
    if len(player) == 0:
        return 0.0
    
    if get_position(player) == 'G':
        gaa = player[10:14]
        sv = player[17:22]
        return (sv * SV_VALUE) - (gaa * GAA_VALUE)
    
    return compute_assist_points(player) + compute_goal_points(player) + compute_dc_points(player) + compute_hit_points(player)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
