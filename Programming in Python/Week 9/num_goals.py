'''Write a function named get_goals that accepts filename and the name of a country as arguments.
It should return a tuple having two elements: (num_players, num_goals).
num_players is the number of players from this country that appear in this file, num_goals is the total number of goals scored by all the players who belong to this country.
If the country is not present in the file, then return the tuple (-1, -1).'''

import pandas as pd
def get_goals(filename, country):
    goals = pd.read_csv(filename)
    want = goals[goals['Country'] == country]['Goals'].sum()
    yer = goals[goals['Country'] == country]['Player ']
    play = len(yer.unique())
    if want == 0:
        return -1,-1
    return play,want
