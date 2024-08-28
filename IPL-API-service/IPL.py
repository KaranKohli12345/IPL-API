import pandas as pd

matches = pd.read_csv(r'CSV Files\ipl-matches.csv')
# print(matches.head())

def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    teams_dict = {
        'teams': sorted(teams)
    }
    return teams_dict

def teamVsTeamFunction(team1, team2):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))

    if ((team1 in valid_teams) & (team2 in valid_teams)):
        temp_df = matches[((matches['Team1'] == team1) & (matches['Team2'] == team2)) | 
        ((matches['Team1'] == team2) & (matches['Team2'] == team1))]
        
        total_matches_bw_two_teams = temp_df.shape[0]

        matches_won_by_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_by_team2 = temp_df['WinningTeam'].value_counts()[team2]
        
        draws = total_matches_bw_two_teams - (matches_won_by_team1 + matches_won_by_team2)

        response = {
            'Total matches played': int(total_matches_bw_two_teams),
            'Matches won by ' + team1: int(matches_won_by_team1),
            'Matches won by ' + team2: int(matches_won_by_team2),
            'Draw': int(draws)
        }      
        return response 
    else:
        return {'message': 'Invalid team name'}
    

def team_record(team):
    team_matches_df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)]

    total_matches_played = team_matches_df.shape[0]

    toss_wins = team_matches_df[team_matches_df['TossWinner'] == team].shape[0]

    matches_won = team_matches_df[team_matches_df['WinningTeam'] == team].shape[0]

    team_record = {
        'Total matches played': total_matches_played,
        'Toss wins': toss_wins,
        'Matches won': matches_won
    }

    return team_record




