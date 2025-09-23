# Title: Baseball Game
# Date: September 17, 2025
# Programmers: Arun Rajakumar
# Description: This Baseball Game is a text-based game simulator where you can 
#              feel the joy of baseball by watching a graphic simulation. 
#              The game of baseball consists of 9 innings, with each player 
#              batting once per inning unless struck out. This program
#              simulates players' scores through a hard-coded database.
#              After the team's struck out, the opponent's score is randomly 
#              generated.

###############################################################################

# Import random module
import random

# Define functions (Modularity)
# Function to read player_statistics.txt file
def read_player_statistics (players_files):
    statistics_file_input = players_files
    player_statistics_file = open (statistics_file_input, "r")
    players = []
    
    for line in player_statistics_file: # Forms dictionary for each player
        
        txt_data = line.split ()
        
        player = {
            "Name": txt_data[0],
            "1B": float (txt_data[1]),
            "2B": float (txt_data[2]),
            "3B": float (txt_data[3]),
            "HB": float (txt_data[4])
        }
        
        players.append (player)
            
    return players

# Assign txt file to a variable
players = read_player_statistics ("player_statistics.txt")

print("SATEC @ W.A. Porter - ICS4U Baseball")
print("Welcome to the Baseball Game Simulator!")
# Ask user input for team name
team_name = input ("\n\nPlease enter your team name: ")
seperator = "-----------------------------------------------------------------------------"
# User Introduction
print ()
print (f"Welcome to the baseball game, Team {team_name}!!")
print (seperator)
input (f"\nPress ENTER to start the game\n")

# Initialize variables and constants
INNINGS = 9
num_players = len (players)
player_counter = 0
outs = 0
runs = 0
opponent_runs = 0
bases = ["", "", ""]
team_inning_scores = []
opponent_inning_scores = []
OPP_ZERO_RUN_CHANCE = 50
OPP_ONE_RUN_CHANCE = 20
OPP_TWO_RUN_CHANCE = 14
OPP_THREE_RUN_CHANCE = 7
OPP_FOUR_RUN_CHANCE = 5
OPP_FIVE_RUN_CHANCE = 3
OPP_SIX_RUN_CHANCE = 1

# Function to decide the outcome of each hit per player
def batting (player):
    global outs, runs
    
    hit_chance = random.randrange (0, 100)
    
    if (hit_chance < (player ['1B'] * 100)):
        base_players (1, player)

    elif (hit_chance < (player ['1B'] * 100) + (player ['2B'] * 100)):
        base_players (2, player)

    elif (hit_chance < (player ['1B'] * 100) + (player ['2B'] * 100) 
          + (player ['3B'] * 100)):
        base_players (3, player)

    elif (hit_chance < (player ['1B'] * 100) + (player ['2B'] * 100) 
          + (player ['3B'] * 100) + (player ['HB'] * 100)):
        base_players (4, player)

    else:
        print (f"\n{player ['Name']} misses and is out!\n")
        print (seperator)
        outs += 1

# Function to determine if a player scores or is out        
def base_players (bases_run, player):
    global runs

    if bases_run == 1:
        print (f"\n{player ['Name']} hits a Single!")
    elif bases_run == 2:
        print (f"\n{player ['Name']} hits a Double!")
    elif bases_run == 3:
        print (f"\n{player ['Name']} hits a Triple!")
    elif bases_run == 4:
        print (f"\n{player ['Name']} hits a Home Run!")
    print (seperator)

    for i in reversed (range (3)):
        if bases [i]:
            if (i + bases_run > 2):
                runs += 1
                
                print (f"{bases [i]} SCORES!!!")
                print (seperator)
                bases [i] = ""
            else:
                bases [bases_run + i] = bases [i]
                bases [i] = ""
        
    if (bases_run < 4):
        bases[bases_run - 1] = player['Name']
    else:
        runs += 1

# Function providing inning and score updates after every hit    
def score_updates (inning):
    print (f"\n{seperator}")
    print (f"Inning Updates:\n{seperator}")
    print (f"Inning: {inning + 1} \nTotal Runs: {runs} \nOuts: {outs}")
    print (seperator)
    print (f"First Base: {bases [0]} \nSecond Base: {bases [1]} \n" + 
           f"Third Base: {bases [2]} ")
    print (seperator)

