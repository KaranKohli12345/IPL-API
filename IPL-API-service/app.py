from flask import Flask, jsonify, request
import IPL
import jugaad

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi'

# API # 1
@app.route('/api/teams')
def teams():
    teams = IPL.teamsAPI()
    return jsonify(teams)

# API # 2
@app.route('/api/teamVsTeam')
def teamVsTeam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = IPL.teamVsTeamFunction(team1, team2)
    return jsonify(response)

# API # 3
@app.route('/api/team-record')
def team_record():
    team = request.args.get('team')
    response = jugaad.teamAPI(team)
    return response

# API # 4
@app.route('/api/batter-record')
def batter_record():
    batsman = request.args.get('batsman')
    response = jugaad.batsmanAPI(batsman)
    return response

# API # 5
@app.route('/api/bowler-record')
def bowler_record():
    bowler = request.args.get('bowler')
    response = jugaad.bowlerAPI(bowler)
    return response

# API # 6
@app.route('/api/players')
def players_API():
    players = IPL.players_list()
    return jsonify(players)

app.run(debug=True)