# Main loop
for inning in range (INNINGS):
    outs = 0
    bases = ["", "", ""]
    print (f"\n-------------------- Inning {inning + 1} ---------------------")
    
    # Loops for every inning (based on outs)
    while outs < 3:

        player = players [(player_counter) % num_players]

        # Visual graphics for the base layout
        input (f"\nPress Enter for Current Base Layout for Team {team_name}\n")
        print (f"\n                 Current Base Layout: (Team {team_name})\n")
        print(f"| Home Base | 1st Base | 2nd Base | 3rd Base |")
        print(f"|--------------------------------------------|")
        print(f"| {player ['Name']:9} | {bases [0]:8} | {bases [1]:8} | {bases [2]:8} |")
        # print (f"                           2nd Base ({bases [1]})")
        # print ("                              /|\\ ")
        # print ("                             / | \\  ")
        # print ("                            /  |  \\  ")
        # print ("                           /   |   \\  ")
        # print (f"       ({bases [2]:10}) 3rd Base ---- 1st Base ({bases [0]})")
        # print ("                           \\   |   /")
        # print ("                            \\  |  /")
        # print ("                             \\ | /")
        # print ("                              \\|/")
        # print (f"                             Home ({player ['Name']})")    
        print (seperator)

        # Player statistics
        print (f"\nAt-Bat ({player ['Name']}) Statistics:        " 
               + f"1B: {player ['1B']}  2B: {player ['2B']}   "
               + f"3B: {player ['3B']}  HB: {player ['HB']}\n")
        print (seperator)
        
        # Ask user for a response for the player to bat
        input (f"Click Enter for {player ['Name']} to bat\n")
        print (seperator)
        
        # Calls above functions for the program
        batting (player)
        input (f"Click Enter for Current Inning Updates")
        score_updates (inning)
        
        # Code to manage to manage and/or reset player order
        player_counter += 1
        if (player_counter == num_players):
            player_counter = 0

    # Code to randomly generate opposition score
    opp_runs_inning = 0
    opp_chance = random.randrange (0, 100)
    
    if (opp_chance < OPP_ZERO_RUN_CHANCE):
        opp_runs_inning = 0
    elif (opp_chance < OPP_ZERO_RUN_CHANCE + OPP_ONE_RUN_CHANCE):
        opp_runs_inning = 1
    elif (opp_chance < OPP_ZERO_RUN_CHANCE + OPP_ONE_RUN_CHANCE 
          + OPP_TWO_RUN_CHANCE):
        opp_runs_inning = 2
    elif (opp_chance < OPP_ZERO_RUN_CHANCE + OPP_ONE_RUN_CHANCE 
          + OPP_TWO_RUN_CHANCE + OPP_THREE_RUN_CHANCE):
        opp_runs_inning = 3
    elif (opp_chance < OPP_ZERO_RUN_CHANCE + OPP_ONE_RUN_CHANCE 
          + OPP_TWO_RUN_CHANCE + OPP_THREE_RUN_CHANCE + OPP_FOUR_RUN_CHANCE):
        opp_runs_inning = 4
    elif (opp_chance < OPP_ZERO_RUN_CHANCE + OPP_ONE_RUN_CHANCE 
          + OPP_TWO_RUN_CHANCE + OPP_THREE_RUN_CHANCE + OPP_FOUR_RUN_CHANCE 
          + OPP_FIVE_RUN_CHANCE):
        opp_runs_inning = 5
    else:        
        opp_runs_inning = 6
    
    opponent_runs += opp_runs_inning

    team_runs_inning = runs - sum(team_inning_scores)  # runs this inning
    team_inning_scores.append(team_runs_inning)

    opponent_inning_scores.append(opp_runs_inning)

    print (f"Current Scores:         " 
           + f"Team {team_name}: {runs}       Opponent: {opponent_runs}")

    # Code to show End of Inning updates
    print (seperator)
    print ("Inning-by-Inning Scores:")
    print(f"Team {team_name}:     ", end="")
    for r in team_inning_scores:
        print(f"{r} ", end="")
    print()

    print("Opponent:     ", end="")
    for r in opponent_inning_scores:
        print(f"{r} ", end="")
    print()
    print (seperator)

    # Code displayed when game is over
    if (inning == INNINGS - 1):
        print (f"\n---------------------- Game Over -------------------------")
        print (f"Final Score for Team {team_name}: {runs}")
        print (f"Opposition Score: {opponent_runs}")
        print (seperator)

        # Code calculating the winner of the game
        if (runs > opponent_runs):
            print(f"Congratulations!!! " 
                  + f"Team {team_name} wins {runs}-{opponent_runs}")
        elif (runs < opponent_runs):
            print(f"Oops! Team {team_name} loses {runs}-{opponent_runs}")
        else:
            print(f"Close Game. It's a draw!!! {runs}-{opponent_runs}")
        
        print (seperator)

input ()
